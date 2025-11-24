# Simple ML-Based Sentiment Analyzer

## Overview
This mini-project is a simple **machine learning-based sentiment analyzer** built for the **Fundamentals of Artificial Intelligence** practical.  
It classifies text into three categories:

- **Positive**
- **Negative**
- **Neutral**

The project uses:
- **CountVectorizer (Bag of Words)**
- **Naive Bayes Classifier**
- A small **custom dataset** created manually.

This project is created using **Jupyter Notebook** and **Python**.

---

## Features
- Simple ML model  
- Custom training dataset  
- Terminal-based user input  
- Easy to understand  
- Perfect for AI fundamentals practical submission  

---

## Technologies Used
- Python  
- Scikit-learn  
- Jupyter Notebook  
- Natural Language Processing (Bag of Words)

---

## Dataset Used
A small dataset of 15 sentences:
- 5 Positive  
- 5 Negative  
- 5 Neutral  

Each sentence is manually labeled.

---

## How It Works
1. Convert text into numerical form using **CountVectorizer**  
2. Train a **Multinomial Naive Bayes** model  
3. Take user input  
4. Predict sentiment using the trained model  

---

## How to Run

### 1. Install Required Library

pip install scikit-learn

### 2. Run the Program

python sentiment_analyzer.py

### 3. Enter any sentence  
Example:

I am very happy today

Output:

Predicted Sentiment: positive

---

## File Structure

ai-sentiment-analyzer/ │ 
                       ├── sentiment_analyzer.ipynb     # Jupyter Notebook 
                       ├── sentiment_analyzer.py        # Python Script 
                       └── README.md                    # Project Documentation

---

## Example Output

Enter a sentence: I am happy today Predicted Sentiment: positive


## Screenshot
<img width="583" height="190" alt="ai-sentiment-analyzer-test" src="https://github.com/user-attachments/assets/22ed902a-da7c-481a-b93b-7efca8b66d4a" />


---

## Author
**Yuvraj Narode**  
B.Tech — Computer Science  
Fundamentals of AI ML Mini Project
