# Setup
Install dependencies and download data for libraries used.
```
pip install -r requirements.txt
python3 -m csa.setup
python3 -m textblob.download_corpora

```

# Usage

```
usage: csa_main.py [-h] -i INPUT_FILE -o OUTPUT_FILE   

Cryto sentiment analyzer

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT_FILE, --input_file INPUT_FILE
                        Path to raw chat data file     
  -o OUTPUT_FILE, --output_file OUTPUT_FILE
                        Path to output data file
```

Example

```
python3 ./src/main.py -i ./data/chat_data.json -o ./data/chat_sentiment_data.json
```

This will read chat data from `./data/chat_data.json` and write chat data with sentiments to `./data/chat_sentiment_data.json`.

# Brief description

## Data
- [Chat data from May 1 to May 15 2021](/data/chat_data.json), was downloaded in json fromat from the CryptoComOfficial telegram channel.
### Structure ([structure.py](/src/csa/structure.py))
- Messages had a text field which was a string when the message was simple.
- When the message had other elements, like links or styling, it was a list of dictionaries/strings having text and type fields.
- The nesting was removed by stitching together text fields from each of the dictionaries.

Messages statistics

```
Total number of messages: 49436
Number of nested_messages: 4654
Number of normal_messages: 44782
```

Different types of styling
```
{'bold', 'link', 'phone', 'hashtag', 'mention', 'cashtag', 'bot_command', 
'code', 'pre', 'text_link', 'underline', 'email', 'italic', 'mention_name'}
```
### Filtering ([filter.py](/src/csa/filter.py))
- Messages were filtered by removing all messages that were not in English.
- Among these messages, only the ones with `shib` or `doge` were selected.

### Cleaning ([clean.py](/src/csa/clean.py))
- Messages were cleaned by removing all non alphanumeric characters and stopwords.
- nltk's corpus of English stopwords was used.

#### Detecting english
- For detecting whether a message is in English or not, the percentage of English words in the message was calculated.
- If this was greater than a threshold, the message was considered to be in English.
- nltk's corpus of English words was used as the vocabulary.

## Sentiment analysis ([sentiment.py](/src/csa/sentiment.py))
- Textblob library was used to compute the sentiment of each message.
- This library provides a very straightforward interface for sentiment analysis.
- It supports couple of techniques for sentiment analysis - PatternAnalyzer, NaiveBayesAnalyzer.
- Tried both of them and found both of them to be making a few errors.
- PatternAnalyzer seems to give a lot more 0.0 values for sentiment polarity.
- The current result shown in the plot was computed using NaiveBayesAnalyzer.
- Better libraries/methods for sentiment analysis could be used.
- Training a simple classifier on some data from this domain might yield better results.

## Plots ([plot.ipynb](/src/plot.ipynb))

- Used pandas to aggregate the data and plotly express to plot the bar charts.
- Ignored 0.0 polarity while computing average sentiment.

| Number of messages per day | Average sentiment per day |
| ---------------------------| ------------------------- |
|![messages per day](/plots/messages_per_day.png)|![average sentiment per day](/plots/sentiment_per_day.png)|
