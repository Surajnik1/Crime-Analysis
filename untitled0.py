from  sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('crimedata.csv')

print(df)
#byCrime=df.groupby('CRIME HEAD')
#byCrime.sum()
s=df[df["CRIME HEAD"]=="TOTAL CRIMES AGAINST WOMEN"]
#print(s)
l=s[s["STATE/UT"]=="TOTAL Crime against Women"]
print(l)

l=l.drop(["STATE/UT"],axis=1)
l=l.drop(["CRIME HEAD"],axis=1)
print(l)

m=[]
for i in l:
  m.append(i)
print(l[m[0]])

z=[]
#print(l)
for i in range(0,len(m)):
  plt.bar(m[i],l[m[i]],color="red")
plt.xlabel("Year")
plt.ylabel("Number of crimes against women")
plt.title("Total crimes year wise")
plt.show()
l=l.reset_index()
print(l)


kmeans=KMeans(n_clusters=3)
q=[]

for i in m:
    print(i)
    q.append(list(l[i].values))
print(q)
x=[]
for i in q:
    for j in i:
        x.append(j)
print(x)
x=np.array(x)
x=x.reshape(-1,1)
kmeans.fit(x)
print(kmeans.labels_)
colors=["red","green","yellow"]
for  i in range(0,len(x)):
    plt.bar(m[i],l[m[i]],color=colors[kmeans.labels_[i]])
plt.xlabel("Year")
plt.ylabel("Number of crimes against women")
plt.title("Total crimes year wise")

plt.show()