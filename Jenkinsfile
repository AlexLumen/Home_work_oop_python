pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                    PATH=$PATH:$WORKSPACE
				    python -m venv venv
				    . venv/bin/activate
				    pip install -r requirements.txt
            }
        }
        stage('Test') {
            steps {
                sh './env/bin/pytest --url ${URL} --executor ${EXECUTOR} --browser ${BROWSER} --alluredir allure-results'
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
