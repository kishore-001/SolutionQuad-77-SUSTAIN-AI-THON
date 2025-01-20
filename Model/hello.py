import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib

# Load the dataset
data = pd.read_csv('./data_set.csv')

# Selecting only the required features (moisture, pH, temperature)
data = data[['temperature', 'humidity', 'ph', 'label']]

# Display the first few rows
print(data.head())

# Check for missing values
print(data.isnull().sum())

# Visualize Crop Type Distribution
plt.figure(figsize=(10, 5))
sns.countplot(x='label', data=data, order=data['label'].value_counts().index, palette='viridis')
plt.xticks(rotation=45)
plt.title('Crop Type Distribution')
plt.show()

# Handling missing values (if any)
imputer = SimpleImputer(strategy='mean')
data[['temperature', 'humidity', 'ph']] = imputer.fit_transform(data[['temperature', 'humidity', 'ph']])

# Visualizing distributions (Boxplots for outliers)
plt.figure(figsize=(15, 5))
for i, col in enumerate(['temperature', 'humidity', 'ph']):
    plt.subplot(1, 3, i + 1)
    sns.boxplot(data[col])
    plt.title(f'Boxplot of {col}')
plt.tight_layout()
plt.show()

# Capping outliers using IQR
def cap_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    df[column] = np.where(df[column] < lower_bound, lower_bound, df[column])
    df[column] = np.where(df[column] > upper_bound, upper_bound, df[column])

for col in ['temperature', 'humidity', 'ph']:
    cap_outliers(data, col)

# Re-visualize boxplots after outlier capping
plt.figure(figsize=(15, 5))
for i, col in enumerate(['temperature', 'humidity', 'ph']):
    plt.subplot(1, 3, i + 1)
    sns.boxplot(data[col])
    plt.title(f'Boxplot of {col} (After Outlier Removal)')
plt.tight_layout()
plt.show()

# Distribution plots
for col in ['temperature', 'humidity', 'ph']:
    sns.kdeplot(data[col], shade=True)
    plt.title(f'Distribution of {col}')
    plt.show()

# Correlation matrix
numeric_data = data.select_dtypes(include=[np.number])
corr_matrix = numeric_data.corr()
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Correlation Matrix")
plt.show()

# Mean feature values by crop type
crop_mean = data.groupby('label').mean()
print(crop_mean)

plt.figure(figsize=(12, 8))
sns.heatmap(crop_mean, annot=True, cmap='YlGnBu')
plt.title('Average Feature Values by Crop Type')
plt.show()

# Encode the target variable
label_encoder = LabelEncoder()
data['crop'] = label_encoder.fit_transform(data['label'])

# Standardize the features
scaler = StandardScaler()
scaled_features = scaler.fit_transform(data[['temperature', 'humidity', 'ph']])
X = pd.DataFrame(scaled_features, columns=['temperature', 'humidity', 'ph'])
y = data['label']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Random Forest model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Predictions and evaluation
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Save the trained model and scaler
joblib.dump(model, 'random_forest_model.pkl')
joblib.dump(scaler, 'scaler.pkl')

# Confusion Matrix
conf_matrix = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=label_encoder.classes_, yticklabels=label_encoder.classes_)
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()