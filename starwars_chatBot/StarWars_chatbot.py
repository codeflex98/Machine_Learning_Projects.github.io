import streamlit as st
import random
import json
import nltk
import numpy as np
import tensorflow as tf
from nltk.stem import WordNetLemmatizer

# Load intents
with open("starwarsintents.json", "r") as file:
    intents = json.load(file)

lemmatizer = WordNetLemmatizer()

# Load trained model
model = tf.keras.models.load_model("chatbot_model.h5")

# Preprocess words and classes
words = sorted(set([lemmatizer.lemmatize(w.lower()) for intent in intents['intents'] for pattern in intent['patterns'] for w in pattern.split()]))
classes = sorted(set(intent['tag'] for intent in intents['intents']))

def bag_of_words(sentence):
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence.split()]
    bag = [1 if w in sentence_words else 0 for w in words]
    return np.array(bag)

def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return classes[results[0][0]] if results else "unknown"

def get_response(tag):
    for intent in intents['intents']:
        if intent['tag'] == tag:
            return random.choice(intent['responses'])
    return "I'm not sure how to respond to that."

# Streamlit App
st.title("Star Wars Chatbot")
st.write("Select a predefined question or type your own!")

# Dropdown for predefined questions
questions = [p for intent in intents['intents'] for p in intent['patterns']]
selected_question = st.selectbox("Choose a question:", questions)

# User input
user_input = st.text_input("Or type your own question:", selected_question)

if st.button("Get Response"):
    tag = predict_class(user_input)
    response = get_response(tag)
    st.write(f"**Bot:** {response}")
