import matplotlib.pyplot as plt

from matplotlib.figure import Figure


def plot_tracks(data,track_id_col_name):

    # Make a plot of the data
    fig = Figure(figsize = (10,10), dpi=115)
    ax = fig.add_subplot()
    data.plot(ax=ax,column=track_id_col_name,alpha=0.5)
    
    return fig