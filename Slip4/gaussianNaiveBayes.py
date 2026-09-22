from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
x, y = make_blobs(
    n_samples=200,
    centers=3,
    cluster_std=1.5,
    random_state=42
)

x_train, x_test, y_train, y_test = train_test_split(
    x, y, random_state=42
)

model = GaussianNB()

model.fit(x_train, y_train)

pred = model.predict(x_test)

print("Accuracy:", accuracy_score(y_test, pred))

test_data = [[-2, 5], [0, 0], [6, -0.3]]

print("Prediction:", model.predict(test_data))