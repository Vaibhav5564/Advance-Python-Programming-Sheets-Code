from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

x = [
    [2,60,55],
    [3,65,60],
    [4,70,65],
    [5,75,70],
    [6,80,75],
    [7,85,80],
    [1,55,50],
    [2,62,58],
    [5,78,72],
    [8,90,85] 
]

y = ['Fail', 'Fail', 'Pass', 'Pass', 'Pass', 'Pass', 'Fail', 'Fail', 'Pass', 'Pass']

encoder = LabelEncoder()

y = encoder.fit_transform(y)

model = RandomForestClassifier(random_state=42)

model.fit(x, y)

test = [[6, 82, 78]]

prediction = model.predict(test)

print("Prediction:", encoder.inverse_transform(prediction))
