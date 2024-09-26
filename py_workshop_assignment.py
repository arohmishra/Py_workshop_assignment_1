import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Physics.csv")


# 1. Highest attendance in the first five rows
x=a.head(5)
y=a.iloc[:5].loc[a["Attendance"].iloc[:5].idxmax()]
print("\n1 - Highest attendance in first five row")
print(y)


# 2. Highest attendance in the lastt five rows
c=a.iloc[-5:].loc[a["Attendance"].iloc[-5:].idxmax()]
print("\n2 - Highest attendance in last five row")
print(c)


# 3. Highest attendance between rows 10-20
d=a.iloc[9:20].loc[a["Attendance"].iloc[9:20].idxmax()]
print("\n3 - Highest attendance in row 10-20")
print(d)


# 4. Highest attendance overall
e=a.loc[a["Attendance"].idxmax()]
print("\n4 - Student Having Highest attendance overall")
print(e)
