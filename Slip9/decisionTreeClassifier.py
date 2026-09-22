from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


x = [
    [6,148,72,35,0,33.6,0.627,50],
    [1,85,66,29,0,26.6,0.351,31],
    [8,183,64,0,0,23.3,0.672,32],
    [1,89,66,23,94,28.1,0.167,21],
    [0,137,40,35,168,43.1,2.288,33],
    [5,116,74,0,0,25.6,0.201,30],
    [3,78,50,32,88,31,0.248,26],
    [10,115,0,0,0,35.3,0.134,29],
    [2,197,70,45,543,30.5,0.158,53],
    [8,125,96,0,0,0,0.232,54],
    [4,110,92,0,0,37.6,0.191,30]
]

y = [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0]

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size = 0.3, random_state = 42
)

for depth in [2, 3, 4]:
    model = DecisionTreeClassifier(
        criterion = 'entropy', 
        max_depth = depth,
        random_state = 42
    )
    
    model.fit(x_train, y_train)
    
    pred = model.predict(x_test)
    
    print("Depth:", depth)
    print("Accuracy:", accuracy_score(y_test, pred))