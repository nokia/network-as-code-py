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
          - name: python
            image: docker-registry-remote.artifactory-espoo1.int.net.nokia.com/python:3.11-slim
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
        string(name: 'gitlabSourceBranch', defaultValue: 'main', description: 'Default branch used when built on-demand', trim: true)
    }
    environment {
        PYPI_REPOSITORY = credentials('PYPI_REPOSITORY')
        PYPI_USERNAME = credentials('PYPI_USERNAME')
        PYPI_PASSWORD = credentials('PYPI_PASSWORD')
        PYPI_TOKEN = credentials('PYPI_TOKEN')
        NAC_TOKEN = credentials('NAC_TOKEN')
        NAC_TOKEN_PROD = credentials('NAC_TOKEN_PROD')
        TEAMS_WEBHOOK = credentials('TEAMS_WEBHOOK')
        SDK_NOTIFICATION_SERVER_URL = credentials('SDK_NOTIFICATION_SERVER_URL')
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
        stage('Setup tools') {
            steps {
                container('python') {
                    script {
                        sh """
                        pip install uv
                        uv sync
                        """
                    }
                }        
            }
        }
        stage('Linting') {
            steps {
                container('python') {
                    script {
                        sh """
                        uv run pylint network_as_code
                        uv run mypy network_as_code
                        """
                    }
                }        
            }
        }
        stage('Test') {
            steps {
                container('python') {
                    script {
                        sh """
                            uv run pytest -n auto --cov-config=.coveragerc --cov-report term --cov-report xml:coverage.xml --cov=network_as_code
                        """
                    }
                }        
            }
        }
        stage('Audit') {
            steps {
                container('python') {
                    script {
                        sh """
                            https_proxy="http://fihel1d-proxy.emea.nsn-net.net:8080" python3 -m uv run pip-audit
                        """
                    }
                }
            }
        }
        stage('Integration Test') {
            when { expression { env.gitlabActionType != "TAG_PUSH" } }
            steps {
                container('python') {
                    script {
                        sh """
                            env | grep gitlab
                            http_proxy="http://fihel1d-proxy.emea.nsn-net.net:8080" https_proxy="http://fihel1d-proxy.emea.nsn-net.net:8080" python3 -m uv run pytest -n 8 --dist worksteal integration_tests/
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
        stage('Build') {
            steps {
                container('python') {
                    script {
                        sh """
                            python3 -m uv build
                        """
                    }
                }
            }
        }
        stage('Installation Test') {
            when { expression { env.gitlabActionType == "TAG_PUSH" && 
            (env.gitlabBranch.contains("rc-") || env.gitlabBranch.contains("release-"))} }
            steps {
                container('python') {
                    script {
                        sh '''
                            python3 -m venv venv
                            . venv/bin/activate
                            python3 -m pip install pytest python-dotenv toml
                            version=$(python3 -m extract_version)
                            python3 -m pip install dist/network_as_code-${version}.tar.gz
                            python3 -m pytest installation_tests/
                        '''
                    }
                }
            }
        }
        stage('Candidate integration tests against production') {
            when { expression { env.gitlabActionType == "TAG_PUSH" && env.gitlabBranch.contains("rc-")} }
            steps {
                container('python') {
                    script {
                        sh """
                        env | grep gitlab
                        """
                        if(env.gitlabActionType == "TAG_PUSH" && env.gitlabBranch.contains("rc-")){
                            sh '''
                                http_proxy="http://fihel1d-proxy.emea.nsn-net.net:8080" https_proxy="http://fihel1d-proxy.emea.nsn-net.net:8080" PRODTEST=1 python3 -m uv run pytest integration_tests/
                            '''
                        }
                    }
                }
            }
        }
        stage('Release integration tests against production') {
            when { expression { env.gitlabActionType == "TAG_PUSH" && env.gitlabBranch.contains("release-")} }
            steps {
                container('python') {
                    script {
                        sh """
                        env | grep gitlab
                        """
                        if(env.gitlabActionType == "TAG_PUSH" && env.gitlabBranch.contains("release-")){
                            sh '''
                            http_proxy="http://fihel1d-proxy.emea.nsn-net.net:8080" https_proxy="http://fihel1d-proxy.emea.nsn-net.net:8080" PRODTEST=1 python3 -m uv run pytest integration_tests/
                            '''
                        }
                    }
                }
            }
        }
        stage('Deploy release') {
            when { expression { env.gitlabActionType == "TAG_PUSH" && env.gitlabBranch.contains("release-")} }
            steps {
                container('python') {
                    script {
                        sh """
                        env | grep gitlab
                        """
                        if(env.gitlabActionType == "TAG_PUSH" && env.gitlabTargetBranch.contains("release-")){
                            sh '''
                                export UV_PUBLISH_TOKEN=$PYPI_TOKEN
                                python3 -m uv build
                                https_proxy="http://fihel1d-proxy.emea.nsn-net.net:8080" python3 -m uv publish
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
