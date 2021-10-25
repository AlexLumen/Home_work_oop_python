pipeline {
    agent any

    stages {



        stage('Build') {
            steps {
                sh """
				    PATH=$PATH:$PWD/build
				    echo $PATH
				    python3 -m venv venv
				    pip3 install -r requirements.txt
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
