import tensorflow as tf
from keras import layers, Input, Model
from keras.callbacks import EarlyStopping
from keras.layers import multiply, Embedding, Bidirectional, LSTM, Dense, Flatten, Activation, RepeatVector, Permute, K
from keras.optimizers import Adam
from keras_preprocessing import sequence
from keras_preprocessing.text import Tokenizer
import imdb

imdb.maybe_download_and_extract()

vocab_size = 20000

x_train, y_train = imdb.load_data(train=True)
x_test, y_test = imdb.load_data(train=False)

data_text = x_train + x_test

# ####################### CHANGE TO GLOVE ##########################
tokenizer = Tokenizer(num_words=vocab_size)
tokenizer.fit_on_texts(data_text)

# integer encode the documents
x_train = tokenizer.texts_to_sequences(x_train)
x_test = tokenizer.texts_to_sequences(x_test)

# pad documents to a max length of 500 words
max_len = 500
rnn_cell_size = 128

pad_type = 'pre'

x_train = sequence.pad_sequences(x_train, maxlen=max_len, truncating=pad_type, padding=pad_type)
x_test = sequence.pad_sequences(x_test, maxlen=max_len, truncating=pad_type, padding=pad_type)

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
                    validation_split=0.05, verbose=1, callbacks=[early_stopping_callback])

model.save('attention_weights.h5')
