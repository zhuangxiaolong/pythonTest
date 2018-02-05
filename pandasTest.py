from SqlServerHelper import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pylab as pl
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=12)

#取数据
objSqlServerHelper=SqlServerHelper(server="localhost",database="gz_kqyc_2017-12-04", uid="sa", pwd="123")

lst=objSqlServerHelper.execute4lst("SELECT  mon ,COUNT(*) AS num FROM    ( SELECT    CONVERT(CHAR(7), dDate, 120) AS mon , * FROM      yCheckWorkData ) AS tmp WHERE     mon BETWEEN '2017-01' and '2017-12' GROUP BY mon ORDER BY mon ")
#print(lst)


lstX=[]
lstY=[]
for row in lst:
   lstX.append(row[0])
   lstY.append(row[1])

#print(lstX)
#print(lstY)

plot1 = pl.plot(lstX, lstY, 'r')# use pylab to plot x and y : Give your plots names
plot2 = pl.plot(lstX, lstY, 'go')

pl.title("打卡趋势",fontproperties=font)# give plot a title
pl.xlabel("月份",fontproperties=font)# make axis labels
pl.ylabel("数量",fontproperties=font)


pl.legend([plot1, plot2], ('red line','green circles'))# make legend

#pl.plot(lstX, lstY)# use pylab to plot x and y
pl.show()# show the plot on the screen



