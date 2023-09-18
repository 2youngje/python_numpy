# twinx
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10,10))

ax1 = fig.add_subplot()
ax2 = ax1.twinx()

ax1.set_xlim([0,100])

ax1.set_xlim([0,100])

ax1.set_ylim([0,100])
ax2.set_ylim([0,0.1])

fig.show()