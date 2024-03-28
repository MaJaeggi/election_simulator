#a first past the post election system for a single seat or office.

#import the libraries needed
import random

#Define the probabilities for each bucket
prob_bucket1 = 0.40
prob_bucket2 = 0.10
prob_bucket3 = 0.50

#Initialise counts for each bucket
bucket1_count = 0
bucket2_count = 0
bucket3_count = 0

#Simulate the distribution of stones
total_stones = 100
for _ in range(total_stones):
    rand_num = random.random()  #Generate a random number between 0 and 1
    if rand_num < prob_bucket1:
        bucket1_count += 1
    elif rand_num < prob_bucket1 + prob_bucket2:
        bucket2_count += 1
    else:
        bucket3_count += 1

#Display the results
print("Bucket 1: {} stones ({:.2f}%)".format(bucket1_count, (bucket1_count / total_stones) * 100))
print("Bucket 2: {} stones ({:.2f}%)".format(bucket2_count, (bucket2_count / total_stones) * 100))
print("Bucket 3: {} stones ({:.2f}%)".format(bucket3_count, (bucket3_count / total_stones) * 100))
