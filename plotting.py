import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0,3*np.pi,0.1)
# print(x)
# y=np.sin(x)
# print(y)
# plt.plot(x,y)
# plt.show()

y_sin=np.sin(x)
y_cos=np.cos(x)

# plt.plot(y_sin)
# plt.plot(y_cos)
# plt.xlabel("x_axis label")
# plt.ylabel("y_axis label")
# plt.title("Sine and Cosine")
# plt.legend(['sine','cosine'])
# plt.show()

# create the first subplot
plt.subplot(2,1,1)
plt.plot(x,y_sin)

#create second subplot
plt.subplot(2,1,2)
plt.plot(x,y_cos)

plt.xlabel("x_axis label")
plt.ylabel("y_axis label")
plt.title("Sine and Cosine")
plt.legend(['sine','cosine'])
plt.show()