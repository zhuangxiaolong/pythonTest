from SqlServerHelper import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pylab as pl
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=12)

class DataLoader:
    def __init__(self,server="localhost", database="SampleDB", uid="sa", pwd="123"):  
        ''''' initialization '''  
        self.server = server  
        self.database = database  
        self.uid = uid  
        self.pwd = pwd
    def get_department(self):
     #取数据
     objSqlServerHelper = SqlServerHelper(
         server=self.server, database=self.database, uid=self.uid, pwd=self.pwd)
     
     sql = "SELECT  "
     sql += "        sDepart_n "
     sql += " FROM   "
     sql += "                     dbo.jDepart d "
     lst = objSqlServerHelper.execute4lst(sql)
     return lst 
    def get_data(self):
     #取数据
     objSqlServerHelper = SqlServerHelper(
         server=self.server, database=self.database, uid=self.uid, pwd=self.pwd)
     
     sql = "SELECT  mon ,"
     sql += "        sDepart_n ,"
     sql += "         SUM(ncd) AS num"
     sql += " FROM    ( SELECT    d.sDepart_n ,"
     sql += "                    CONVERT(char(7),CAST( Convert(char(6),cw.sMonth)+'01' AS DATE),120) AS mon ,"
     sql += "                     nCD"
     sql += "           FROM      yRptCheckWorkTotalFast cw ,"
     sql += "                     dbo.jDepart d ,"
     sql += "                     dbo.jEmployee e"
     sql += "           WHERE     cw.sEmpl_c = e.sEmpl_c"
     sql += "                     AND d.sDepart_c = e.sDepart_c"
     #sql += "                     AND nCD > 0"
     sql += "         ) AS tmp"
     sql += " WHERE   mon >'2017-09'"
     sql += " GROUP BY mon ,"
     sql += "        sDepart_n"
     sql += " ORDER BY mon "
     lst = objSqlServerHelper.execute4lst(sql)
     return lst