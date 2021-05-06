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
                sh 'mkdir -p ./build'
                sh 'pushd lambdas; zip ../build/deployment.zip ./lambda_function.py; popd'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
                s3Upload consoleLogLevel: 'INFO', dontSetBuildResultOnFailure: false, dontWaitForConcurrentBuildCompletion: false, entries: [[bucket: 'staircase-demo/bin', excludedFile: '', flatten: false, gzipFiles: false, keepForever: false, managedArtifacts: false, noUploadOnFailure: true, selectedRegion: 'us-east-2', showDirectlyInBrowser: false, sourceFile: 'output/deployment.zip', storageClass: 'STANDARD', uploadFromSlave: false, useServerSideEncryption: false]], pluginFailureResultConstraint: 'FAILURE', profileName: 'JenkinsEC2', userMetadata: []
            }
        }
    }
}