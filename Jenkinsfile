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
                script {
                    docker.build('lambda-docker-hello')
                }
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
                script {
                    docker.withRegistry('https://362764577362.dkr.ecr.us-east-2.amazonaws.com/default', 'jenkins-ecr-default') {
                        docker.image('lambda-docker-hello').push()
                    }
                }
            }
        }
    }
}