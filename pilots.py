import matplotlib.pyplot as plt
import numpy as np
import math

plot_height = 10
size = 15 # dot size
show_ratio = False
pilots = 10 # total amount of pilots
cashiers = 100 # total amount of cashiers
pilot_ratio = 0.9 # amount of pilots fitting the description
cashier_ratio = 0.4 # amount of cashiers fitting the description

if plot_height <= 0:
    print("Please enter a plot height that is greater than 0.")
    quit()

if pilots%plot_height!=0 or cashiers%plot_height!=0: # check if people can be evenly distributed
    print("Please enter a number of pilots and cashiers that is a multiple of the plot height.")
    quit()

if cashier_ratio > 1 or pilot_ratio > 1 or cashier_ratio < 0 or pilot_ratio < 0: # check if ratios are within the correct range
    print("Please enter a ratio between 0 and 1.")
    quit()
    
# show pilots and cashiers as dots in graph
pilots_x = [] # creating arrays
pilots_y = []
cashiers_x = []
cashiers_y = []
for i in range(pilots+cashiers): # creating general plot
    if i < pilots:
        pilots_x.append(math.floor(i/plot_height)+1)
        pilots_y.append(i%plot_height+1)
    else:
        cashiers_x.append(math.floor(i/plot_height)+1)
        cashiers_y.append(i%plot_height+1)

# plot settings
plt.xticks(np.arange(1, (pilots+cashiers)/plot_height+1, 5)) # make x axis go from 1 to pilots+cashiers
plt.yticks(np.arange(1, plot_height, 2)) # make y axis go from 1 to 10
plt.subplots_adjust(bottom=0.16) # adjust bottom margin

# plotting pilots and cashiers
plt.plot(pilots_x, pilots_y, marker="o", markersize=size, linestyle="None", color="blue", label="All Pilots")
plt.plot(cashiers_x, cashiers_y, marker="o", markersize=size, linestyle="None", color="red", label="All Cashiers")

if show_ratio:
    # Showing pilot and cashier ratio
    pilots_ratio_x = [] # creating arrays
    pilots_ratio_y = []
    cashiers_ratio_x = []
    cashiers_ratio_y = []
    for i in range(math.floor(pilots*pilot_ratio)): # creating pilot ratio
        pilots_ratio_x.append(i%(pilots/plot_height)+1)
        pilots_ratio_y.append(math.floor(i/(pilots/plot_height))+1)
    for i in range(math.floor(cashiers*cashier_ratio)): #creating cashier ratio
        cashiers_ratio_x.append(i%(cashiers/plot_height)+1+(pilots/plot_height))
        cashiers_ratio_y.append(math.floor(i/(cashiers/plot_height))+1)

    # plotting pilot and cashier ratios
    plt.plot(pilots_ratio_x, pilots_ratio_y, marker="o", markersize=size*0.7, linestyle="None", color="green", label="Pilots Ratio")
    plt.plot(cashiers_ratio_x, cashiers_ratio_y, marker="o", markersize=size*0.7, linestyle="None", color="yellow", label="Cashiers Ratio")

if show_ratio:
    plt.title(f"Pilots: {pilots} / Cashiers: {cashiers} / Pilot Ratio: {pilot_ratio} / Cashier Ratio: {cashier_ratio}")
else:
    plt.title(f"Pilots: {pilots} / Cashiers: {cashiers}")
plt.legend(loc='upper center', bbox_to_anchor=(0.5,-0.1), fancybox=True, shadow=True, ncol=5) # formatting legend
plt.show()