from  sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv('crimedata.csv')
print(df)
s=df[df["CRIME HEAD"]=="TOTAL CRIMES AGAINST WOMEN"]
m=s[s["STATE/UT"]!="TOTAL Crime against Women"]
print(m)
m=m.reset_index()
df=m
df['TOTALCRIME']=m['2001']+m['2002']+m['2003']+m['2004']+m['2005']+m['2006']
+m['2007']+m['2008']+m['2009']+m['2010']+m['2011']+m['2012']
print(df)
s=df[["TOTALCRIME","STATE/UT"]]
print(s)
m=df["TOTALCRIME"].values
print(m)
plt.scatter(df["STATE/UT"],df["TOTALCRIME"])
plt.xticks(rotation="vertical")
plt.xlabel("States")
plt.ylabel("Number of crimes statewise")
plt.title("Total crimes state wise")
plt.show()
kmeans=KMeans(n_clusters=3)
m=np.array(m)
m=m.reshape(-1,1)
kmeans.fit(m)
colors=["green","red","blue"]
for i in range(0,len(df)):
    plt.bar(df["STATE/UT"][i],df["TOTALCRIME"][i],color=colors[kmeans.labels_[i]])
plt.xticks(rotation="vertical")
plt.xlabel("States")
plt.ylabel("Number of crimes statewise")
plt.title("Total crimes state wise")
plt.show()