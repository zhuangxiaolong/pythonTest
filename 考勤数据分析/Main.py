from DataLoader import *
from DataCleanUp import *
from DataChange import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pylab as pl
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=12)
import datetime

def main():
    #数据加载
     objDataLoader=DataLoader(server="localhost", database="kqyc20180201", uid="sa", pwd="123")
     departmentData=objDataLoader.get_department()
     data=objDataLoader.get_data()
    #数据清理
     objDataCleanUp=DataCleanUp(departmentData,data)
     cleanUpData=objDataCleanUp.clean_data()
    #数据转换
     objDataChange=DataChange()
     lstCnames=objDataChange.get_change_data()
    #数据合并
     lstPlot=[]
     dataIndex=0
     for department in cleanUpData:
        lstX=[]
        lstY=[]
        for row in department:
            lstX.append(row[0])
            lstY.append(row[2])
        if len(department)!=0:
           tmp=department[0]
           color=lstCnames[dataIndex]
           dataIndex=dataIndex+1
           plot1 = pl.plot(lstX, lstY, linewidth=1.0, linestyle='-',color=color, label=tmp[1])# use pylab to plot x and y : Give your plots names
           
           lstPlot.append(plot1)
    #数据重塑
     pl.title("迟到次数统计",fontproperties=font)# give plot a title
     pl.xlabel("月份",fontproperties=font)# make axis labels
     pl.ylabel("数量",fontproperties=font)
     pl.grid(True)
     pl.ylim(0,50)
     #pl.legend(lstPlot, lstPlotName)# make legend
     pl.legend(loc='best',prop=font)
     pl.gcf().autofmt_xdate()  # 自动旋转日期标记
     pl.show()# show the plot on the screen

if __name__ == '__main__':
    main()