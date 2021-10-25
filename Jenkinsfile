pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'python3 -m venv venv'
		sh 'pip3 install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
		    sh 'pytest -v tests --url ${APP_URL} --executor ${EXECUTOR} --browser ${BROWSER} --alluredir allure-results'
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
