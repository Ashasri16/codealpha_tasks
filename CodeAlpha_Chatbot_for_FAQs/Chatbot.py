import streamlit as st
import nltk
import string
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')

faq_questions = [
    "What is Artificial Intelligence?",
    "What is Machine Learning?",
    "What is Deep Learning?",
    "What is NLP?",
    "What is Python?",
    "What is ChatGPT?",
     "What is a Neural Network?",
    "What is Generative AI?",
    "What is supervised learning?",
    "What is unsupervised learning?"
]
faq_answers = [
    "Artificial Intelligence is the simulation of human intelligence by machines.",
    "Machine Learning is a subset of AI that learns from data.",
    "Deep Learning is a subset of Machine Learning that uses neural networks.",
    "NLP stands for Natural Language Processing.",
    "Python is a popular programming language.",
    "ChatGPT is an AI chatbot developed by OpenAI.",
    "A Neural Network is a computing model inspired by the human brain.",
    "Generative AI creates new content such as text, images, and audio.",
    "Supervised learning uses labeled data to train models.",
    "Unsupervised learning finds patterns in unlabeled data."
     
]

def preprocess(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = word_tokenize(text)
    return " ".join(tokens)

st.title("FAQ Chatbot")

user_question = st.text_input("Ask a Question")

if user_question:

    processed_questions = [preprocess(q) for q in faq_questions]
    processed_user = preprocess(user_question)

    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform(
        processed_questions + [processed_user]
    )

    similarity = cosine_similarity(
        vectors[-1],
        vectors[:-1]
    )

    best_match = similarity.argmax()

    st.write(faq_answers[best_match])