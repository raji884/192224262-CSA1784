from sklearn.neural_network import MLPClassifier
X = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]
y = [0, 1, 1, 1]
model = MLPClassifier(hidden_layer_sizes=(4,),
                      max_iter=1000,
                      random_state=1)
model.fit(X, y)
test = [[1, 1]]

prediction = model.predict(test)

print("Input:", test[0])
print("Predicted Output:", prediction[0])
