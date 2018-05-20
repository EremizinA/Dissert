from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB


class SimpleClassifier:
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

        self.classifier = MultinomialNB()  # very simple model for word counts
        self.classifier.fit(self.matrix, self.labels)
        self.new_matrix = self.vec.transform([' '.join(self.new_data)])

        return self.classifier.predict(self.new_matrix)


data = [['this is about dogs', 'dogs are really great'],
        ['this is about cats', 'cats are evil'],
        ['this is about mouses', 'this is about mouses are good']]
labels = ['dogs', 'cats', 'mouses']
new_data = ['cat fdsfsd', 'cats fdsf']

classifier1 = SimpleClassifier(data, labels, None, None, None, new_data, None)


predict1 = classifier1.predict_data_class()

print(predict1)

# ['cats']