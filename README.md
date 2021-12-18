# Setup
Install dependencies and download data for libraries used.
```
pip install requirements.txt
python3 setup.py
python3 -m textblob.download_corpora
```

# Usage

```
python3 src/csa_main.py data
```

# Brief description

## Data
- [Chat data from May 1 to May 15 2021](/data/chat_data.json), was downloaded in json fromat from the CryptoComOfficial telegram channel.
### Structure ([csa_structure.py](/src/csa_structure.py))
- Messages had a text field that was a string when the message was simple.
- When the message had other elements, like links or styling, it was a list of dictionaries/strings having a text and type fields.
- The nesting was removed by taking the text fields from each of the dictionaries and stitching them together.

Messages statistics

```
Total number of messages: 49436
Number of nested_messages: 4654
Number of normal_messages: 44782
```

Different types of styling
```
{'bold', 'link', 'phone', 'hashtag', 'mention',
    'cashtag', 'bot_command', 'code', 'pre', 'text_link',
    'underline', 'email', 'italic', 'mention_name'}
```
### Filtering ([csa_filter.py](/src/csa_filter.py))
- Messages were filtered by removing all messages that were not in English.
- Among these messages, only the ones with `shib` or `doge` were selected.
#### Detecting english
- For detecting whether a sentence is in English or not, the percentage of English words in the sentence was calculated.
- If this was greater than a threshold, the sentence was considered to be English.
- nltk's corpus of English words was used as the vocabulary.

## Sentiment analysis ([csa_sentiment.py](/src/csa_sentiment.py))
- Textblob library was used to compute the sentiment of each message.

## Plots ([csa_plot.ipynb](/src/csa_plot.ipynb))

- Used pandas to aggregate the data and plotly express to plot the bar charts.

| Number of messages per day | Average sentiment per day |
| ---------------------------| ------------------------- |
|![messages per day](/plots/messages_per_day.png)|![average sentiment per day](/plots/sentiment_per_day.png)|