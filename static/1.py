import tensorflow as tf
from tensorflow import keras
import numpy as np
import pandas as pd

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
model = tf.keras.models.load_model('model.h5')


data = pd.read_csv('sentences.csv')
max_length = 100
training_size = 20000
gap = data['sentence']
label = data['label']
training_sentences = gap[0:training_size]
tokenizer = Tokenizer(num_words=30000, oov_token='<OOV>')
tokenizer.fit_on_texts(training_sentences)
redict = ["She eats noodles every Sunday."]
training_sequences = tokenizer.texts_to_sequences(redict)
training_padded = pad_sequences(training_sequences, maxlen=100, padding='post', truncating='post')
testss = np.array(training_padded)
print(model.predict(testss))

