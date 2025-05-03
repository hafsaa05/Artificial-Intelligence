import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, classification_report, roc_curve, auc
import matplotlib.pyplot as plt

# Step 1: Load the dataset
df = pd.read_csv("emails.csv")

# Step 2: Encode categorical features
le_sender = LabelEncoder()
df['sender_encoded'] = le_sender.fit_transform(df['sender'])

le_domain = LabelEncoder()
df['domain_encoded'] = le_domain.fit_transform(df['domain'])

# Step 3: Prepare features and label
X = df[['sender_encoded', 'domain_encoded']]
y = df['spam']

# Step 4: Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# Step 5: Train the model (Decision Tree)
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Step 6: Predictions
y_pred = model.predict(X_test)
y_probs = model.predict_proba(X_test)[:, 1]

# Step 7: Evaluation
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Step 8: ROC Curve
fpr, tpr, _ = roc_curve(y_test, y_probs)
roc_auc = auc(fpr, tpr)

plt.plot(fpr, tpr, label="AUC = {:.2f}".format(roc_auc), color='blue')
plt.plot([0, 1], [0, 1], linestyle='--', color='gray')
plt.title("ROC Curve")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.legend()
plt.grid(True)
plt.show()
