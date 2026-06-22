# Phishing Email Detection

## Overview

This project is a Machine Learning-based phishing email detection system developed using Python and Scikit-learn. The model analyzes email content and classifies emails as either **Phishing** or **Safe**.

## Features

* Trains on phishing and legitimate email samples
* Uses TF-IDF for feature extraction
* Classifies emails as Phishing or Safe
* Displays model accuracy
* Generates a confusion matrix
* Allows users to test custom email content

## Technologies Used

* Python
* Pandas
* Scikit-learn
* NumPy

## Machine Learning Workflow

1. Load email dataset
2. Extract text features using TF-IDF
3. Split data into training and testing sets
4. Train the model using Multinomial Naive Bayes
5. Evaluate accuracy and confusion matrix
6. Predict whether a new email is Phishing or Safe

## Project Structure

PhishingEmailDetection/
│
├── phishing_detector.py
├── README.md
└── requirements.txt

## Sample Input

Dear Customer,

Your bank account has been suspended.
Please click the link below to verify your account.

Regards,
Bank Team

## Sample Output

Prediction: Phishing

## Another Sample Input

Dear Team,

The project meeting is scheduled for tomorrow at 10:00 AM.

Regards,
Project Manager

## Sample Output

Prediction: Safe

## Learning Outcomes

* Understanding phishing attacks
* Feature extraction using TF-IDF
* Text classification using Naive Bayes
* Model evaluation using Accuracy and Confusion Matrix
* Building basic Machine Learning applications with Scikit-learn

## Future Improvements

* Use a larger real-world email dataset
* Improve classification accuracy
* Add URL-based phishing detection
* Develop a web-based user interface

