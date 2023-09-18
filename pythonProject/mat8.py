
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10,10))

ax = fig.add_subplot()

ax.tick_parmas(labelsize=20,
               lenght=10,
               width=3,
               rotation=30)

fig.tight_layout()
fig.show()