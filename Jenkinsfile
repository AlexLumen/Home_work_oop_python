pipeline {
    agent any

    stages {



        stage('Build') {
            steps {
                sh """
				    PATH=$PATH:$PWD/build
				    echo $PATH
				    apt-get install python3-venv
				    python3 -m venv venv
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
