import matplotlib.pyplot as plt
from datetime import datetime

x = [4,5,6,7,8]

start_time = datetime(2025, 3, 26, 10, 36, 23)

times = [datetime(2025, 3, 26, 10, 38, 30), datetime(2025, 3, 26, 10, 37, 39), datetime(2025, 3, 26, 10, 40, 18), datetime(2025, 3, 26, 10, 59, 18), datetime(2025, 3, 26, 11, 32, 56)]

y = []

for time in times:
    y.append((time - start_time).total_seconds())


plt.scatter(x,y,color='blue',label='Time taken to crack password (seconds) vs. length of password')
plt.xlabel('Length of password')
plt.ylabel('Time taken to crack password (seconds)')
plt.title('Time taken to crack password (seconds) vs. length of password')

plt.show()
