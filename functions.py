fam=[16,45 ,56.4, 34,0.876,32]
tallest=max(fam)
print(tallest)#reusable code for finding the maximum with writing the max code from scratch
print(round(fam[-2],1))#round func takes 2 important , the number itself and the num of preffered dp
#if you dont specify that is it can take one input. it will return the nearest integer
print(round(fam[2]))
#help(round)  #open up a documentation on a function

var1=[1,2,3,4]
var2=True

print(type(var1))#print the type of var1
print(len(var1))#print the lenght of var1
#In IPython specifically, you can also use ? before the function name.
#To get help on a function, for example, help(max) or ?functioname

# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full=first+second
print(full)
# Sort full in descending order: full_sorted
full_sorted=sorted(full,reverse=True)

# Print out full_sorted
print(full_sorted)#the data types are called objects
fam1=["dad","mum","sister","bro","aunt"]
print(fam1.index("bro"))#applying method index to an element
print(first.count(11.25))
sister="lia"
print(sister.capitalize())
print(sister.replace("a", "nata"))#replace method to strings

# string to experiment with: place
place = "poolhouse"

# Use upper() on place: place_up
place_up=place.upper()

# Print out place and place_up
print(place)
print(place_up)

# Print out the number of o's in place
print(place.count("o"))

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0
print(areas.index(20.0))

# Print out how often 9.50 appears in areas
print(areas.count(9.50))

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size
areas.append(24.5)
areas.append(15.45)


# Print out areas
print(areas)

# Reverse the orders of the elements in areas
areas.reverse()

# Print out areas
print(areas)






