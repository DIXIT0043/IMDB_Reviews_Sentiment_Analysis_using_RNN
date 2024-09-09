import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.datasets import imdb
import streamlit as st

word_index = imdb.get_word_index()
reverse_word_index = dict([(value,key) for (key,value) in word_index.items()])

def decode_review(test_review):
    decoded_review = ' '.join([reverse_word_index.get(i-3,'?') for i in test_review])
    return decoded_review

model = load_model('simple_RNN.h5')
model.summary()

def preprocess_text(text):
    words = text.lower().split()
    encoded_review = [word_index.get(word,2)+3 for word in words]
    padded_review = sequence.pad_sequences([encoded_review],maxlen=500)
    return padded_review

st.title('IMDB Movie Review Sentiment Analysis')
st.write('Enter the movie review to check if it is positive or negative')

user_input = st.text_area('Movie Review')
if st.button('Check'):
    preprocess_input = preprocess_text(user_input)
    prediction = model.predict(preprocess_input)
    sentiment = 'Positive' if prediction[0][0] > 0.5 else 'Negative'
    st.write(f'Sentiment : {sentiment}')
    st.write(f'Prediction score : {((prediction[0][0])*100):.3f}%')
else:
    st.write('Please Enter a Movie review')
