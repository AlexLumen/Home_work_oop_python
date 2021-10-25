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
                sh """
				    PATH=$PATH:$WORKSPACE
				    python3 -m venv venv
				    . venv/bin/activate
				    pip3 install -r tests/requirements.txt
				    pytest -v tests --url ${APP_URL} --executor ${EXECUTOR} --browser ${BROWSER} --alluredir allure-results --junitxml=report.xml
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
