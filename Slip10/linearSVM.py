from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC

X = [
    [5.1,3.5,1.4,0.2],
    [4.9,3.0,1.4,0.2],
    [4.7,3.2,1.3,0.2],
    [4.6,3.1,1.5,0.2],
    [5.0,3.6,1.4,0.2],
    [7.0,3.2,4.7,1.4],
    [6.4,3.2,4.5,1.5],
    [6.9,3.1,4.9,1.5],
    [5.5,2.3,4.0,1.3],
    [6.5,2.8,4.6,1.5]
]

y = [0,0,0,0,0,1,1,1,1,1]

model = Pipeline([
    ('scaler', StandardScaler()),
    ('svm', LinearSVC(C=1, loss='hinge'))
])

model.fit(X, y)

test = [[5.2,3.4,1.5,0.2]]

print("Prediction:", model.predict(test))