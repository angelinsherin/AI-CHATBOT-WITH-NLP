!pip install -q spacy scikit-learn
!python -m spacy download en_core_web_sm


import spacy
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


nlp = spacy.load("en_core_web_sm")


corpus = [
    # Python & AI
    "Python is a popular programming language used for web development, data analysis, AI, and automation.",
    "Python is known for its readability and simplicity.",
    "Python was created by Guido van Rossum and released in 1991.",
    "Python supports multiple programming paradigms, including procedural, object-oriented, and functional programming.",
    "NLP stands for Natural Language Processing, a field of AI that focuses on understanding human language.",
    "NLP is used in chatbots, translation apps, sentiment analysis, and more.",
    "Chatbots are software applications that simulate conversation with users.",
    "Chatbots work by processing user input and generating appropriate responses.",
    "Rule-based chatbots follow fixed scripts while AI-powered ones learn from data.",
    "The main purpose of chatbots is to assist users and provide quick information.",
    "I can help you learn about Python, NLP, and how chatbots work.",
    "Ask me anything related to Python programming or artificial intelligence.",

    " I’m a simple chatbot designed to help you.",
    "I am your friendly assistant. Ask me anything from my knowledge base.",
    "You're welcome. I'm always here to help.",
    "Goodbye. It was nice chatting with you.",

    "Water is a compound made of two hydrogen atoms and one oxygen atom. Its chemical formula is H2O.",
    "Atoms are the basic building blocks of matter, made up of protons, neutrons, and electrons.",
    "The periodic table organizes chemical elements based on their atomic number and properties.",
    "An acid is a substance that donates protons (H+ ions) in a solution. A base accepts protons.",
    "pH is a scale used to measure how acidic or basic a solution is. 7 is neutral, below 7 is acidic, above 7 is basic.",
    "Carbon is a unique element that forms the backbone of organic molecules. It can form 4 covalent bonds.",
    "Chemical reactions involve the breaking and forming of bonds, and are represented by chemical equations.",
    "The atomic number of an element is the number of protons in its nucleus.",
    "Electrons are negatively charged particles that orbit the nucleus in energy levels or shells.",
    "A molecule is formed when two or more atoms bond together chemically.",
]


GREETING_INPUTS = ("hello", "hi", "hey", "greetings", "yo")
GREETING_RESPONSES = [
    "Hi there! How can I help?",
    "Hello! What would you like to ask?",
    "Hey! I'm Bujji. Ask me anything.",
]

FALLBACK_RESPONSES = [
    "Hmm, I’m not sure about that. Can you ask in another way?",
    "That’s a bit outside my knowledge. Try rephrasing?",
    "I didn’t get that fully. Can you clarify?",
]


vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)


def get_bujji_response(user_input):
    input_vec = vectorizer.transform([user_input])
    sim_scores = cosine_similarity(input_vec, X)
    max_score = sim_scores.max()
    if max_score < 0.3:
        return random.choice(FALLBACK_RESPONSES)
    else:
        index = sim_scores.argmax()
        return corpus[index]

def is_greeting(text):
    for word in text.lower().split():
        if word in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)
    return None

def chat():
    print(" Hi! I’m your chatbot. Ask me anything. (Type 'bye' to exit.)")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "exit", "quit"]:
            print( "Bye! Take care.")
            break
        response = is_greeting(user_input)
        if response:
            print(" response)
        else:
            print(":", get_bujji_response(user_input))

chat()
