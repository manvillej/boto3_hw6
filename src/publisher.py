"""

"""

# std library
import random
import time

def randIntGenerator(iterations, sleep_time):
	""""""
	for i in range(iterations):
		yield f'{random.randint(1, 100)}'
		time.sleep(sleep_time)

