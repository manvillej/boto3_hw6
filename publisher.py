"""

"""

# std library
import os

# custom library
from src import randIntGenerator

# 3rd party packages
import boto3

def main():
	topic = os.environ['SNS_ARN']
	iterations = os.environ.get('PUBLISHER_ITERATIONS', 1000)
	sleep_time = os.environ.get('PUBLISHER_SLEEP_TIME', 5)
	sns = boto3.client('sns')
	for i in randIntGenerator(iterations, sleep_time):
		sns.publish(
		    TopicArn=topic,    
		    Message=i,)

if __name__ == '__main__':
	main()