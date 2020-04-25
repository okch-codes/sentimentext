import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import matplotlib.pyplot as plt

text="""Hello Mr. Smith, how are you doing today? The weather is great, and city is awesome.
The sky is pinkish-blue. You weather shouldn't eat cardboard. Albert Einstein was born in Ulm, Germany in 1879."""
"""
tokenized_word=word_tokenize(text)
print("--- TOKENIZED WORD ---")
print(tokenized_word)
print("----------------------\n")

tokenized_text=sent_tokenize(text)
print("--- TOKENIZED TEXT ---")
print(tokenized_text)
print("----------------------\n")

fdist = FreqDist(tokenized_word)
print(fdist)

#print(fdist.most_common(10))

from nltk.corpus import stopwords
nltk.download('stopwords')
stop_words=set(stopwords.words("english"))

filtered_word=[]
for w in tokenized_word:
    if w not in stop_words:
        filtered_word.append(w)
print("Tokenized Sentence:",tokenized_word)
print("Filterd Sentence:",filtered_word)

nltk.download('wordnet')
from nltk.stem.wordnet import WordNetLemmatizer
lem = WordNetLemmatizer()

lemmatize_text=""
for w in filtered_word:    
    lemmatize_text += lem.lemmatize(w,"v")+" "
    print("Lemmatized Word:",lem.lemmatize(w,"v"), "(before: ",w,")")
nltk.download('averaged_perceptron_tagger')
lemmatize_text_tokenized = nltk.word_tokenize(lemmatize_text)
print(nltk.pos_tag(lemmatize_text_tokenized))
"""
import pandas as pd
data=pd.read_csv('train.tsv', sep='\t')
""" print(data.Sentiment.value_counts())
Sentiment_count=data.groupby('Sentiment').count()
plt.bar(Sentiment_count.index.values, Sentiment_count['Phrase'])
plt.xlabel('Review Sentiments')
plt.ylabel('Number of Review')
plt.show() """


from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import RegexpTokenizer
token = RegexpTokenizer(r'[a-zA-Z0-9]+')
print(token.tokenize)
cv = CountVectorizer(
        lowercase=True,
        stop_words='english',
        ngram_range = (1,1),
        tokenizer = token.tokenize
    )
text_counts= cv.fit_transform(data['Phrase'])
print(text_counts)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    text_counts,
    data['Sentiment'],
    test_size=0.33,
    random_state=1
)

from sklearn.naive_bayes import MultinomialNB
#Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics
# Model Generation Using Multinomial Naive Bayes
clf = MultinomialNB().fit(X_train, y_train)
predicted= clf.predict(X_test)
print("MultinomialNB Accuracy:",metrics.accuracy_score(y_test, predicted))