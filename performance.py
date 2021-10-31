from numpy import mat
import pandas as pd
import os
os.system("cls")
import plotly.figure_factory as pff
import statistics
df = pd.read_csv("StudentsPerformance.csv")

math_score = df["math score"].tolist()
# graph = pff.create_distplot([math_score],["Math Score"],show_hist=False)
# graph.show()
mean = statistics.mean(math_score)
stdev = statistics.stdev(math_score)

fstd_sp = mean - stdev
fstd_ep = mean + stdev

fstd_count = 0

for i in math_score:
    if i>fstd_sp and i<fstd_ep:
        fstd_count+=1
f_percentage = (fstd_count/len(math_score))*100
print(f_percentage)

sstd_count = 0
sstd_sp = mean - (2*stdev)
sstd_ep = mean + (2*stdev)

for i in math_score:
    if i>sstd_sp and i<sstd_ep:
        sstd_count+=1
s_percentage = (sstd_count/len(math_score))*100
print(s_percentage)
tstd_count = 0
tstd_sp = mean - (3*stdev)
tstd_ep = mean + (3*stdev)

for i in math_score:
    if i> tstd_sp and i<tstd_ep:
        tstd_count += 1
t_percentage = (tstd_count/len(math_score))*100
print(t_percentage)