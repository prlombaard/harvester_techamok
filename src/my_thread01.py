# https://convertkit.s3.amazonaws.com/assets/documents/8985/937101/scaling-python-sample.pdf

import threading
import random

results = []

def compute():
    results.append(sum([random.randint(1,100) for i in range(1000000)]))

workers = [threading.Thread(target=compute) for x in range(8)]

for worker in workers:
    worker.start()
for worker in workers:
    worker.join()
print("Results: %s" % results)