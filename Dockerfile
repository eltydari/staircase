# set a base image that includes Lambda Runtime API:
# Source: https://hub.docker.com/ramazon/aws-lambda-python
FROM amazon/aws-lambda-python:3.7

# optional: ensure that pip is up to date
RUN pip install --upgrade pip

# first we COPY only requirements.txt to ensure that later builds
# with changes to your src code will be faster due to caching of this layer
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy all your custom modules and files from the src directory
COPY src/ .

# specify lambda handler that will be invoted on container start
CMD [ "lambda_function.lambda_handler" ]