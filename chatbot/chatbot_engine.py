# chatbot_engine.py

import random
import nltk
import string
from textblob import TextBlob
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Ensure necessary NLTK packages are downloaded
nltk.download('punkt')
nltk.download('wordnet')

class Chatbot:
    def __init__(self, corpus_filename):
        try:
            with open(corpus_filename, 'r', errors='ignore') as file:
                raw = file.read().lower()
            self.sent_tokens = nltk.sent_tokenize(raw)
        except FileNotFoundError:
            print(f"Error: The file '{corpus_filename}' was not found.")
            self.sent_tokens = []

        self.lemmer = nltk.stem.WordNetLemmatizer()

        # Expanded Dictionary of greetings and responses
        self.greetings = {
            "hello": ["Hi there!", "Hello!", "Greetings!"],
            "what is your name": ["Hi there!, I am your Trading ChatBot"],
            "Who is pukar sharma": ["Pukar Sharma is the founder of Trading ChatBot"],
            "pukar sharma ": ["Pukar Sharma is the founder of Trading ChatBot"],
            "hi": ["Hello!", "Hey there!", "Hi!"],
            "hey": ["Hey!", "Hey there!", "Hi!"],
            "how are you": ["I'm doing well, thank you!", "Good, thanks for asking!", "I'm fine, and you?"],
            "what's up": ["Not much, you?", "Just chatting here!", "The usual stuff."],
            "good morning": ["Good morning!", "A bright day ahead!", "Morning!"],
            "good evening": ["Good evening!", "Hope you're having a nice evening!", "Evening!"],
            "good night": ["Good night!", "Sweet dreams!", "Have a good sleep!"],

            # Nepali Romanized Greetings
            "nameste": ["Namaste!", "Namaskar!", "Namaste. Kasto chha?"],
            "k cha": ["Thik cha, tapai?", "Sab thikai cha", "Ramro cha, dhanyabaad!"],
            "sanchai chha": ["Sanchai chhu, tapaini?", "Hajur, sanchai chhu.", "Sabai ramro chha, dhanyabaad!"],
            "ramro chha": ["Dhanyabaad!", "Hajur, ramro chha."],
            "subha prabhat": ["Subha prabhat!", "Bihaan ko ramro suruwaat!", "Shubha bihaani!"],
            "subha sandhya": ["Subha sandhya!", "Sandhya ko ramailo!", "Ramro sandhya hos!"],
        }

    def lem_normalize(self, text):
        remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
        return [self.lemmer.lemmatize(token) for token in nltk.word_tokenize(text.lower().translate(remove_punct_dict))]

    def greet(self, user_response):
        for greeting in self.greetings:
            if greeting in user_response:
                return random.choice(self.greetings[greeting])
        return None

    def analyze_sentiment(self, sentence):
        analysis = TextBlob(sentence)
        if analysis.sentiment.polarity > 0.1:
            return "It sounds like you're in a good mood today!"
        elif analysis.sentiment.polarity < -0.1:
            return "I'm sensing some negativity. Is everything okay?"
        return None

    def response(self, user_response):
        user_response = user_response.lower()
        
        # Check for a greeting and analyze sentiment
        greeting_response = self.greet(user_response)
        sentiment_response = self.analyze_sentiment(user_response)
        if greeting_response:
            return f"{greeting_response}\n{sentiment_response if sentiment_response else ''}".strip()

        # TF-IDF based response
        self.sent_tokens.append(user_response)
        TfidfVec = TfidfVectorizer(tokenizer=self.lem_normalize, stop_words='english')
        tfidf = TfidfVec.fit_transform(self.sent_tokens)
        vals = cosine_similarity(tfidf[-1], tfidf)
        idx = vals.argsort()[0][-2]
        flat = vals.flatten()
        flat.sort()
        req_tfidf = flat[-2]
        self.sent_tokens.remove(user_response)

        if req_tfidf == 0:
            return "I am sorry! I don't understand you."
        else:
            return self.sent_tokens[idx]

# Example usage:
# chatbot = Chatbot("path/to/your/knowledge_base.txt")
# print(chatbot.response("hello"))
