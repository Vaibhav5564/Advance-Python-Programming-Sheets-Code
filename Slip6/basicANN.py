from sklearn.neural_network import MLPClassifier

x = [
    [3, 1.5],
    [2, 1],
    [4, 1.5],
    [3, 4],
    [3.5, 0.5],
    [2, 0.5],
    [5.5, 1],
    [1, 1]
]

y = [0, 1, 0, 1, 0, 1, 1, 0]

model = MLPClassifier(
    learning_rate_init=0.1,
    max_iter=20,
    random_state=42
)

model.fit(x, y)

print("Prediction:", model.predict(x))
print("Accuracy:", model.score(x, y))