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
    PYPI_REPOSITORY = 'test_pypi_repository'
    PYPI_USERNAME = "${PYPI_USERNAME}"
    PYPI_PASSWORD = "${PYPI_PASSWORD}"
  }
  stages {
    stage('Test') {
      steps {
        container('beluga') {
          script {
            sh """
              python3 -m poetry install
              python3 -m poetry run pytest
            """
          }
        }        
      }
    }
    stage('Version bumping') {
      steps {
        container('beluga') {
          script {
            sh """
              python3 -m poetry version \$(git describe --tags --abbrev=0)
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
      steps {
        container('beluga') {
          script {
            sh """
              python3 -m poetry config repositories.devpi ${PYPI_REPOSITORY}
              python3 -m poetry publish --build -r devpi -u ${PYPI_USERNAME} -p ${PYPI_PASSWORD}
            """
          }
        }
      }
    }
  }
}
