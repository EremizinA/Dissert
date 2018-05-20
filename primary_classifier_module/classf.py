from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

data = [['this is about dogs', 'dogs are really great'],
        ['this is about cats', 'cats are evil']]
labels = ['dogs', 'cats']

vec = CountVectorizer()  # count word occurrences
X = vec.fit_transform([' '.join(row) for row in data])

clf = MultinomialNB()  # very simple model for word counts
clf.fit(X, labels)

new_data = ['this is about cats too', 'I think cats are awesome']
new_X = vec.transform([' '.join(new_data)])

print(clf.predict(new_X))
# ['cats']