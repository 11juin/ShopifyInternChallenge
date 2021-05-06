import pandas as pd  
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.patches import ConnectionPatch
from matplotlib.gridspec import GridSpec

def export_report(data):
    # The wrong aov value $3145.13 is calcuated by 'data["order_amount"].mean()', despite from situations when one order contains mutiple items 
    aov = data["order_amount"].sum()/data["total_items"].sum()
    gs = GridSpec(nrows=2, ncols=2)
    data1 = data.groupby("payment_method")["total_items"].sum()
    pie = plt.figure(figsize=[10,5])
    ax = pie.add_subplot(gs[0, 0])
    labels = data1.keys()
    plt.pie(x=data1, autopct="%.1f%%", explode=[0.05]*3, labels=labels, pctdistance=0.3)
    plt.title("Percentage of # of Items sold by payment type", fontsize=14)
    data2 = data.groupby("shop_id")["total_items"].sum().sort_values(ascending = False) 
    data2 = data2[:1].append(pd.Series(sum(data2[1:].values), index =['others']))
    ax1 = pie.add_subplot(gs[0, 1])
    labels1 = ['Store '+ str(np.array(data2[:1].index)[0]),'Others']
    myexplode = [0.1, 0.1]
    plt.pie(x=data2, autopct="%.1f%%", explode=myexplode, labels=labels1, pctdistance=0.3)
    plt.title("Percentage of # of Items Sold by Top 1 Store", fontsize=14)
    data3 = data.groupby("shop_id")["order_amount"].sum().sort_values(ascending = False) 
    data3 = data3[1:3].append(pd.Series(sum(data3[3:].values), index =['others']))
    ax2 = pie.add_subplot(gs[1, 0])
    labels2 = ['Store '+ str(np.array(data3[:1].index)[0]), 'Store '+ str(np.array(data3[1:2].index)[0]), 'Others']
    myexplode = [0.1, 0.1, 0.1]
    plt.pie(x=data3, autopct="%.1f%%", explode=myexplode, labels=labels2, pctdistance=0.3)
    plt.title("Percentage of Order Amount by Top 2 Stores", fontsize=14)
    plt.tight_layout()
    text  = 'The wrong value $3145.13 is calcuated by data["order_amount"].mean(), ignored situations when one order contains mutiple items,corrected value should be ' + str(aov)
    ax3 = pie.add_subplot(gs[1, 1])
    plt.axis([0, 10, 0, 10])
    plt.text(0, 5, text, fontsize=10, va='center',wrap=True, color='green',bbox=dict(facecolor='none', edgecolor='blue', pad=10.0))
    plt.show()

if __name__ == "__main__":
    path = '../../Downloads/Shopify.csv'
    data = pd.read_csv(path)
    export_report(data)