import matplotlib.pyplot as plt
import numpy as np

# create bar plot
probabilities = [0.312, 0.091, 0.181, 0.139, 0.277]
colors = ["blue", "orange", "green", "red", "purple", "grey", "brown", "pink", "olive", "cyan"] # colors of the groups

# plot each probability as a bar
for i in range(len(probabilities)):
    plt.bar(i, round(probabilities[i]*100,1), color=colors[i], label=f"Group {i+1}")

# y label 'percentage' with 5%-steps
plt.ylabel('percentage')
plt.yticks(np.arange(0, max(probabilities), 5))

# plot legend and show plot
plt.title("Population distribution")
plt.legend(loc='upper center', bbox_to_anchor=(0.5,0), fancybox=True, shadow=True, ncol=5)
plt.show()