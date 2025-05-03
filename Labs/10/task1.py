import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler, LabelEncoder

df = pd.read_csv("Mall_Customers.csv")

df = df.drop(columns=["CustomerID"])

le = LabelEncoder()
df['Gender'] = le.fit_transform(df['Gender'])  # Female=0, Male=1

# ------------------ Clustering WITHOUT SCALING ------------------

# Get feature values as numpy array
X_all = df.values

kmeans_no_scale = KMeans(n_clusters=5, random_state=42)
labels_no_scale = kmeans_no_scale.fit_predict(X_all)

plt.scatter(X_all[:, 0], X_all[:, 1], c=labels_no_scale, cmap='rainbow')
plt.title("Clustering without Feature Scaling")
plt.xlabel("Gender")
plt.ylabel("Age")
plt.show()

# ------------------ Clustering WITH SCALING (except Age) ------------------

# Save Age column separately (not to scale it)
age = df['Age'].values.reshape(-1, 1)

# Scale Gender, Income, and Spending Score
features_to_scale = df.drop(columns=['Age'])
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features_to_scale)

# Combine scaled features with original Age
X_scaled = np.concatenate((age, scaled_features), axis=1)

kmeans_scaled = KMeans(n_clusters=5, random_state=42)
labels_scaled = kmeans_scaled.fit_predict(X_scaled)

plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=labels_scaled, cmap='rainbow')
plt.title("Clustering with Feature Scaling (Age not scaled)")
plt.xlabel("Age")
plt.ylabel("Scaled Features")
plt.show()
