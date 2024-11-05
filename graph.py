# import matplotlib.pyplot as plt

# x1 = [1,2,3,4]
# y1 = [1,2,3,4]
# plt.plot(x1,y1)
# x2 = [1,2,3,4]
# y2 = [4,3,2,1]
# plt.plot(x2,y2)
# plt.xlabel('x-axis')
# plt.ylabel('y-axis')
# plt.title('my first graph')
# # plt.savefig("plot",dpi=300)
# plt.show()


# import numpy as np
# import matplotlib.pyplot as plt

# y1 = [1, 2, 3, 4]
# x1 = ['one', 'two', 'three', 'four']
# y2 = [1, 2, 3, 4]
# x = np.arange(len(y1))
# plt.bar(x - 0.2, y1, width=0.4, label='a')
# plt.bar(x + 0.2, y2, width=0.4, label='b')
# plt.xticks(x, x1)
# plt.legend()
# plt.show()

# import matplotlib.pyplot as plt
# ages = [2,5,70,40,30,45,50,45,43,40,44,60,7,13,57,18,90,77,32,21,20,40]
# range = (0,100,)
# bins = 10 
# plt.hist(ages, bins, range, edgecolor='silver')
# plt.xlabel('age')
# plt.ylabel('# of people')
# plt.title('My histogram')
# plt.show()

# import matplotlib.pyplot as plt


# activities = ['eat','sleep', 'work', 'play']
# slices = [3,7,8,6]
# colors = ['r','y','g','b']
# plt.pie(slices, labels=activities, colors= colors, autopct='%1.2f%%')
# plt.show()

import matplotlib.pyplot as plt
import numpy as np
x = [1,2,12,20,3,4,6,9]
y = [2,4,6,8,9,11,12,12]
plt.scatter(x,y)
plt.plot(x, y, linestyle=':', color='black', label='dots connecting dots')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('scatter plot')
plt.xticks(np.arange(min(x),max(x),1.0))
plt.show()

import matplotlib.pyplot as plt 
import numpy as np
from  mpl_toolkits import mplot3d 
plt.axes(projection="3d")

x=[1,2,3,4,5]

y=[3,5,2,1,4]

z=[5,2,1,4,3]

plt.plot(x,y,z)

plt.show()