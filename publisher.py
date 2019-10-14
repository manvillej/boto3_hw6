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
	sns = boto3.client('sns')
	for i in randIntGenerator(4, .5):
		sns.publish(
		    TopicArn=topic,    
		    Message=i,)

if __name__ == '__main__':
	main()