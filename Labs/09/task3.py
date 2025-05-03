import pandas as pd                  
import numpy as np                  
from sklearn.model_selection import train_test_split  
from sklearn.svm import SVC          
from sklearn.metrics import confusion_matrix, roc_curve, auc  
import matplotlib.pyplot as plt      
import seaborn as sns                

df = pd.read_csv("customers.csv")  
df = df.fillna(df.mean())

#Split data into features (X) and label (y)
X = df[['total_spending', 'age', 'visits', 'purchase_frequency']]  # Features
y = df['high_value']  # Target label (0 = Low Value, 1 = High Value)

#Split the dataset into training and testing sets 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 6: Train a Support Vector Machine model 
model = SVC(kernel='linear', probability=True)  # Using linear kernel
model.fit(X_train, y_train)  # Training the model

y_pred = model.predict(X_test)  # Predicting class labels

#Evaluate model using Confusion Matrix (5.1 Confusion Matrix)
cm = confusion_matrix(y_test, y_pred)  # Create confusion matrix

# Visualize Confusion Matrix
sns.heatmap(cm, annot=True, cmap="Blues", fmt="d")
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

#Evaluate model using ROC Curve (5.2 ROC Curve)
y_prob = model.predict_proba(X_test)[:, 1]  # Probabilities for class 1 (high value)

# Calculate False Positive Rate and True Positive Rate
fpr, tpr, thresholds = roc_curve(y_test, y_prob)

# Calculate AUC
roc_auc = auc(fpr, tpr)

# Plot ROC Curve
plt.plot(fpr, tpr, label="AUC = %.2f" % roc_auc)
plt.plot([0, 1], [0, 1], linestyle='--', color='gray')  # Diagonal reference line
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.legend()
plt.show()
