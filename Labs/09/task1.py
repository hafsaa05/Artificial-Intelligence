import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("house_data.csv")

# Fill missing values for numerical columns with median and categorical with mode
df['square_footage'] = df['square_footage'].fillna(df['square_footage'].median())
df['bedrooms'] = df['bedrooms'].fillna(df['bedrooms'].median())
df['bathrooms'] = df['bathrooms'].fillna(df['bathrooms'].median())
df['age_of_house'] = df['age_of_house'].fillna(df['age_of_house'].median())
df['neighborhood'] = df['neighborhood'].fillna(df['neighborhood'].mode()[0])

# One-Hot Encoding for the 'neighborhood' column
df = pd.get_dummies(df, columns=['neighborhood'], drop_first=True)

# Separate features and target variable
X = df.drop('price', axis=1)
y = df['price']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Cross-validation with K-Fold to evaluate the model
kfold = KFold(n_splits=5, shuffle=True, random_state=42)
r2_scores = cross_val_score(model, X, y, cv=kfold, scoring='r2')
mse_scores = -cross_val_score(model, X, y, cv=kfold, scoring='neg_mean_squared_error')

# Print Cross-Validation Results
print(f"Cross-Validation R² Scores: {r2_scores}")
print(f"Average R² Score: {r2_scores.mean():.2f}")
print(f"Average MSE: {mse_scores.mean():.2f}")

# Predict price for a new house
new_house = {
    'square_footage': 2200,
    'bedrooms': 3,
    'bathrooms': 2,
    'age_of_house': 5,
    'neighborhood_B': 0,
    'neighborhood_C': 1
}
new_df = pd.DataFrame([new_house])
predicted_price = model.predict(new_df)
print(f"Predicted Price for New House: ${predicted_price[0]:,.2f}")

# Evaluate the model on the test set
y_pred = model.predict(X_test)

# Calculate final R² and MSE
final_r2 = r2_score(y_test, y_pred)
final_mse = mean_squared_error(y_test, y_pred)

# Print the final evaluation
print(f"Final R² Score: {final_r2:.2f}")
print(f"Final MSE: {final_mse:.2f}")

# Plot the true vs predicted prices
plt.scatter(y_test, y_pred)
plt.xlabel('True Values')
plt.ylabel('Predicted Values')
plt.title('True vs Predicted House Prices')
plt.show()
