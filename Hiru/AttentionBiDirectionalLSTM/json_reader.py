import json

texts = []

with open('data/dailycoffeenews.json') as json_file:
    data = json.load(json_file)
    for article in data:
        text = "".join(article['text'])
        texts.append(text)


