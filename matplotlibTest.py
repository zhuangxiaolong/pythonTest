#coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from SqlServerHelper import *
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=12)

plt.figure(figsize=(8, 5), dpi=80)
axes = plt.subplot(111)

#取数据
objSqlServerHelper=SqlServerHelper(server="localhost",database="gz_kqyc_2017-12-04", uid="sa", pwd="123")

#卷接包车间
lst1=objSqlServerHelper.execute4lst("SELECT TOP 1000 d.sDepart_n,Convert(varchar(5),y.dDate,108) FROM dbo.yCheckWorkData y,dbo.jEmployee j,dbo.jDepart d WHERE y.sEmpl_c=j.sEmpl_c AND d.sDepart_c=j.sDepart_c and d.sDepart_n='卷接包车间'")
type1_x = []
type1_y = []
for obj in lst1:
    type1_x.append(obj[1])
    type1_y.append(10)
type1 = axes.scatter(type1_x, type1_y, s=20,label="卷接包车间",color='blue')

#制丝车间    
lst2=objSqlServerHelper.execute4lst("SELECT TOP 1000 d.sDepart_n,Convert(varchar(5),y.dDate,108) FROM dbo.yCheckWorkData y,dbo.jEmployee j,dbo.jDepart d WHERE y.sEmpl_c=j.sEmpl_c AND d.sDepart_c=j.sDepart_c and d.sDepart_n='制丝车间'")
type2_x = []
type2_y = []
for obj in lst2:
    type2_x.append(obj[1])
    type2_y.append(20)
type2 = axes.scatter(type2_x, type2_y, s=40,label="制丝车间",color='red')

#动力车间    
lst3=objSqlServerHelper.execute4lst("SELECT TOP 1000 d.sDepart_n,Convert(varchar(5),y.dDate,108) FROM dbo.yCheckWorkData y,dbo.jEmployee j,dbo.jDepart d WHERE y.sEmpl_c=j.sEmpl_c AND d.sDepart_c=j.sDepart_c and d.sDepart_n='动力车间'")
type3_x = []
type3_y = []
for obj in lst3:
    type3_x.append(obj[1])
    type3_y.append(30)
type3 = axes.scatter(type3_x, type3_y, s=60,label="动力车间",color='green')


#plt.xlabel(u'部门',fontproperties=font)
plt.ylabel(u'时间',fontproperties=font)
plt.title(u"上班时间散点图",fontproperties=font)
# 设置坐标轴范围
plt.ylim((0, 24))
plt.xlim((0, 24))

axes.legend((type1, type2, type3), (u'卷接包车间', u'制丝车间', u'动力车间'), loc=2, prop=font)


plt.show()