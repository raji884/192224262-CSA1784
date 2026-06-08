from sklearn.tree import DecisionTreeClassifier
X = [[25], [30], [45], [35], [22], [40]]
y = ["No", "No", "Yes", "Yes", "No", "Yes"]
model = DecisionTreeClassifier()
model.fit(X, y)
age = [[38]]
prediction = model.predict(age)

print("Prediction for Age 38:", prediction[0])
