import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder, StandardScaler
import matplotlib.pyplot as plt

data = {
    'vehicle_serial_no': [5, 3, 8, 2, 4, 7, 6, 10, 1, 9],
    'mileage': [150000, 120000, 250000, 80000, 100000, 220000, 180000, 300000, 75000, 280000],
    'fuel_efficiency': [15, 18, 10, 22, 20, 12, 16, 8, 24, 9],
    'maintenance_cost': [5000, 4000, 7000, 2000, 3000, 6500, 5500, 8000, 1500, 7500],
    'vehicle_type': ['SUV', 'Sedan', 'Truck', 'Hatchback', 'Sedan', 'Truck', 'SUV', 'Truck', 'Hatchback', 'SUV']
}
df = pd.DataFrame(data)

le = LabelEncoder()
df['vehicle_type_encoded'] = le.fit_transform(df['vehicle_type'])

# -----------------------------Clustering without Scaling-----------------------------
X_unscaled = df[['mileage', 'fuel_efficiency', 'maintenance_cost', 'vehicle_type_encoded']]

kmeans_unscaled = KMeans(n_clusters=3, random_state=0)
df['cluster_unscaled'] = kmeans_unscaled.fit_predict(X_unscaled)

# -----------------------------Clustering with Scaling (excluding vehicle_type)-----------------------------
scaler = StandardScaler()
scaled_features = scaler.fit_transform(df[['mileage', 'fuel_efficiency', 'maintenance_cost']])

# Combine scaled features with encoded vehicle_type
X_scaled = pd.concat([
    pd.DataFrame(scaled_features, columns=['mileage', 'fuel_efficiency', 'maintenance_cost']),
    df['vehicle_type_encoded']
], axis=1)

kmeans_scaled = KMeans(n_clusters=3, random_state=0)
df['cluster_scaled'] = kmeans_scaled.fit_predict(X_scaled)

# Compare Results
print("Cluster assignments WITHOUT scaling:")
print(df[['vehicle_serial_no', 'cluster_unscaled']])
print("\nCluster assignments WITH scaling:")
print(df[['vehicle_serial_no', 'cluster_scaled']])

# Plot unscaled
plt.subplot(1, 2, 1)
plt.scatter(df['mileage'], df['fuel_efficiency'], c=df['cluster_unscaled'], cmap='viridis')
plt.title("Without Scaling")
plt.xlabel("Mileage")
plt.ylabel("Fuel Efficiency")

# Plot scaled
plt.subplot(1, 2, 2)
plt.scatter(df['mileage'], df['fuel_efficiency'], c=df['cluster_scaled'], cmap='viridis')
plt.title("With Scaling")
plt.xlabel("Mileage")
plt.ylabel("Fuel Efficiency")

plt.tight_layout()
plt.show()
