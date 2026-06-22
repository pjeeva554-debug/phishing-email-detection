import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix

# Sample Dataset
data = {
    "Email": [
        "Click here to claim your prize",
        "Meeting scheduled tomorrow",
        "Verify your bank account immediately",
        "Project report attached",
        "Urgent! Update your password",
        "Team meeting at 2 PM",
        "Win a free iPhone now",
        "Assignment submission deadline"
    ],
    "Label": [
        "Phishing",
        "Safe",
        "Phishing",
        "Safe",
        "Phishing",
        "Safe",
        "Phishing",
        "Safe"
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Features (Email Text)
X = df["Email"]

# Target (Safe or Phishing)
y = df["Label"]

# Convert text into numbers
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(X)

# Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# Train Model
model = MultinomialNB()
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", accuracy * 100, "%")

# Confusion Matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))

# User Input
email = input("\nEnter Email Content: ")

# Convert input to TF-IDF
email_vector = vectorizer.transform([email])

# Predict
result = model.predict(email_vector)

print("\nPrediction:", result[0])