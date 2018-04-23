from scipy import stats
import numpy as np
from matplotlib import pyplot as plt

x = np.array([112, 255, 564, 889, 778, 283])  # house in square meters || training data
y = np.array([1152, 2256, 1236, 9876, 7536, 9856])  # price of the house || training data

slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

plt.plot(x, y, 'ro', color='black')

plt.ylabel('Price')
plt.xlabel('Size of House')

plt.axis([0, 900, 0, 10000])

plt.plot(x, x*slope+intercept, 'b')

# plt.plot()
# plt.show()
#Prediction
# y=a*x+b

newX = 552
newY = newX*slope+intercept

print(newY)