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
    mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
    mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
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
        ax.axhline(sp382, c='r')
        ax.axhline(sp382_stats, c='m')
        ax.axhline(sp618, c='g')
        ax.axhline(sp618_stats, c='k')
        ax.fill_between(data.index, above618, below618, alpha=0.5, color='r')
        ax.fill_between(data.index, above382, below382, alpha=0.5, color='g')
        
        ax.set_title(name,fontsize=16)
        ax.legend(['close', 'sp382:{:.2f}'.format(sp382), 'sp382_stats:{:.2f}'.format(sp382_stats), 'sp618:{:.2f}'.format(sp618), 'sp618_stats:{:.2f}'.format(sp618_stats)], loc='right',bbox_to_anchor=(1.5, 0.5))  
        
        
def plot_golden_for_option(input, historyLength):
    mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
    mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
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
            ax.axhline(sp382, c='r')
            ax.axhline(sp382_stats, c='m')
            ax.axhline(sp618, c='g')
            ax.axhline(sp618_stats, c='k')
            ax.fill_between(data.index, above618, below618, alpha=0.5, color='r')
            ax.fill_between(data.index, above382, below382, alpha=0.5, color='g')
            
            ax.set_title(name,fontsize=16)
            ax.legend(['close', 'sp382:{:.2f}'.format(sp382), 'sp382_stats:{:.2f}'.format(sp382_stats), 'sp618:{:.2f}'.format(sp618), 'sp618_stats:{:.2f}'.format(sp618_stats)], loc='right',bbox_to_anchor=(1.5, 0.5))              
        

                