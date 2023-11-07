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
    PYPI_REPOSITORY = credentials('PYPI_REPOSITORY')
    PYPI_USERNAME = credentials('PYPI_USERNAME')
    PYPI_PASSWORD = credentials('PYPI_PASSWORD')
    NAC_TOKEN = credentials('NAC_TOKEN')
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
      steps {
        container('beluga') {
          script {
            sh """
              env | grep gitlab
              python3 -m poetry run pytest integration_tests/
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
    stage('Deploy') {
      when { expression { env.gitlabActionType == "TAG_PUSH" && env.gitlabTargetBranch.contains("release-")} }
      steps {
        container('beluga') {
            script {
              sh """
                env | grep gitlab
              """
              if(env.gitlabActionType == "TAG_PUSH" && env.gitlabTargetBranch.contains("release-")){
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
  }
  post {
    success{
      updateGitlabCommitStatus name: 'build', state: 'success'
    }
    failure{
      postToTeams("Jenkins build failed see ${env.BUILD_URL} for more.", 'https://nokia.webhook.office.com/webhookb2/aa652e35-891b-4c8d-890b-fac0296cc4d1@5d471751-9675-428d-917b-70f44f9630b0/IncomingWebhook/81dabf069f9d4e63af24a0a66b0d2fd4/9c73183b-22f9-4e0e-91c3-bd336ea99d77')
      updateGitlabCommitStatus name: 'build', state: 'failed'
    }
  }
}
