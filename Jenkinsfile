pipeline {
    agent any

    stages {



        stage('Build') {
            steps {
                sh """
				    PATH=$PATH:$PWD/build
				    echo $PATH
				    sudo apt install python3-venv
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
