pipeline {
    agent any

    stages {
        stage('Test') {
            steps {
                echo 'Testing...'
                sh '/usr/local/bin/tox'
            }
        }
        stage('Package') {
            steps {
                echo 'Packaging...'
                sh 'rm ~/.dockercfg || true'
                sh 'rm ~/.docker/config.json || true'
                script {
                    docker.build('lambda-docker-hello')
                }
            }
        }
        stage('Upload'){
            steps {
                echo 'Uploading to ECR...'
                script {
                    docker.withRegistry('https://362764577362.dkr.ecr.us-east-2.amazonaws.com/lambda-docker-hello', 'ecr:us-east-2:jenkins-ecr-default') {
                        docker.image('lambda-docker-hello').push()
                    }
                }
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
                sh '/usr/local/bin/aws lambda update-function-code --function-name getHello --image-uri "https://362764577362.dkr.ecr.us-east-2.amazonaws.com/lambda-docker-hello:latest"'
            }
        }
    }
}