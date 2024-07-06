z=6
if z%2==0:#condition for even numbers
    print("Z is:even")
else:
    print("z is odd")
sum=58.7
if sum%2==0: #checking multiple conditions
    print(sum,"is divisible by 2")
elif sum%3==0:
    print(sum,"is divisible by 3")
else :
    print( sum,"is neither divisible by two or 3")

# Define variables
room = "kit"
area = 14.0

# if statement for room
if room == "kit" :
    print("looking around in the kitchen.")

# if statement for area
if area>15:
    print("big place")


 #loop
age=45
while age>4:
    age=age/4
    print(age)

# Initialize offset
offset = -6

# Code the while loop
while offset != 0 :
    print("correcting...")
    if offset>0 :
       offset=offset-1
    else :
      offset=offset+1
    print(offset)

#for loop
fam=[2.65,1.56,2.98,3.00]
for height in fam:  #for each element in fam make a copy to height and execute the statement
    print(height)
    for index,height in enumerate(fam):#provide the index of the values
        print("index is :",index ,"and height is :",height)

#looping strings



# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for each_area in areas:
    print(each_area)

# house list of lists
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

# Build a for loop from scratch
for x in house:
    room_name = x[0]
    room_area = x[1]
    print("the", room_name, "is", room_area, "sqm")