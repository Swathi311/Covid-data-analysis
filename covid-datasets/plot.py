import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt


#1
def graph1():
   
    data = pd.read_csv('case_time_series.csv')

    Y = data.iloc[61:,1].values
    R = data.iloc[61:,3].values
    D = data.iloc[61:,5].values
    X = data.iloc[61:,0]

    plt.plot(X,Y)


#2
def graph2():
   
    data = pd.read_csv('case_time_series.csv')

    Y = data.iloc[61:,1].values
    R = data.iloc[61:,3].values
    D = data.iloc[61:,5].values
    X = data.iloc[61:,0]

    plt.figure(figsize=(25,8))

    ax = plt.axes()
    ax.grid(linewidth=0.4, color='#8f8f8f')

    ax.set_facecolor("black")
    ax.set_xlabel('\nDate',size=25,color='#4bb4f2')
    ax.set_ylabel('Number of Confirmed Cases\n',
    size=25,color='#4bb4f2')

    ax.plot(X,Y,
    color='#1F77B4',
    marker='o',
    linewidth=4,
    markersize=15,
    markeredgecolor='#035E9B')



#3
def graph3():
   
    data = pd.read_csv('case_time_series.csv')

    Y = data.iloc[61:,1].values
    R = data.iloc[61:,3].values
    D = data.iloc[61:,5].values
    X = data.iloc[61:,0]

    plt.figure(figsize=(25,8))

    ax = plt.axes()
    ax.grid(linewidth=0.4, color='#8f8f8f')

    ax.set_facecolor("black")
    ax.set_xlabel('\nDate',size=25,color='#4bb4f2')
    ax.set_ylabel('Number of Confirmed Cases\n',
    size=25,color='#4bb4f2')

    plt.xticks(rotation='vertical',size='20',color='white')
    plt.yticks(size=20,color='white')
    plt.tick_params(size=20,color='white')

    for i,j in zip(X,Y):
        ax.annotate(str(j),xy=(i,j+100),color='white',size='13')
   
    ax.annotate('Second Lockdown 15th April',
    xy=(15.2, 860),
    xytext=(19.9,500),
    color='white',
    size='25',
    arrowprops=dict(color='white',
    linewidth=0.025))

    plt.title("COVID-19 IN : Daily Confirmed\n",
    size=50,color='#28a9ff')

    ax.plot(X,Y,
    color='#1F77B4',
    marker='o',
    linewidth=4,
    markersize=15,
    markeredgecolor='#035E9B')


    slices = [62, 142, 195]
    activities = ['Travel', 'Place Visit', 'Unknown']

    cols=['#4C8BE2','#00e061','#fe073a']
    exp = [0.2,0.02,0.02]

    plt.pie(slices,labels=activities,
    textprops=dict(size=25,color='black'),
    radius=3,
    colors=cols,
    autopct='%2.2f%%',
    explode=exp,
    shadow=True,
    startangle=90)

    plt.title('Transmission\n\n\n\n',color='#4fb4f2',size=40)


#4
def graph4():
   
    data = pd.read_csv('district.csv')
    data.head()

    re=data.iloc[:30,5].values
    de=data.iloc[:30,4].values
    co=data.iloc[:30,3].values
    x=list(data.iloc[:30,0])

    plt.figure(figsize=(25,10))
    ax=plt.axes()

    ax.set_facecolor('black')
    ax.grid(linewidth=0.4, color='#8f8f8f')


    plt.xticks(rotation='vertical',
    size='20',
    color='white')#ticks of X

    plt.yticks(size='20',color='white')


    ax.set_xlabel('\nDistrict',size=25,
    color='#4bb4f2')
    ax.set_ylabel('No. of cases\n',size=25,
    color='#4bb4f2')


    plt.tick_params(size=20,color='white')


    ax.set_title('Maharashtra District wise breakdown\n',
    size=50,color='#28a9ff')

    plt.bar(x,co,label='re')
    plt.bar(x,re,label='re',color='green')
    plt.bar(x,de,label='re',color='red')

    for i,j in zip(x,co):
        annotate(str(int(j)),
    xy=(i,j+3),
    color='white',
    size='15')

    plt.legend(['Confirmed','Recovered','Deceased'],
    fontsize=20)


if __name__=='__main__':
   
    window = tk.Tk()
   
    window.title(" COVID ANALYSIS ")
    window.geometry('300x300')
    label = tk.Label(window, text = " GRAPH 1 ")
    label.grid(row = 20, column = 5)
    '''e = tk.Entry(window)
    e.grid(row = 20, column = 6)'''
    tk.Button(window, text = "view", command = graph1).grid(row = 20, column = 7)
   
   
    label = tk.Label(window, text = " GRAPH 2 ")
    label.grid(row = 30, column = 5)
    ''' e = tk.Entry(window)
    e.grid(row = 30, column = 6)'''
    tk.Button(window, text = "view", command = graph2).grid(row = 30, column = 7)
   
   
    label = tk.Label(window, text = " GRAPH 3 ")
    label.grid(row = 40, column = 5)
    ''' e = tk.Entry(window)
    e.grid(row = 40, column = 6)'''
    tk.Button(window, text = "view", command = graph3).grid(row = 40, column = 7)
   
   
   
    label = tk.Label(window, text = " GRAPH 4 ")
    label.grid(row = 50, column = 5)
    '''e = tk.Entry(window)
    e.grid(row = 50, column = 6)'''
    tk.Button(window, text = "view", command = graph4).grid(row = 50, column = 7)
   
   
    window.mainloop()