pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'chmod +x install.sh'
                sh './install.sh'
                sh 'pip3 install pytest'
            }
        }
        stage('Test') {
            steps {
                sh '/var/jenkins_home/.local/bin/pytest -v tests'
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
