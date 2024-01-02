# TradingBot Chatbot

TradingBot is a simple chatbot implemented in Python, specifically designed to provide information and engage in conversations about the stock market. It uses TF-IDF and cosine similarity to generate relevant responses based on user input.

## Features

- **TF-IDF Vectorization:** Converts input sentences into numerical vectors using the `TfidfVectorizer` from scikit-learn, facilitating the understanding of user queries in the context of stock market knowledge.
- **Cosine Similarity:** Measures the cosine similarity between the TF-IDF vector of the user's input and the TF-IDF matrix of existing sentences to find the most relevant responses.
- **Lemmatization:** Employs the WordNet Lemmatizer from the NLTK library for processing natural language, enhancing the understanding of different forms of words.
- **User Interaction:** Designed to engage users in conversations about the stock market, allowing them to ask questions and receive informative responses.

## Outputs (Interface)
<img src="output/Screenshot (257).png" alt="Image Description" width="250px">
<img src="output/Screenshot (258).png" alt="Image Description" width="250px">
<img src="output/Screenshot (259).png" alt="Image Description" width="250px">
<img src="output/Screenshot (260).png" alt="Image Description" width="250px">

## Dependencies

- `numpy`: Used for numerical operations.
- `nltk`: Natural Language Toolkit, essential for processing human language data.
- `scikit-learn`: Provides necessary machine learning tools, including the `TfidfVectorizer`.
- `string`: Standard Python library for string manipulation.

## Usage

1. **Clone the repository:** Use Git or a similar tool to clone the repository to your local machine.
2. **Install Dependencies:** Run `pip install -r requirements.txt` to install the necessary Python packages.
3. **Running the Chatbot:** Launch the chatbot by running the main Python script (e.g., `app.py`) with a Python interpreter or within an environment that supports Python execution.
4. **Interact with TradingBot:** Start interacting with TradingBot by typing your stock market-related queries.

### ChatBot - Stock Market Knowledge Base

This chatbot is tailored to help users gain insights into the stock market, making it a useful tool for both beginners and those looking to expand their market knowledge.
