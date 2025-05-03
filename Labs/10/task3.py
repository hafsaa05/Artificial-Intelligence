import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import numpy as np

data = {
    'student_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'GPA': [3.5, 3.7, 3.8, 2.9, 3.1, 3.3, 3.9, 2.7, 3.6, 2.8],
    'study_hours': [15, 20, 25, 10, 12, 18, 30, 9, 22, 16],
    'attendance_rate': [90, 85, 92, 75, 80, 88, 95, 70, 90, 82]
}

df = pd.DataFrame(data)

X = df[['GPA', 'study_hours', 'attendance_rate']]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

wcss = []
for k in range(2, 7):  # Trying K from 2 to 6
    kmeans = KMeans(n_clusters=k, init='k-means++', random_state=42)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

plt.plot(range(2, 7), wcss, marker='o')
plt.title('Elbow Method to Determine Optimal K')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('WCSS')
plt.grid(True)
plt.show()

#Perform Clustering (Assume optimal K=3 from elbow plot)
k_optimal = 3
kmeans = KMeans(n_clusters=k_optimal, random_state=42)
df['cluster'] = kmeans.fit_predict(X_scaled)

plt.figure(figsize=(8, 5))
scatter = plt.scatter(df['study_hours'], df['GPA'], c=df['cluster'], cmap='viridis', s=100)
plt.title('Student Clusters based on Study Hours and GPA')
plt.xlabel('Study Hours (Weekly Average)')
plt.ylabel('GPA')
plt.colorbar(scatter, label='Cluster')
plt.grid(True)
plt.show()

print("Final dataset with clusters:")
print(df[['student_id', 'GPA', 'study_hours', 'attendance_rate', 'cluster']])
