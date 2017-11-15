from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from scipy.spatial import distance

def euc(a, b):
    return distance.euclidean(a, b)

class ScrappyKNN():
    def fit(self, features_train, labels_train):
        self.features_train = features_train
        self.labels_train = labels_train

    def predict(self, features_test):
        prediction = []
        for item in features_test:
            label = self.closest(item)
            prediction.append(label)

        return prediction

    def closest(self, item):
        best_dist = euc(item, self.features_train[0])
        best_index = 0
        for i in range(1, len(self.features_train)):
            dist = euc(item, self.features_train[i])
            if dist < best_dist:
                best_dist = dist
                best_index = i

        return self.labels_train[best_index]

iris = datasets.load_iris()

features = iris.data
labels = iris.target

features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=.5)

my_classifier = ScrappyKNN()
my_classifier.fit(features_train, labels_train)

prediction = my_classifier.predict(features_test)

print (accuracy_score(labels_test, prediction))

# Virginica
iris1 = [[7.1, 2.9, 5.3, 2.4]]
iris_prediction = my_classifier.predict(iris1)

if iris_prediction[0] == 0:
    print("Setosa")

if iris_prediction[0] == 1:
    print("Versicolor")

if iris_prediction[0] == 2:
    print("Virginica")
