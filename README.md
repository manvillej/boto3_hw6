# boto3

## Requirements:
you must have the aws cli install and have your access_key and secret_key set. 

## Publisher
### install
.$> pip install requirements.txt

### run
.$> set SNS_ARN=<SNS_ARN>

.$> python publisher.py

## Consumer
### install
.$> pip install requirements.txt

### run
.$> set SQS_QUEUE_URL=<SQS_QUEUE_URL>

.$> python consumer.py

