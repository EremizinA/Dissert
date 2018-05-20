from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import NuSVC


class SVMClassifier:
    def __init__(self, data, labels, vec, matrix, classifier, new_data, new_matrix):
        self.data = data
        self.labels = labels
        self.vec = None
        self.matrix = None
        self.classifier = None
        self.new_data = new_data
        self.new_matrix = None

    def predict_data_class(self):
        self.vec = CountVectorizer()  # count word occurrences
        self.matrix = self.vec.fit_transform([' '.join(row) for row in self.data])

        self.classifier = NuSVC()  # very simple model for word counts
        self.classifier.fit(self.matrix, self.labels)

        self.new_matrix = self.vec.transform([' '.join(self.new_data)])

        return self.classifier.predict(self.new_matrix)


data = [['FF 00 C4 B3 E3', '00 C3 B5 E3 84', 'C5 B3'],
        ['this is about cats', 'cats are evil'],
        ['this is about mouses', 'this is about mouses are good']]
labels = ['Malware', 'NotMalware']
new_data = ['moses are great', 'thery well dog']

classifier1 = SVMClassifier(data, labels, None, None, None, new_data, None)


predict1 = classifier1.predict_data_class()

print(predict1)
