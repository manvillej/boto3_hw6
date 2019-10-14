"""

"""

# std library
import time
import os
import json

# 3rd party packages
import boto3

# custom library
from src import OddsAndEvensCounter as Counter


def main():
    sqs_queue_url=os.environ['SQS_QUEUE_URL']
    sqs_client = boto3.client('sqs')
    counter = Counter()

    while(True):
        response = sqs_client.receive_message(
            QueueUrl=sqs_queue_url, 
            MaxNumberOfMessages=1, 
            WaitTimeSeconds=0)

        try:
            messages = response['Messages']
        except KeyError:
            continue

        for message in messages:
            SNSMessage = json.loads(message['Body'])

            try:
                counter.count(int(SNSMessage['Message']))
                print(counter)
            except ValueError:
                pass

            sqs_client.delete_message(
                QueueUrl=sqs_queue_url,
                ReceiptHandle=message['ReceiptHandle'])

        time.sleep(1)


if __name__ == '__main__':
    main()
