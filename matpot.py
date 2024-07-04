import matplotlib.pyplot as plt #mother of all visulisation packages in python
year=[1950,1970,1990,2010]
popu=[2.519,3.692,5.263,6.972]
plt.plot(year ,popu)#plot(line) fun tells python what to plot and how to plot it. horizontal  axis, vertical
plt.scatter(year,popu)#displays into a scatter format
plt.show()#show displays the plot
#Put the x-axis on a logarithmic scale.plt.xscale('log')

values=[0.23,0.86,7.84,7.93,67.89,34,67,89,90,34,67.45,81]
plt.hist(values,bins=3)
plt.show()## Show and clear plot plt.clf()

year=[1950,1970,1990,2010]
popu=[2.519,3.692,5.263,6.972]
plt.plot(year,popu)
plt.scatter(year,popu)
plt.xlabel('year')
plt.ylabel('population')#customization
plt.title('World Population Projection')#adds title using the title function
plt.yticks([0,2,4,6,8,10],
           ['0','2B','4B','6B','8B','10B'])#changing the scale of the y axis and assining a value representaion.
#that is this shows that the interval on the y axis is 2  with with every scale representing a billion(B)
year=[1880,1873,1995,2000]+year
popu=[1.546,4.567,2.567,3.890]+popu#adding more data
plt.plot(year,popu)
plt.grid(True)#add grid to the plot
plt.show()


