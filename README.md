# ML-Based Sentiment Analyzer (Improved Version)

## Overview
This project is a medium-level **machine learning sentiment analyzer** made for the **Fundamentals of AI** practical.  
It classifies sentences into three categories:

- **Positive**
- **Negative**
- **Neutral**

This improved version includes:

- Model accuracy calculation  
- Probability scores for each class  
- Loop-based user input  
- Flowchart and architecture diagram  
- Clean Jupyter Notebook implementation  

---

## Features (Updated)
✔️ Machine learning–based sentiment classification  
✔️ Uses **CountVectorizer (Bag of Words)**  
✔️ Uses **Multinomial Naive Bayes**  
✔️ **Displays probabilities** for all classes  
✔️ **Evaluates accuracy** on a small test dataset  
✔️ Easy, understandable logic for viva and external exam  

---

## Dataset
A custom dataset containing 15 sentences:

- 5 Positive  
- 5 Negative  
- 5 Neutral  

All sentences are manually labeled.

---

## Flow Diagram

   ┌────────────────────────┐
   │      User Input        │
   │ (Sentence/Statement)   │
   └────────────┬───────────┘
                │
                ▼
    ┌────────────────────────┐
    │   Text Preprocessing   │
    │  - Lowercasing         │
    │  - Tokenization        │
    └────────────┬───────────┘
                 │
                 ▼
    ┌────────────────────────┐
    │   Feature Extraction   │
    │   CountVectorizer      │
    │  (Bag of Words Model)  │
    └────────────┬───────────┘
                 │
                 ▼
    ┌─────────────────────────┐
    │ ML Model Training       │
    │ Multinomial Naive Bayes │
    └────────────┬────────────┘
                 │
                 ▼
     ┌─────────────────────────┐
     │     Prediction          │
     │  - Sentiment Label      │
     │  - Class Probabilities  │
     └────────────┬────────────┘
                  │
                  ▼
     ┌──────────────────────────┐
     │        Output            │
     │ Positive/Negative/Neutral│
     │ + Probabilities          │
     └──────────────────────────┘

---

## Model Accuracy
A small test dataset was used to check accuracy:

Model accuracy on test set: XX.XX % True labels: [...] Predicted labels: [...]

(Exact accuracy depends on variations.)

---

## Example Output

Enter a sentence: I am happy today

Predicted Sentiment: positive Class probabilities: negative : 0.05 neutral  : 0.10 positive : 0.85

---

##  How to Run

### Install library

pip install scikit-learn

### Run the script

python sentiment_analyzer.py

---

## File Structure

ai-sentiment-analyzer/ │ 
                       ├── sentiment_analyzer.ipynb 
                       ├── sentiment_analyzer.py 
                       ├── requirements.txt 
                       └── README.md

---
## Screenshots
<img width="583" height="190" alt="ai-sentiment-analyzer-test1" src="https://github.com/user-attachments/assets/2febc088-c096-4f7e-9be7-5f8322e9a770" />
<img width="583" height="190" alt="ai-sentiment-analyzer-test2" src="https://github.com/user-attachments/assets/0770a747-a030-4e37-9da4-20cd9fe14fe6" />
<img width="583" height="190" alt="ai-sentiment-analyzer-test3" src="https://github.com/user-attachments/assets/d62d47ea-1b1c-4130-9067-ae9afaf3d7d8" />


## Author
**Yuvraj Narode**  
B.Tech CSE – Fundamentals of AI ML
