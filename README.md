# staircase

As a user I like to see how many times the helloworld service has been invoked 

* Create a service which return helloworld

  * Serverless framework

  * Lambda

  * API Gateway

* Everytime the service is called there is a new record added to the invocation file in S3

* A QuickSight report is created automatically which display #times the service is invoked 

* Call the service multiple times

* Report should be refreshed automatically with the total number of invocations

* Test the service automatically to make sure it returns helloworld

* Change the code to response with byeworld, should result in deployment rejection
