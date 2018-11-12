from  sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('crimedata.csv')
print(df)

s=df[df["CRIME HEAD"]=="RAPE"]
# YEAR WISE
l=s[s["STATE/UT"]=="All India"]
print(l)
l=l.drop(["STATE/UT"],axis=1)
l=l.drop(["CRIME HEAD"],axis=1)
print(l)
x=[]
for i in l:
  x.append(i)
print(l[x[0]])

z=[]
#print(l)
for i in range(0,len(x)):
  plt.bar(x[i],l[x[i]],color="red")
plt.xlabel("Year")
plt.ylabel("Number of Rapes")
plt.title("Total Rape year wise")
plt.show()
l=l.reset_index()
print(l)


kmeans=KMeans(n_clusters=3)
q=[]

for i in x:
    print(i)
    q.append(list(l[i].values))
print(q)
y=[]
for i in q:
    for j in i:
        y.append(j)
print(y)
y=np.array(y)
y=y.reshape(-1,1)
kmeans.fit(y)
print(kmeans.labels_)
colors=["red","green","yellow"]
for  i in range(0,len(x)):
    plt.bar(x[i],l[x[i]],color=colors[kmeans.labels_[i]])
plt.xlabel("Year")
plt.ylabel("Number of Rapes")
plt.title("Total Rapes year wise")

plt.show()
# STATE WISE
m=s[s["STATE/UT"]!="All India"]
print(m)
m=m.reset_index()
df=m
df['TOTALCRIME']=m['2001']+m['2002']+m['2003']+m['2004']+m['2005']+m['2006']+m['2007']+m['2008']+m['2009']+m['2010']+m['2011']+m['2012']
print(df)
s=df[["TOTALCRIME","STATE/UT"]]
print(s)
m=df["TOTALCRIME"].values
print(m)
plt.bar(df["STATE/UT"],df["TOTALCRIME"])
plt.xticks(rotation="vertical")
plt.show()
plt.scatter(df["STATE/UT"],df["TOTALCRIME"])
plt.xticks(rotation="vertical")
plt.xlabel("States")
plt.ylabel("Number of rape statewise")
plt.title("Rape state wise")
plt.show()
kmeans=KMeans(n_clusters=3)
m=np.array(m)
m=m.reshape(-1,1)
kmeans.fit(m)
colors=["green","blue","red"]
for i in range(0,len(df)):
    plt.bar(df["STATE/UT"][i],df["TOTALCRIME"][i],color=colors[kmeans.labels_[i]])
plt.xticks(rotation="vertical")
plt.xlabel("States")
plt.ylabel("Number of rape statewise")
plt.title("Rape state wise")
plt.show()