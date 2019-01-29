import tensorflow as tf
from keras import layers, Input, Model
from keras.backend import zeros
from keras.callbacks import EarlyStopping
from keras.layers import multiply, Embedding, Bidirectional, LSTM, Dense, Flatten, Activation, RepeatVector, Permute, K, \
    np
from keras.optimizers import Adam
from keras_preprocessing import sequence
from keras_preprocessing.text import Tokenizer
from numpy import asarray

vocab_size = 20000

pad_id = 0
start_id = 1
oov_id = 2
index_offset = 2

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.imdb.load_data(num_words=vocab_size, start_char=start_id,
                                                                        oov_char=oov_id, index_from=index_offset)
print(x_train[1])
data_text = x_train + x_test

####################### CHANGE TO GLOVE ##########################
word2idx = tf.keras.datasets.imdb.get_word_index()

idx2word = {v + index_offset: k for k, v in word2idx.items()}

idx2word[pad_id] = '<PAD>'
idx2word[start_id] = '<START>'
idx2word[oov_id] = '<OOV>'

max_len = 250
rnn_cell_size = 512

pad_type = 'pre'

x_train = sequence.pad_sequences(x_train, maxlen=max_len, truncating=pad_type, padding=pad_type, value=pad_id)
x_test = sequence.pad_sequences(x_test, maxlen=max_len, truncating=pad_type, padding=pad_type, value=pad_id)

####################### CHANGE TO GLOVE ##########################

# tokenizer = Tokenizer()
# tokenizer.fit_on_texts(data_text)
#
# if vocab_size is None:
#     vocab_size = len(tokenizer.word_index) + 1
#
# # integer encode the documents
# x_train = tokenizer.texts_to_sequences(x_train)
# x_test = tokenizer.texts_to_sequences(x_test)
#
# # pad documents to a max length of 250 words
# max_len = 250
# rnn_cell_size = 128
#
# pad_type = 'pre'
#
# x_train = sequence.pad_sequences(x_train, maxlen=max_len, truncating=pad_type, padding=pad_type, value=pad_id)
# x_test = sequence.pad_sequences(x_test, maxlen=max_len, truncating=pad_type, padding=pad_type, value=pad_id)
#
# embeddings_index = dict()
# f = open('glove.6B.100d.txt')
# for line in f:
#     values = line.split()
#     word = values[0]
#     coefs = tf.convert_to_tensor(asarray(values[1:], dtype='float32'), dtype='float32')
#     embeddings_index[word] = coefs
# f.close()
# print('Loaded %s word vectors.' % len(embeddings_index))
#
# # create a weight matrix for words in training docs
# embedding_matrix = zeros((vocab_size, 100))
# for word, i in tokenizer.word_index.items():
#     embedding_vector = embeddings_index.get(word)
#     if embedding_vector is not None:
#         embedding_matrix[i] = embedding_vector


###################################################################

sequence_input = Input(shape=(max_len,), dtype='int32')

embedded_sequences = Embedding(vocab_size, 512, input_length=max_len)(sequence_input)

# Attention layer
units = 64
activations = Bidirectional(LSTM(units, return_sequences=True, dropout=0.2, recurrent_dropout=0.2))(embedded_sequences)

attention = Dense(1, activation='tanh')(activations)
attention = Flatten()(attention)
attention = Activation('softmax')(attention)
attention = RepeatVector(units*2)(attention)
attention = Permute([2, 1])(attention)

sent_representation = multiply([activations, attention])
sent_representation = layers.Lambda(lambda xin: K.sum(xin, axis=-2), output_shape=(units*2,))(sent_representation)

output_layer = Dense(1, activation='sigmoid')(sent_representation)

model = Model(inputs=sequence_input, outputs=output_layer)

print(model.summary())

# Compile the model
model.compile(optimizer=Adam(lr=8e-04, beta_1=0.9, beta_2=0.999, epsilon=None, decay=0.0, amsgrad=False),
              loss='binary_crossentropy',
              metrics=['accuracy'])

early_stopping_callback = EarlyStopping(monitor='val_loss', min_delta=0, patience=1, verbose=0, mode='auto')

history = model.fit(x_train,
                    y_train,
                    epochs=10,
                    batch_size=200,
                    validation_split=.3, verbose=1, callbacks=[early_stopping_callback])

model.save('attention_weights.h5')

# 5 fold cross validation