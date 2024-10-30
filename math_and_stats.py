import random
import math
import statistics

vals_1_100 = range(1, 100)
vals_sample = random.sample(vals_1_100, 75)
vals_choices = random.choices(vals_1_100, k=200)  
radius = random.randint(3, 10)
pi = math.pi
sample_sum = sum(vals_sample)
sample_avg = statistics.mean(vals_sample)
sample_median = statistics.median(vals_sample)

print("_Experimenting with a subset of integers 1-100:")
print(f"Sum of 75 sample values from 1 to 100: {sample_sum}")
print(f"Average of 75 sample values: {sample_avg}")
print(f"Median of 75 sample values: {sample_median}")
print('\n')
area = pi * (radius ** 2)
area_rounded_up = math.ceil(area)
area_rounded_down = math.floor(area)

print("_Modeling a random circle:")
print(f"Radius = {radius}, area = {area_rounded_up}")
print(f"Radius = {radius}, area = {area_rounded_down}")