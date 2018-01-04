from SqlServerHelper import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#取数据
objSqlServerHelper=SqlServerHelper(server="localhost",database="gz_kqyc_2017-12-04", uid="sa", pwd="123")
lst=objSqlServerHelper.execute4lst("SELECT top 10000 Convert(char(10),dDate,108) FROM dbo.yCheckWorkData")
print(lst)

data = pd.DataFrame(
    lst,
    index=np.arange(1000),
    columns=list("ABCD")
    )
data.cumsum()
data.plot()

ax = data.plot.scatter(x='A',y='B',color='DarkBlue',label='Class1')
data.plot.scatter(x='A',y='C',color='LightGreen',label='Class2',ax=ax)

plt.show()