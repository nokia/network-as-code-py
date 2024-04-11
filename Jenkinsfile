#!/bin/groovy

def jenkinsBuildToken
withCredentials([string(credentialsId: 'gitlab-build-secret-token-sdk-py', variable: 'buildToken')]) {
 jenkinsBuildToken = "${buildToken}"
}

pipeline {
    agent {
        kubernetes {
            label "k8s-sdk-py-${cto.devops.jenkins.Utils.getTimestamp()}"
            inheritFrom 'k8s-proxy'
            yaml """
        spec:
          containers:
          - name: beluga
            image: sf-docker-releases.repo.lab.pl.alcatel-lucent.com/abllabs/beluga:latest
            workingDir: /home/jenkins
            tty: true
            command:
            - cat
          - name: sonar
            image: registry1-docker-io.repo.cci.nokia.net/sonarsource/sonar-scanner-cli:5.0.1
            workingDir: /home/jenkins
            tty: true
            command:
            - cat
      """
        }
    }
    triggers {
        gitlab(
            triggerOnPush: true,
            branchFilterType: 'All',
            triggerOnMergeRequest: true,
            triggerOpenMergeRequestOnPush: "never",
            triggerOnNoteRequest: true,
            triggerOnAcceptedMergeRequest: true,
            noteRegex: "Jenkins please retry a build",
            skipWorkInProgressMergeRequest: true,
            ciSkip: false,
            setBuildDescription: true,
            addNoteOnMergeRequest: true,
            addCiMessage: true,
            addVoteOnMergeRequest: true,
            acceptMergeRequestOnSuccess: true,
            cancelPendingBuildsOnUpdate: false,
            secretToken: jenkinsBuildToken
        )
    }
    parameters {
        string(name: 'gitlabSourceBranch', defaultValue: 'master', description: 'Default branch used when built on-demand', trim: true)
    }
    environment {
        PYPI_REPOSITORY = credentials('PYPI_REPOSITORY')
        PYPI_USERNAME = credentials('PYPI_USERNAME')
        PYPI_PASSWORD = credentials('PYPI_PASSWORD')
        PYPI_TOKEN = credentials('PYPI_TOKEN')
        NAC_TOKEN = credentials('NAC_TOKEN')
        TEAMS_WEBHOOK = credentials('TEAMS_WEBHOOK')
        SONAR_PATH = "/opt/sonar-scanner/bin"
        SONAR_TOKEN = "sonar-token"
    }
    options {
        gitLabConnection('gitlab-ee2')  // the GitLab connection name defined in Jenkins, check the value from pipeline configure UI
        timeout(time: 60, unit: 'MINUTES')
        buildDiscarder(logRotator(daysToKeepStr: '30', artifactDaysToKeepStr: '1'))
        disableConcurrentBuilds()
        timestamps()
    }

    stages {
        stage('Test') {
            steps {
                container('beluga') {
                    script {
                        sh """
                            python3 -m poetry --no-cache install
                            poetry run pytest --cov-config=.coveragerc --cov-report term --cov-report xml:coverage.xml --cov=network_as_code
                        """
                    }
                }        
            }
        }
        stage('Integration Test') {
            steps {
                container('beluga') {
                    script {
                        sh """
                            env | grep gitlab
                            https_proxy="http://fihel1d-proxy.emea.nsn-net.net:8080" python3 -m poetry run pytest integration_tests/
                        """
                    }
                }        
            }
        }
        stage('Sonar Scan') {
            steps {
                withCredentials([string(credentialsId: "${SONAR_TOKEN}", variable: 'sonar_login')]) {
                    container('sonar') {
                        script {
                            sh """
                                export PATH=$PATH:${SONAR_PATH}
                                sonar-scanner \
                                    -Dsonar.projectKey=nac-sdk-py \
                                    -Dsonar.sources=./network_as_code \
                                    -Dsonar.tests=./tests \
                                    -Dsonar.host.url=${SONARQUBE_HTTPS_URL} \
                                    -Dsonar.login=${sonar_login} \
                                    -Dsonar.python.coverage.reportPaths=coverage.xml
                            """
                        }
                    }
                }
            }
        }
        stage('Audit') {
            steps {
                container('beluga') {
                    script {
                        sh """
                            https_proxy="http://fihel1d-proxy.emea.nsn-net.net:8080" python3 -m poetry run pip-audit
                        """
                    }
                }
            }
        }
        stage('Build') {
            steps {
                container('beluga') {
                    script {
                        sh """
                            python3 -m poetry install
                            python3 -m poetry build
                        """
                    }
                }
            }
        }
        stage('Deploy candidate') {
            when { expression { env.gitlabActionType == "TAG_PUSH" && env.gitlabTargetBranch.contains("rc-")} }
            steps {
                container('beluga') {
                    script {
                        sh """
                        env | grep gitlab
                        """
                        if(env.gitlabActionType == "TAG_PUSH" && env.gitlabTargetBranch.contains("rc-")){
                            sh '''
                                python3 -m poetry config repositories.devpi ${PYPI_REPOSITORY}
                                python3 -m poetry build
                                python3 -m poetry publish --no-interaction -r devpi -u ${PYPI_USERNAME} -p ${PYPI_PASSWORD}
                            '''
                        }
                    }
                }
            }
        }
        stage('Deploy release') {
            when { expression { env.gitlabActionType == "TAG_PUSH" && env.gitlabTargetBranch.contains("release-")} }
            steps {
                container('beluga') {
                    script {
                        sh """
                        env | grep gitlab
                        """
                        if(env.gitlabActionType == "TAG_PUSH" && env.gitlabTargetBranch.contains("release-")){
                            sh '''
                                python3 -m poetry config pypi-token.pypi ${PYPI_TOKEN}
                                python3 -m poetry build
                                https_proxy="http://fihel1d-proxy.emea.nsn-net.net:8080" python3 -m poetry publish --no-interaction
                            '''
                        }
                    }
                }
            }
        }
    }
    post {
        success{
            updateGitlabCommitStatus name: 'build', state: 'success'
        }
        failure{
            postToTeams("Jenkins build failed see ${env.BUILD_URL} for more.", "${TEAMS_WEBHOOK}")
            updateGitlabCommitStatus name: 'build', state: 'failed'
        }
    }
}
