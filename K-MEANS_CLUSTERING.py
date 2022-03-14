
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D

plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('ggplot')
DataFrame = pd.read_csv("analisis.csv")
DataFrame.head()
DataFrame.describe()
print(DataFrame.GroupBy('wordcount').size)
DataFrame.drop((['wordcount'],1).hist())
plt.show()
sb.pairplot(DataFrame.dropna(), hue='wordcount',size=4,vars=["op","ex","ag"],kind='scatter')
X = np.array(DataFrame[["op","ex","ag"]])
y = np.array(DataFrame['categoria'])
X.shape

fig = plt.figure()
ax = Axes3D(fig)
colores=['blue','red','green','blue','cyan','yellow','orange','black','pink','brown','purple']
asignar=[]

for row in y:
    asignar.append(colores[row])
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=asignar,s=60)
Nc = range(1, 20)
kmeans = [KMeans(n_clusters=i) for i in Nc]
kmeans
score = [kmeans[i].fit(X).score(X) for i in range(len(kmeans))]
score

plt.plot(Nc,score)
plt.xlabel('Number of Clusters')
plt.ylabel('Score')
plt.title('Elbow Curve')
plt.show()
kmeans = KMeans(n_clusters=5).fit(X)
centroids = kmeans.cluster_centers_
print(centroids)

# Predicting the clusters
labels = kmeans.predict(X)
# Getting the cluster centers
C = kmeans.cluster_centers_
colores = ['red', 'green', 'blue', 'cyan', 'yellow']
asignar = []
for row in labels:
    asignar.append(colores[row])

fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=asignar, s=60)
ax.scatter(C[:, 0], C[:, 1], C[:, 2], marker='*', c=colores, s=1000)

f1 = DataFrame['op'].values
f2 = DataFrame['ex'].values

plt.scatter(f1, f2, c=asignar, s=70)
plt.scatter(C[:, 0], C[:, 1], marker='*', c=colores, s=1000)
plt.show()

f1 = DataFrame['ex'].values
f2 = DataFrame['ag'].values

plt.scatter(f1, f2, c=asignar, s=70)
plt.scatter(C[:, 1], C[:, 2], marker='*', c=colores, s=1000)
plt.show()

f1 = DataFrame['ex'].values
f2 = DataFrame['ag'].values

plt.scatter(f1, f2, c=asignar, s=70)
plt.scatter(C[:, 1], C[:, 2], marker='*', c=colores, s=1000)
plt.show()
copy =  pd.DataFrame()
copy['usuario']=DataFrame['usuario'].values
copy['categoria']=DataFrame['categoria'].values
copy['label'] = labels;
cantidadGrupo =  pd.DataFrame()
cantidadGrupo['color']=colores
cantidadGrupo['cantidad']=copy.groupby('label').size()
cantidadGrupo
group_referrer_index = copy['label'] == 0
group_referrals = copy[group_referrer_index]

diversidadGrupo = pd.DataFrame()
diversidadGrupo['categoria'] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
diversidadGrupo['cantidad'] = group_referrals.groupby('categoria').size()
diversidadGrupo

users=DataFrame['usuario'].values
print(users[row])

X_new = np.array([[45.92, 57.74, 15.66]])  # davidguetta

new_labels = kmeans.predict(X_new)
print(new_labels)
