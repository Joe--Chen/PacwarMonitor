__author__ = "Zhouhan Chen"
__email__ = "zc12@rice.edu"

import time
import sys
import random

hamming = 30
avg = 0.1
max_score = 0.1
count = 0

if len(sys.argv) < 2:
	print("not enough input arguments")
	exit()

date = sys.argv[1]
instance_number = sys.argv[2]

with open(date + "_instance_" + instance_number + ".log", "w") as f:
	while count < 100:
		hamming -= random.uniform(-0.4, 1) * 0.2
		avg += random.uniform(-0.7, 1) * 0.5
		max_score += random.uniform(-0.7, 1) * 0.6
		f.write("INFO:root:"+str(avg)+","+str(max_score)+","+str(hamming)+"\n")
		f.flush()
		count += 1
		print("%d-th iteration" %(count))
		time.sleep(1)

