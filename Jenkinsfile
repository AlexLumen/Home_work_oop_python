pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'chmod +x install.sh'
                sh './install.sh'
            }
        }
        stage('Test') {
            steps {
                sh 'chmod 777 nodeids ./venv/lib/python3.9/site-packages/pytest'
                sh './venv/lib/python3.9/site-packages/pytest --url ${APP_URL} --executor ${EXECUTOR} --browser ${BROWSER} --alluredir allure-results'
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
