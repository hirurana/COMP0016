import json

import numpy as np
import imdb
from keras.models import load_model
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

imdb.maybe_download_and_extract()

# Max number of tokens allowed to be created
vocab_size = 20000
# max length of each text analysed
max_length = 500

x_train, y_train = imdb.load_data(train=True)
x_test, y_test = imdb.load_data(train=False)

data_text = x_train + x_test

# Set up tokenizer
tokenizer = Tokenizer(num_words=vocab_size)
tokenizer.fit_on_texts(data_text)

# integer encode the documents
x_train = tokenizer.texts_to_sequences(x_train)
x_test = tokenizer.texts_to_sequences(x_test)

# pad documents to a max length of 500 words
max_len = 500
rnn_cell_size = 128

pad_type = 'pre'


# Load model
print("Loading model...")
model = load_model('attention_weights.h5')


# read JSON file and store text as an array
texts = []
print("Reading JSON file...")
with open('data/perfectdailygrind.json') as json_file:
    data = json.load(json_file)
    for article in data:
        text = "".join(article['text'])
        texts.append(text)

print("Performing sentiment analysis...")
tokens = tokenizer.texts_to_sequences(texts)
tokens_pad = pad_sequences(tokens, maxlen=max_length, padding=pad_type, truncating=pad_type)
result = model.predict(tokens_pad)
result = np.array(result).tolist()

print("Cleaning results...")
cleaned_results = []
for i in result:
    data_point = i[0]-0.3
    if data_point < 0:
        data_point += 0.3
    cleaned_results.append(data_point)

print("Storing results...")
for article in data:
    article['sentiment'] = cleaned_results[data.index(article)]

with open('data/perfectdailygrind_with_sentiment.json', 'w') as output:
    json.dump(data, output)
print("Done")

