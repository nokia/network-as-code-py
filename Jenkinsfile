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
    PYPI_REPOSITORY = "${PYPI_REPOSITORY}"
    PYPI_USERNAME = "${PYPI_USERNAME}"
    PYPI_PASSWORD = "${PYPI_PASSWORD}"
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
              python3 -m poetry run pytest --cov=network_as_code
            """
          }
        }        
      }
    }
    stage('Integration Test') {
      when { expression { env.gitlabActionType == "TAG_PUSH" && env.gitlabTargetBranch.contains("release-")} }
      steps {
        container('beluga') {
          script {
            sh """
              env | grep gitlab
            """
            if(env.gitlabTargetBranch.contains("release-") && env.gitlabActionType == "TAG_PUSH") {
              sh """
                export http_proxy=http://fihel1d-proxy.emea.nsn-net.net:8080
                export https_proxy=https://fihel1d-proxy.emea.nsn-net.net:8080
                python3 -m poetry run pytest integration_tests/
              """
            }
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
    stage('Deploy') {
      steps {
        container('beluga') {
          withCredentials([
            string(credentialsId: "${PYPI_PASSWORD}", variable: 'PYPI_PASSWORD'),
            string(credentialsId: "${PYPI_USERNAME}", variable: 'PYPI_USERNAME'),
            string(credentialsId: "${PYPI_REPOSITORY}", variable: 'PYPI_REPOSITORY')
          ]) {
            script {
              sh """
                env | grep gitlab
              """
              if(env.gitlabActionType == "TAG_PUSH" && env.gitlabTargetBranch.contains("release-")){
                sh '''
                  python3 -m poetry config repositories.devpi ${PYPI_REPOSITORY}
                  python3 -m poetry publish --build -r devpi -u ${PYPI_USERNAME} -p ${PYPI_PASSWORD}
                '''
              }
            }
          }
        }
      }
    }
  }
}
