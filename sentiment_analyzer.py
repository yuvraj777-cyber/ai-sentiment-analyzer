#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score


# In[2]:


# Small custom training dataset
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


# Convert text to numerical features
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(sentences)

# Train Naive Bayes model
model = MultinomialNB()
model.fit(X, labels)

print("Model trained on custom dataset.")


# In[4]:


# Small test dataset to check model accuracy
test_sentences = [
    "I really love this movie",
    "This food is terrible",
    "Today is a normal day",
    "I am very disappointed",
    "I feel amazing"
]

test_labels = [
    "positive",
    "negative",
    "neutral",
    "negative",
    "positive"
]

# Transform test sentences
X_test = vectorizer.transform(test_sentences)
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(test_labels, y_pred)

print("Model accuracy on small test set:", round(accuracy * 100, 2), "%")
print("True labels     :", test_labels)
print("Predicted labels:", list(y_pred))


# In[ ]:


def predict_sentiment(text):
    # Transform input text
    x_test = vectorizer.transform([text])

    # Predicted label
    label = model.predict(x_test)[0]

    # Predicted probabilities for each class
    probs = model.predict_proba(x_test)[0]

    # Map class name -> probability
    class_probs = {
        cls: round(float(p), 3)
        for cls, p in zip(model.classes_, probs)
    }

    return label, class_probs


print("===== Sentiment Analyzer (with probabilities) =====")
print("Type 'exit' to quit.\n")

while True:
    sentence = input("Enter a sentence: ")

    if sentence.lower() == "exit":
        print("Exiting...")
        break

    label, prob_dict = predict_sentiment(sentence)

    print("\nPredicted Sentiment:", label)
    print("Class probabilities:")
    for cls, p in prob_dict.items():
        print(f"  {cls:8s}: {p}")
    print("\n" + "-"*40 + "\n")


# In[ ]:




