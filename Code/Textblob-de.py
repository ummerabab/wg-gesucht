import pandas as pd
from textblob_de import TextBlobDE as TextBlob

df = pd.read_csv('dataset_P+R.csv', sep=',')
text = df['WG-Leben']
text = df['Lage']
text = df['Sonstiges']

sentiment = []
sentiment_temp = []
result = []


def Average(lst):
    return sum(lst) / len(lst)


def main():
    for elem in text:
        blob = TextBlob(elem)
        for sentence in blob.sentences:
            sentiment_temp.append(sentence.sentiment.polarity)
        sentiment = Average(sentiment_temp)
        result.append(sentiment)

    df['Sentiment'] = result
    df.to_csv("./sentiment.csv", sep=',', index=False)


if __name__ == "__main__":
    main()