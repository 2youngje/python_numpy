import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10,10))

ax1 = fig.add_subplot()
ax2 = ax1.twinx()

ax1.set_xlim([0,100])

ax1.set_ylim([0,100])
ax2.set_ylim([0,0.1])

ax1.set_title("Twinx graph", fontsize = 30)
ax1.set_ylabel("Data1", fontsize=20)
ax1.set_ylabel("Data2", fontsize=20)

ax1.tick_params(labelsize=20,
                lenght=20,
                width=3,
                bottom=False, labelbottom=False,
                left=False, labelleft=False,
                top = False, labeltop = False,
                right = True, labelright=True)

fig.tight_layout()
fig.show()