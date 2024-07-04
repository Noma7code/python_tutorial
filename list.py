fam=['Joe',45 ,'Ama', 34,'kojo',32]
print(fam[3])#indexing
print(fam[-3])#negative indexing. For that it start counting from 1  backwards
print(fam[2:5])#slicing.start(inclusive) end(exclusive)
print(fam[:4])# auto start from 0
print(fam[5:])# start from 5 and end at the last value inclusive
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Print out second element from areas
print(areas[-9])

# Print out last element from areas
print(areas[-1])

# Print out the area of the living room
print(areas[5])

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Sum of kitchen and bedroom area: eat_sleep_area
eat_sleep_area=areas[3]+areas[7]

# Print the variable eat_sleep_area
print(eat_sleep_area)

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create downstairs
downstairs=areas[:6]

# Use slicing to create upstairs
upstairs=areas[6:]

# Print out downstairs and upstairs
print(downstairs)
print(upstairs)
x = [["a", "b", "c"],#works likes an array
     ["d", "e", "f"],
     ["g", "h", "i"]]
print(x[2][0])
print(x[2][:2])
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
print(areas[-1])
areas[0:4]=[" Verander",10.3," dinning room",43.5]#updating the elements of a list
print(areas)
areas[5:7]=19,35
areas[0]="estate"
print(areas)
fam=fam+["Henry",98]#addition of list
del(fam[2])#deleting an element
print(fam)

x=["a","b","c"]
y=x #stores the reference to the list not the actual values themselves
y[2]="z"
print(y)
y=list(x)#creates the same elements such that any manipuation in x will not affect y
y=x[:]
print(y)

areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]
#del(areas[10]);del(areas[10])#same command on a line cab be separated with ;
del(areas[-4:-2])#since after remving the bathroom the list indexes will be updated before another removal
print(areas)
#Change the second command, that creates the variable areas_copy, such that areas_copy is an explicit copy of areas.
#After your edit, changes made to areas_copy shouldn't affect areas. Submit the answer to check this.
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Create areas_copy
areas_copy =list(areas)#explicit copy
# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)
