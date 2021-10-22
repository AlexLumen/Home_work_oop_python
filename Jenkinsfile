pipeline {
    agent any

    stages {
        stage("Prepare container") {
      agent {
        docker {
          image 'python:latest'
        }
      }
        stage('Prepair') {
            steps {
                sh 'python --version'
            }
        }
        stage('Build') {
            steps {
                sh 'chmod +x install.sh'
                sh './install.sh'
            }
        }
    }

    post {

        always {

            script {
                allure([
                        includeProperties: false,
                        jdk: '',
                        properties: [],
                        reportBuildPolicy: 'ALWAYS',
                        results: [[path: 'allure-results']]
                ])
            }

            cleanWs()
        }
    }
}