# ------------------------------------------------------------------------------
# Deep Learning Test
# ------------------------------------------------------------------------------
from sklearn.datasets        import load_iris
from sklearn.model_selection import train_test_split
iris = load_iris()

# Show Dataset Head 5 data
for idx, item in enumerate(zip(iris.data, iris.target)):
  if idx == 5:
    break

  print('data:', item[0], ', target:', item[1])

# Devide DataSet
print("")
print('length of iris.data:'  , len(iris.data))
print('length of iris.target:', len(iris.target))

# Shuffle & Devide iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target)
print('length of X_train:', len(X_train))
print('length of y_train:', len(y_train))
print('length of X_test:' , len(X_test))
print('length of y_test:' , len(y_test))
