import random
import matplotlib.pyplot as plt
import numpy as np

x = [] # coin array
p = [] # probability array
head_prob = 50 # probability for coin showing heads
tosses = 1000 # amount of tosses

# 0 = Tails
# 1 = Heads

for i in range(tosses): # repeat 'tosses' times
    if random.randrange(0,100) < head_prob: # random number generator to determine 'heads' or 'tails'
        x.append(1) # add 'heads' to coin array
    else:
        x.append(0) # add 'tails' to coin array
    prob = round((x.count(1)+1)/(len(x)+2), 3) # calculate probability using binomial distribution
    p.append(prob) # adding probability to probability array

plt.plot(x, marker="o", linestyle="None", label="0 = Tails / 1 = Heads") # create coin toss dots
plt.plot(p, color="red", label="Binomial") # create binomial probability line
plt.plot(np.array([(head_prob/100) for i in range(tosses)]), linestyle="dotted", color="green", label="True Probability") # add dotted line of true probability

plt.legend(loc='upper center', bbox_to_anchor=(0.5,-0.1), fancybox=True, shadow=True, ncol=5) # formatting legend
plt.title(f"{head_prob}% prob. for heads, {tosses} tosses") # setting plot title
plt.xlabel("Coin Tosses") # setting x-axis label
plt.ylabel("Heads/Tails\nHead Probability") # setting y-axis label
plt.show() # showing final plot