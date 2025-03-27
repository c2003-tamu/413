import random
import string

for i in range(4, 9):
    random_str = ''.join(random.choices('0123456789', k=i))
    print(random_str)
