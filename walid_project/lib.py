import requests


def try_me():
    return print('Décollage immédiat')


def weather(ville):
    response = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?q={ville}&appid=dae9a5019961ec753439f157ed0e1221'
    ).json()
    c = response['main']['temp'] - 273.15

    return c



from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
from gensim.models import Word2Vec



# Function to convert a sentence (list of words) into a matrix representing the words in the embedding space
def embed_sentence(word2vec, sentence):
    word2vec = Word2Vec(sentences=X_train)

    embedded_sentence = []
    for word in sentence:
        if word in word2vec.wv:
            embedded_sentence.append(word2vec.wv[word])

    return np.array(embedded_sentence)


# Function that converts a list of sentences into a list of matrices
def embedding(word2vec, sentences):
    embed = []

    for sentence in sentences:
        embedded_sentence = embed_sentence(word2vec, sentence)
        embed.append(embedded_sentence)

    return embed


def x_pad () :
    X_train_embed = embedding(word2vec, X_train)
    X_test_embed = embedding(word2vec, X_test)

    X_train_pad = pad_sequences(X_train_embed,
                            dtype='float32',
                            padding='post',
                            maxlen=200)
    X_test_pad = pad_sequences(X_test_embed,
                           dtype='float32',
                           padding='post',
                           maxlen=200)
    return X_train_pad, X_test_pad
