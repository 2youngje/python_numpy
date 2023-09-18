import matplotlib.pyplot as plt

#피규어 사이즈를 정한다.
figsize= (7,7)

#피규어와 x축에의 사이즈를 figsize와 함께 정한다.
fig, ax = plt.subplots(figsize=figsize)

#x축에 대한 범위를 설정
ax.set_xlim([-1,1])
#y축에 대한 범위를 설정
ax.set_ylim([-1,1])

ax.grid()
ax.tick_params(axis='both',
               labelsize=15)

ax.text(x=0,y=0,s="Hello",fontsize=30)

ax.text(x=0.5,y=0,s="Hello2",fontsize=30)

ax.text(x=0.5,y=-0.5,s="Hello3",fontsize=30)

fig.show()