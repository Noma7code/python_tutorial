names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Import pandas as pd
import pandas as pd

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict={ "country":names,
           "drives_right":dr,
          "cars_per_cap":cpc }

# Build a DataFrame cars from my_dict:
cars=pd.DataFrame(my_dict)
# Print cars
print(cars)

# Build cars DataFrame
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
cars_dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }
cars = pd.DataFrame(cars_dict)
print(cars)

# Definition of row_labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars
cars.index=row_labels

# Print cars again
print(cars)
#cars = pd.read_csv('cars.csv',index_col=0).read a csv
print(cars['country'])#do not access column like this
print(cars[['country']])#coulum access. use double square bracket to avoid printing the data type
print(cars[['country','cars_per_cap']])#accesing two columns
print(type(cars[['country']]))
print(cars[1:4])#acess rows  by slicing

print(cars.loc[['RU']])#acesing rows using the loc(label based)
print(cars.loc[['RU','EG'],['country','drives_right']])#specifying specific rows
print(cars.loc[:,['country','cars_per_cap']])#column acess

print(cars.iloc[:,[0,1]])#subsetting my index or postions use (iloc)
# Print out observations for Australia and Egypt
print(cars.iloc[[1,6]])

