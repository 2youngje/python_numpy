import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(14,7))

major_xticks = [i for i in range(0,101,20)]
minor_xticks = [i for i in range(0,101,5)]

ax.set_xticks(major_xticks)
ax.set_xticks(minor_xticks, minor=True)

ax.tick_params(axis='x',
               labelsize=20,
               length=10,
               width=3,
               rotation=30)

ax.tick_params(axis='x',
               which = 'minor',
               length=5,
               width=2)

fig.show()