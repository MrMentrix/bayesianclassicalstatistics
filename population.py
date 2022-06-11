import numpy as np
import matplotlib.pyplot as plt
import math
import random

plot_height = 25 # height of the plot
plot_width = 25 # width of the plot
groups = 5 # number of groups in the plot
size = 6 # dot size
colors = ["blue", "orange", "green", "red", "purple", "grey", "brown", "pink", "olive", "cyan"] # colors of the groups

# set up plot
plt.xticks(np.arange(0, plot_width+5, 5)) # make x axis go from 1 to pilots+cashiers
plt.yticks(np.arange(0, plot_height+5, 5)) # make y axis go from 1 to 10
plt.subplots_adjust(bottom=0.16) # adjust bottom margin

# generate random probabilites for groups which add up to 1
probabilities = []
for i in range(groups): # for each group
    probabilities.append(random.randint(1,100)) # generate a random probability
total = sum(probabilities)
probabilities = [round(i/total, 2) for i in probabilities] # normalize probabilities so they sum to 1
diff = 1 - sum(probabilities)
probabilities[0] += diff

people = []
for i in range(plot_height*plot_width): # randomly generating people sample
    people.append(np.random.choice(np.arange(0,groups), p=probabilities))

for i in range(groups): # sorting people into groups
    group_x = []
    group_y = []
    for j in range(len(people)):
        if people[j] == i: # if the person is in the group
            group_y.append(j%plot_height+1)
            group_x.append(math.floor(j/plot_height)+1)

    # plot group
    plt.plot(group_x, group_y, marker="o", markersize=size, linestyle="None", color=colors[i], label=f"Group {i+1}\n{round((people.count(i)/len(people))*100,1)}%")

# plot legend and show plot
plt.legend(loc='upper center', bbox_to_anchor=(0.5,-0.1), fancybox=True, shadow=True, ncol=5) # formatting legend
plt.show()