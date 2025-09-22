# AI-CHATBOT-WITH-NLP

COMPANY: CODTECH IT SOLUTIONS

NAME: ANGELIN SHERIN P

INTERN ID: CT04DY2758

DOMAIN: Python programming

DURATION : 4 WEEKS

MENTOR: NEELA SANTHOSH

Project Overview

This project brings lightweight AI chatbot built using Python and NLP techniques.it is designed to assist users by responding to queries based on a predefined knowledge base. What makes this chatbot special is its ability to talk not only about Python programming, natural language processing, and chatbots, but also answer basic chemistry-related questions.

The chatbot uses TF-IDF vectorization and cosine similarity from the scikit-learn library to semantically match user questions with answers from its internal corpus. It also utilizes spaCy, a popular NLP library, to handle natural language understanding tasks. The project is designed for educational use — ideal for those exploring how to build custom chatbots, combine domains like chemistry and programming, and apply machine learning concepts to conversational AI.

Technologies Used

Python 3: The core language used to develop the chatbot. spaCy: Used for text processing and language modeling. scikit-learn: Utilized for TF-IDF vectorization and cosine similarity calculations. random: For generating dynamic fallback and greeting responses. Jupyter Notebook / Google Colab: Ideal platforms for running and testing the chatbot interactively. Key Features

Knowledge Domains:

Programming: ai knows about Python, its syntax, history, paradigms, and more. Artificial Intelligence & NLP: Understands basic concepts of AI and natural language processing. Chemistry: Answers fundamental questions about atoms, molecules, pH, acids, the periodic table, and more. Greeting Recognition: Detects and responds to common greetings like “hi”, “hello”, and “hey”.

Fallback Responses: When the chatbot doesn't understand a query, it responds with friendly fallback messages, prompting the user to rephrase.

Simple, Modular Design: Easy to extend the knowledge base with more domains or deeper content.

Text Matching via TF-IDF: Uses vector similarity rather than keyword matching, offering more flexibility and intelligent responses.

Workflow

User input is taken in a loop (via command line or notebook). Greeting check: If the input is a greeting, Bujji returns a random greeting response. Semantic matching: If not a greeting, the input is compared to all knowledge base entries using TF-IDF and cosine similarity. Best match: If similarity is high enough (threshold = 0.3), the most relevant answer is returned. Fallback logic: If the confidence is low, Bujji responds with a polite fallback suggestion. This loop continues until the user types bye, quit, or exit. Use Cases

Teaching beginners how chatbots work. Demonstrating semantic search using TF-IDF and cosine similarity. Combining domain knowledge (e.g., chemistry + AI) in a chatbot. Academic assignments and educational projects in AI/NLP. Lightweight alternatives to heavy chatbot frameworks. Customization Ideas

Add more knowledge domains like biology, history, or math. Integrate speech-to-text and text-to-speech for voice interaction. Add a GUI using Tkinter or a web interface using Flask. Train it on external documents or a custom dataset. Improve NLU with spaCy’s named entity recognition (NER) and dependency parsing. How to Use

Install dependencies: pip install spacy scikit-learn python -m spacy download en_core_web_sm Run the script in a Python environment or notebook. Type your queries interactively. Try: “What is Python?” “Tell me about atoms.” “What is pH?” “Explain chatbots.” Type bye to exit the conversation.

OUTPUT

<img width="1353" height="461" alt="Image" src="https://github.com/user-attachments/assets/0b88538c-bc06-4f91-84b8-3ea602b4543a" />
