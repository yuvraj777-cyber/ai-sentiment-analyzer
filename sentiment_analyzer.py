#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB


# In[2]:


sentences = [
    "I love this product",
    "This is a great day",
    "I am very happy",
    "The movie was awesome",
    "I enjoyed the food",

    "I hate this",
    "This is a bad experience",
    "I am feeling sad",
    "The service was terrible",
    "I am disappointed",

    "I am going to school",
    "It is a normal day",
    "He is reading a book",
    "I went to the market",
    "She is watching TV"
]

labels = [
    "positive", "positive", "positive", "positive", "positive",
    "negative", "negative", "negative", "negative", "negative",
    "neutral", "neutral", "neutral", "neutral", "neutral"
]


# In[3]:


vectorizer = CountVectorizer()
X = vectorizer.fit_transform(sentences)

model = MultinomialNB()
model.fit(X, labels)


# In[4]:


def predict_sentiment(text):
    x_test = vectorizer.transform([text])
    return model.predict(x_test)[0]

sentence = input("Enter a sentence: ")
print("Predicted Sentiment:", predict_sentiment(sentence))


# In[ ]:




