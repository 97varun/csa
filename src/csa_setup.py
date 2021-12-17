import nltk


def setup_nltk_corpus():
    nltk.download('words')
    nltk.download('stopwords')


if __name__ == '__main__':
    setup_nltk_corpus()
