from sklearn.svm import SVC

x = [[1, 2], [2, 3], [5, 5]]
y = [0, 0, 1]

model = SVC(kernel="rbf")

model.fit(x, y)

test = [[4, 4]]

print("Prediction:", model.predict(test))