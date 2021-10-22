pipeline {
    agent any

    stages {



        stage('Build') {
            steps {
                sh """
				    PATH=${PATH}:/usr/local/bin
				    python -m venv venv
				    . venv/bin/activate
				    pip install -r tests/requirements.txt
				    pytest -v tests --junitxml=report.xml
                """
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