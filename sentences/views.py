from django.shortcuts import render
from .forms import Sentences
import tensorflow as tf
from tensorflow import keras
import numpy as np
import pandas as pd



from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
model = tf.keras.models.load_model('./static/model.h5')
data = pd.read_csv('./static/sentences.csv')
max_length = 100
training_size = 20000
gap = data['sentence']
label = data['label']
training_sentences = gap[0:training_size]
tokenizer = Tokenizer(num_words=30000, oov_token='<OOV>')
tokenizer.fit_on_texts(training_sentences)

# Create your views here.

def taqvim(request):
    if request.method == 'POST':
        form = Sentences(request.POST)
        if form.is_valid():
            text = form.cleaned_data['name']
            redict = [text]
            training_sequences = tokenizer.texts_to_sequences(redict)
            training_padded = pad_sequences(training_sequences, maxlen=100, padding='post', truncating='post')
            testss = np.array(training_padded)
            predict =model.predict(testss)
            text = predict[0][0]
            foiz = round(predict[0][0], 2)
            print(predict[0][0])
            return render(request, 'sentences.html', {'text': text, 'foiz':int(foiz*100),'form': form})

    else:
        form = Sentences()
    return render(request, 'sentences.html', {'form': form})