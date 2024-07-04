import numpy as np
height=([1.34,1.67,1.50,1.43])
np_height=np.array(height)
print(np_height)

weight=([45.5,67.0,54.3,32.6])
np_weight=np.array(weight)
print(np_weight)
bmi=np_weight/np_height**2#finding the bmi elementwise operation
print(bmi)
print(np.array([1.0,"is",True]))#numpy array only take one data type. it does type coersion on diff data types
print(np_height+np_weight) # array addition perform summation not concatenation as in list
print(bmi[1])#indexing
print(bmi>23)#or by using bolean values for indexing
print(bmi[bmi>23])

# Import the numpy package as np
import numpy as np

# Create list baseball
baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Create a numpy array from baseball: np_baseball
np_baseball=np.array(baseball)

# Print out type of np_baseball
print(type(np_baseball))
print(np.array([True, 1, 2]) + np.array([3, 4, False]))

np_2d=np.array([[1.34,2.56,2.54,1.32,1.56],
               [51.43,25.54,71.76,42.54,32.54]])
print(np_2d)
print(np_2d.shape)#determing the number of rows and columns
print(np_2d[0])
print(np_2d[0][2]) #selecting the first row and indexing the third element
print(np_2d[0,2])
print(np_2d[:,1:3])#finding the height and weight of the second and third member. : selecting all the rows
print(np_2d[1,:])#selecting all weight

# Import numpy
import numpy as np

# Create baseball, a list of lists
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Create a 2D numpy array from baseball: np_baseball
np_baseball=np.array(baseball)

# Print out the type of np_baseball
print(type(np_baseball))

# Print out the shape of np_baseball
print(np_baseball.shape)

np_mean=np.mean(np_baseball[:,0])
print(np_mean)#statistics in numpy
print(np.median(np_baseball[:,1]))

# Print mean height (first column)
avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))

# Print median height. Replace 'None'
med = np.median(np_baseball[:,0])
print("Median: " + str(med))

# Print out the standard deviation on height. Replace 'None'
stddev = np.std(np_baseball[:,0])
print("Standard Deviation: " + str(stddev))

# Print out correlation between first and second column. Replace 'None'
corr = np.corrcoef(np_baseball[:,0],np_baseball[:,1])
print("Correlation: " + str(corr))

positions=['GK','MD','ST']
heights=[1.54,2.56,7.84]



# Convert positions and heights to numpy arrays: np_positions, np_heights
np_positions=np.array(positions)
np_heights=np.array(heights)


# Heights of the goalkeepers: gk_heights
gk_heights=np_heights[np_positions=='GK']

# Heights of the other players: other_heights
other_heights=np_heights[np_positions!='GK']

# Print out the median height of goalkeepers. Replace 'None'
print("Median height of goalkeepers: " + str(np.median(gk_heights)))

# Print out the median height of other players. Replace 'None'
print("Median height of other players: " + str(np.median(other_heights)))

x=[1,2,3]
y=[-1,0.1,1.1]+x[0:2]
print(y)
print(len(y))
print(sorted(y))

x1=['e','a','b']
y1=x[1:]
y1[0]='g'
print(x1)
nd=np.array([[2,3],[4,5]])
print(nd*np.array([2,0]))

m=[15,10,2,84]+[1,4,8,7,9]
print(m.index(m.count(m[0])))




