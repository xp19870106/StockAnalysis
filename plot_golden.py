import time
import datetime
import numpy as np
import pandas as pd
import tushare as ts
from pylab import mpl
from scipy import stats
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.gridspec as gridspec

def plot_golden(input, historyLength):
    mpl.rcParams['font.sans-serif'] = ['FangSong']
    mpl.rcParams['axes.unicode_minus'] = False
    endTime = datetime.datetime.now()
    endTimeStr = endTime.strftime("%Y-%m-%d") 
    startTime = (endTime - datetime.timedelta(days = historyLength)) 
    startTimeStr = startTime.strftime("%Y-%m-%d")
    
    length = len(input.index)
    fig = plt.figure(figsize=(5,length*5))
    spec = gridspec.GridSpec(ncols=1, nrows=length, figure=fig)
    for index, row in input.iterrows():
        name = row['name']
        code = row['code']
        data = ts.get_hist_data(code, start=startTimeStr,end=endTimeStr)
        data = data.iloc[::-1]

        cs_max = data.close.max();
        cs_min = data.close.min();
        sp382 = (cs_max - cs_min) * 0.382 + cs_min;
        sp618 = (cs_max - cs_min) * 0.618 + cs_min;
        sp382_stats = stats.scoreatpercentile(data.close, 38.2)
        sp618_stats = stats.scoreatpercentile(data.close, 61.8)

        above618 = np.maximum(sp618, sp618_stats)
        below618 = np.minimum(sp618, sp618_stats)
        above382 = np.maximum(sp382, sp382_stats)
        below382 = np.minimum(sp382, sp382_stats)

        ax = fig.add_subplot(spec[index, 0])
        ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
        ax.plot(data.close);
        ax.axhline(below382, c='r')
        ax.axhline(above618, c='m')
        #ax.axhline(sp618, c='g')
        #ax.axhline(sp618_stats, c='k')
        #ax.fill_between(data.index, above618, below618, alpha=0.5, color='r')
        #ax.fill_between(data.index, above382, below382, alpha=0.5, color='g')
        ax.fill_between(data.index, above618, below382, alpha=0.5, color='r')
        
        ax.set_title(name,fontsize=16)
        ax.legend(['close', 'below382:{:.2f}'.format(below382), 'above618:{:.2f}'.format(above618)], loc='right',bbox_to_anchor=(1.5, 0.5))  
        
        
def plot_golden_for_option(input, historyLength):
    mpl.rcParams['font.sans-serif'] = ['FangSong']
    mpl.rcParams['axes.unicode_minus'] = False
    endTime = datetime.datetime.now()
    endTimeStr = endTime.strftime("%Y-%m-%d") 
    startTime = (endTime - datetime.timedelta(days = historyLength)) 
    startTimeStr = startTime.strftime("%Y-%m-%d")
    
    length = len(input.index)
    fig = plt.figure(figsize=(5,length*5))
    spec = gridspec.GridSpec(ncols=1, nrows=length, figure=fig)
    for index, row in input.iterrows():
        name = row['name']
        code = row['code']
        data = ts.get_hist_data(code, start=startTimeStr,end=endTimeStr)
        data = data.iloc[::-1]

        cs_max = data.close.max();
        cs_min = data.close.min();
        sp382 = (cs_max - cs_min) * 0.382 + cs_min;
        sp618 = (cs_max - cs_min) * 0.618 + cs_min;
        sp382_stats = stats.scoreatpercentile(data.close, 38.2)
        sp618_stats = stats.scoreatpercentile(data.close, 61.8)

        above618 = np.maximum(sp618, sp618_stats)
        below618 = np.minimum(sp618, sp618_stats)
        above382 = np.maximum(sp382, sp382_stats)
        below382 = np.minimum(sp382, sp382_stats)
        
        closeList = data.close.tolist()
        last = closeList[len(data.close)-1]
        if last <= below618:
            ax = fig.add_subplot(spec[index, 0])
            ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
            ax.plot(data.close);
            ax.axhline(below382, c='r')
            ax.axhline(above618, c='m')
            #ax.axhline(sp618, c='g')
            #ax.axhline(sp618_stats, c='k')
            #ax.fill_between(data.index, above618, below618, alpha=0.5, color='r')
            #ax.fill_between(data.index, above382, below382, alpha=0.5, color='g')
            ax.fill_between(data.index, above618, below382, alpha=0.5, color='r')
            
            ax.set_title(name,fontsize=16)
            ax.legend(['close', 'below382:{:.2f}'.format(below382), 'above618:{:.2f}'.format(above618)], loc='right',bbox_to_anchor=(1.5, 0.5))              
        

                