# Define a 2 hidden layer Sequential model with dropout and batch normalization model for avazu
avazu_mlp = Sequential([
    Dense(128,activation='relu'),
    BatchNormalization(),
    Dropout(rate=0.7),
    Dense(64,activation='relu'),
    BatchNormalization(),
    Dropout(rate=0.7),
    Dense(32,activation='relu'),
    BatchNormalization(),
    Dropout(rate=0.7),
    Dense(1,activation='sigmoid')
])
adam = tf.keras.optimizers.Adam()
auc = tf.keras.metrics.AUC(name='auc')
accuracy = tf.keras.metrics.BinaryAccuracy(name='accuracy')
binary_crossentropy = tf.keras.losses.BinaryCrossentropy(name='log_loss')

avazu_mlp.compile(loss=binary_crossentropy, optimizer=adam, metrics=[accuracy,auc])
avazu_mlp_hist = avazu_mlp.fit(
    avazu_train_tfd,
    batch_size=100,
    epochs=50,
    validation_data=avazu_val_tfd,
    verbose=False
)
# Save model
avazu_mlp.save('models/mlp/avazu_mlp.keras')

# Save hist object
with open('models/mlp/avazu_hist.json','w') as f:
    json.dump(avazu_mlp_hist.history,f)
f.close()