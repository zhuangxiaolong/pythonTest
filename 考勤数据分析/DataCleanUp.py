from SqlServerHelper import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pylab as pl
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=12)

class DataCleanUp:
    def __init__(self,departmentData,data):  
        ''''' initialization '''  
        self.departmentData = departmentData  
        self.data = data  
    def clean_data(self):
        #取数据
        lst=[]
        for department in self.departmentData:
             eachDepartment=[]
             for row in self.data:
                 if row[1]==department[0]:
                    eachDepartment.append(row)
             lst.append(eachDepartment)
        return lst