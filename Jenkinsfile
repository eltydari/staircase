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
                sh 'rm -rf ./build'
                sh 'mkdir ./build'
                sh 'zip -j ./build/deployment.zip ./lambdas/lambda_function.py'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
                s3Upload consoleLogLevel: 'INFO', dontSetBuildResultOnFailure: false, dontWaitForConcurrentBuildCompletion: false, entries: [[bucket: 'staircase-demo/bin', excludedFile: '', flatten: false, gzipFiles: false, keepForever: false, managedArtifacts: false, noUploadOnFailure: true, selectedRegion: 'us-east-2', showDirectlyInBrowser: false, sourceFile: 'build/deployment.zip', storageClass: 'STANDARD', uploadFromSlave: false, useServerSideEncryption: false]], pluginFailureResultConstraint: 'FAILURE', profileName: 'JenkinsEC2', userMetadata: []
            }
        }
    }
}