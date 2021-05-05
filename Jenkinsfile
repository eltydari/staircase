pipeline {
    agent any

    stages {
        stage('Test') {
            steps {
                echo 'Testing...'
                sh '/usr/local/bin/tox'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
    }
}