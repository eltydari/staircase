pipeline {
    agent any

    stages {
        stage('Test') {
            steps {
                echo 'Testing...'
                sh '/usr/local/bin/tox'
            }
        }
        stage('Prepackage') {
            steps {
                sh 'rm ~/.dockercfg || true'
                sh 'rm ~/.docker/config.json || true'
            }
        }
        stage('Package'){
            steps {
                echo 'Packaging...'
                docker.build('lambda-docker-hello')
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
                docker.image('lambda-docker-hello').push()
            }
        }
    }
}