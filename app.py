# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Step 1: Load the dataset
df = pd.read_csv('dataset.csv')

# Step 2: Data Preprocessing
# Convert 'GENDER' to numerical (M = 1, F = 0)
df['GENDER'] = df['GENDER'].apply(lambda x: 1 if x == 'M' else 0)

# Convert 'LUNG_CANCER' to numerical (YES = 1, NO = 0)
df['LUNG_CANCER'] = df['LUNG_CANCER'].apply(lambda x: 1 if x == 'YES' else 0)

# Drop any missing data (if any)
df.dropna(inplace=True)

# Step 3: Split the dataset into features (X) and target (y)
X = df.drop('LUNG_CANCER', axis=1)
y = df['LUNG_CANCER']

# Step 4: Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Initialize Logistic Regression model
model = LogisticRegression(max_iter=1000)

# Step 6: Train the model
model.fit(X_train, y_train)

# Step 7: Make predictions
y_pred = model.predict(X_test)

# Step 8: Evaluate the model
# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")

# Compute the confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(conf_matrix)

# Get the classification report
class_report = classification_report(y_test, y_pred)
print("Classification Report:")
print(class_report)
