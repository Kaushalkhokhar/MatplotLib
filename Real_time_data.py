import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x_vals = []
y_vals = []

index = count()

def animate(i):
    data = pd.read_csv('data/real_time_data.csv')
    x = data['x_value']
    y1 = data['total_1']
    y2 = data['total_2']
    
    plt.cla() # Needed to clear a old line 

    plt.plot(x, y1, label='channel_1')
    plt.plot(x, y2, label='channel_2')

    plt.legend(loc='upper left') # to aff legend in every plot

    plt.tight_layout()
    
# gcf = get current figure
ani = FuncAnimation(plt.gcf(), 
                    animate, interval=1000) # interval is time interval to run fucntion. 1000 is equal to one second


plt.show()

