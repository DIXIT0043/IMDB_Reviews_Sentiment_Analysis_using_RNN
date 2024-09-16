# IMDB Movie Review Sentiment Analysis

This project is a web application that performs sentiment analysis on IMDB movie reviews. The application uses a pre-trained Recurrent Neural Network (RNN) model to predict whether a given movie review is positive or negative.
## Visit
Link =[ https://obesity-detector-bydixit.streamlit.app/](https://imdbreviewssentimentanalysisusingrnn-bydixit.streamlit.app/)
## Features
- Accepts user input in the form of movie reviews.
- Preprocesses the input to match the format required by the model.
- Displays whether the sentiment is **Positive** or **Negative** based on the model's prediction.
- Shows the prediction score as a percentage.

## Technologies Used
- Python
- TensorFlow/Keras
- Streamlit for the web interface
- IMDB Dataset for movie reviews

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/DIXIT0043/IMDB_Reviews_Sentiment_Analysis_using_RNN.git
    ```

2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Download the IMDB dataset using Keras and place the pre-trained RNN model in the specified directory.

4. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

## Model

The application uses a pre-trained RNN model, located at `simple_RNN.h5`, to perform sentiment analysis on movie reviews. You can load this model in the `app.py` file.

### Preprocessing

The input review text is preprocessed by:
1. Converting the words to lowercase.
2. Tokenizing the words using the IMDB word index.
3. Padding the sequence to a maximum length of 500 tokens.

### Output

- The sentiment is classified as **Positive** if the model's prediction score is above 0.5, otherwise, it's **Negative**.
- The exact prediction score is displayed as a percentage.

## Usage

1. Enter a movie review in the text area.
2. Click the **Check** button to analyze the sentiment.
3. The sentiment and prediction score will be displayed below the input field.

## Example

- Input: `This movie was fantastic!`
- Output: `Sentiment: Positive`  
  `Prediction score: 85.762%`
