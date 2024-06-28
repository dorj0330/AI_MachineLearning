import pandas as pd
from sklearn import tree

# Read the CSV file
df = pd.read_csv('./data.csv')

# Convert categorical variables into numerical variables
df['Humidity'] = df['Humidity'].map({'normal': 0, 'high': 1})
df['Temperature'] = df['Temperature'].map({'cool': 0, 'warm': 1})
df['Outlook'] = df['Outlook'].map({'sunny': 0, 'rain': 1})
df['Win'] = df['Win'].map({'yes': 1, 'no': 0})

# Define features and target variable
X = df[['Humidity', 'Temperature', 'Outlook']]
y = df['Win']

# Create decision tree classifier
clf = tree.DecisionTreeClassifier()

# Train the classifier
clf = clf.fit(X, y)

# Export the decision tree as a .dot file
tree.export_graphviz(clf, out_file='decision_tree.dot', 
                     feature_names=['Humidity', 'Temperature', 'Outlook'], 
                     class_names=['No', 'Yes'], 
                     filled=True, rounded=True)

print("Decision tree exported as 'decision_tree.dot'")
