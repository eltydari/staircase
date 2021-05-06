pipeline {
    agent any

    stages {
        stage('Test') {
            steps {
                echo 'Testing...'
                sh '/usr/local/bin/tox'
            }
        }
        stage('Package'){
            steps {
                echo 'Packaging...'
                sh 'mkdir -p ./output'
                sh 'zip ./output/deployment.zip ./lambdas/lambda_function.py'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
    }
}