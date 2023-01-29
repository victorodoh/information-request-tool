from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from tkinter import *
import squarify
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def draw_plot_canvas(figure, title_of_plot):
    pop_out_window = Toplevel()
    pop_out_window.geometry("+%d+%d" % (250, 10))
    pop_out_window.title(title_of_plot)

    Canvas = FigureCanvasTkAgg(figure, master=pop_out_window)
    Canvas.draw()
    Canvas.get_tk_widget().pack(side=TOP, fill=BOTH)

    # matplotlib toolbar
    tool_bar = NavigationToolbar2Tk(Canvas, pop_out_window)
    tool_bar.update()
    tool_bar.pack(side=TOP, fill=X)
    
    # adding the toolbar to the tk window
    Canvas.get_tk_widget().pack(side=TOP, fill=BOTH) 
    
    
def bar_chart_(title, df, values, label ):

    fig, ax = plt.subplots(figsize=(15,10), facecolor='white', dpi= 100)
    ax.vlines(x=df.index, ymin=0, ymax=values, color='green', alpha=1.0, linewidth=23)

    # Annotate Text
    for i, cty in enumerate(values):
        ax.text(i, cty+0.5, round(cty, 0), horizontalalignment='center')

    # Title, Label, Ticks and Ylim
    ax.set_title(title, fontdict={'size':16})
    ax.set(ylabel='Cases count')
    plt.xticks(df.index, label.str.upper(), rotation=15, horizontalalignment='right', fontsize=6)

    draw_plot_canvas(fig, title)
    
def scattered_plot(title, x, y, colors):
    plt.scatter(x, y, c=colors)
    plt.title(title, fontsize=12)
    plt.rcParams["figure.figsize"] = (20,3)
    plt.show()
    
def donut_chart(title, values, labels, colors, explode):
    plt.close()
    plt.pie(values, colors=colors, labels=labels, autopct='%1.1f%%', pctdistance=0.85, explode=explode)
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    
    draw_plot_canvas(fig, title)
    
def horizontal_lollipop_chart(x, y, label, maximum, graph_title, data):
    plt.close()
    fig, ax = plt.subplots(figsize=(16,16), dpi= 80)
    ax.vlines(x=x, ymin=0, ymax=y, color='firebrick', alpha=0.7, linewidth=2)
    ax.scatter(x=x, y=y, s=75, color='firebrick', alpha=0.7)
    ax.set_title(graph_title, fontdict={'size':16})
    ax.set_ylabel("Cases")
    ax.set_xticks(x)
    ax.set_xticklabels(label.str.upper(), rotation=60, fontdict={'horizontalalignment': 'right', 'size':12})
    ax.set_ylim(0, int(maximum) + 20)
    
    # Annotate
    for row in data.itertuples():
        ax.text(row.Index, row.involved_person+3.5, s=round(row.involved_person, 2), horizontalalignment= 'center', verticalalignment='bottom', fontsize=9)

    draw_plot_canvas(fig, graph_title)
    
    
def area_graph(chart_title, title_one, title_two, data_frame, x, y, ax0_legend, plot_one_label, plot_two_label, y_Label, legends):
    fig, (ax0, ax1) = plt.subplots(nrows=2, figsize=(10, 10), sharex=True)
      
    fig.suptitle(chart_title)
    
    ax0.set(title=title_one)
    ax1.set(title=title_two)

    data_frame.plot.area( x=x, y=y, stacked=False, ax=ax0)
    ax0.set(ylabel="Cases")
    ax0.legend([ax0_legend])

    data_frame[[x, plot_one_label , plot_two_label]].plot.area(x=x, stacked=False, ax=ax1)
    
    ax1.set(ylabel=y_Label)
    handles, labels = ax1.get_legend_handles_labels()
    ax1.legend(handles, legends)
        
    draw_plot_canvas(fig, chart_title)

def pie_chart(title, data, labels):
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.pie(data, labels=labels, autopct='%.1f%%',
        wedgeprops={'linewidth': 3.0, 'edgecolor': 'white'},
        textprops={'size': 'x-large'})
    ax.set_title(title, fontsize=14)

    draw_plot_canvas(fig, title)

def Lollipop(title, df_first, df_second, label_one, label_two, xlabel, ylabel, yticks):
    plt.close()
    my_range=range(1,4)
    # The horizontal plot is made using the hline function
    plt.hlines(y=my_range, xmin=df_first, xmax=df_second, color='grey', alpha=0.4)
    plt.scatter(df_first, my_range, color='skyblue', alpha=1, label=label_one)
    plt.scatter(df_second, my_range, color='green', alpha=0.4 , label=label_two)
    plt.legend()
    
    # Add title and axis names
    plt.yticks(my_range, yticks)
    plt.title(title, loc='left')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    # Show the graph
    plt.show()
    
def tree_map(chart_title, data_size, labels ):
    
    plt.close()
    colors=['#247BA0','#FFADAD','#f9dc5c','#FFD60A','#F3D5B5','#ef233c','#b7094c', '#c7294c', '#A5BE00', '#28094d', '#FEC5BB'] #color palette
    fig = plt.gcf()
    fig.set_size_inches(12, 7.5)
    sns.set_style(style="whitegrid") # set seaborn plot style
    sizes= data_size
    label= labels
    squarify.plot(sizes=sizes, label=label, alpha=0.6,color=colors).set(title=chart_title)
    plt.title(chart_title, fontsize=14, fontweight="bold")
    plt.axis('off')
    draw_plot_canvas(fig, chart_title)
