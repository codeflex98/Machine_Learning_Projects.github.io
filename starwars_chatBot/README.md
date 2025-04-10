# Star Wars Chatbot

This project is a simple chatbot built using Python, Natural Language Processing (NLP), and deep learning techniques. It is designed to simulate a conversational agent themed around the Star Wars universe. The chatbot uses a JSON-based intent structure and a neural network to classify user input and generate contextually relevant responses.

## Features

- Intent classification using a neural network
- Preprocessing with tokenization and lemmatization (NLTK)
- Bag-of-words feature representation
- Themed response generation based on Star Wars characters and lore
- Model and metadata saving for reuse

## Project Structure

```
starwars_chatbot/
├── starwars_chatbot.ipynb   # Jupyter notebook containing the full implementation
├── starwarsintents.json     # Dataset of intents, patterns, and responses
├── chatbot_model.h5         # Trained model file (saved after execution)
├── words.pkl                # Preprocessed vocabulary (saved)
├── classes.pkl              # Encoded intent classes (saved)
├── README.md                # Project documentation
```

## Requirements

To run this project, make sure you have the following installed:

- Python 3.7+
- Jupyter Notebook
- NumPy
- TensorFlow
- NLTK

Install required Python packages:

```bash
pip install numpy nltk tensorflow
```

You will also need to download the following NLTK resources the first time you run the notebook:

```python
import nltk
nltk.download('punkt')
nltk.download('wordnet')
```

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/yourusername/starwars_chatbot.git
cd starwars_chatbot
```

2. Open the Jupyter Notebook:

```bash
jupyter notebook starwars_chatbot.ipynb
```

3. Run all cells in the notebook to:
   - Load and process the intents
   - Train the chatbot model
   - Save the trained model and metadata
   - Start chatting with the bot

4. At the end of the notebook, use the `chat()` or `chatbot_response()` functions to interact with the chatbot.

## Data Format

The `starwarsintents.json` file defines different intents and includes example input patterns and responses:

```json
{
  "intents": [
    {
      "tag": "greeting",
      "patterns": ["Hi", "Hello", "Hey"],
      "responses": ["Hello there!", "Greetings, young Jedi."]
    },
    ...
  ]
}
```

## Sample Interaction

```
User: Hello
Bot: Greetings, young Jedi.

User: Who is Darth Vader?
Bot: Darth Vader was a Dark Lord of the Sith and once a Jedi Knight named Anakin Skywalker.
```

## Future Improvements

- Enhance the model using LSTM or Transformer architecture
- Expand the dataset with more characters and responses
- Develop a web-based interface using Flask or Streamlit
