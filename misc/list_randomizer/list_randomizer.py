import random

number_list = list(range(1, 13))
print("Original list: " + str(number_list))

random.shuffle(number_list)
print("Shuffled list: " + str(number_list))

