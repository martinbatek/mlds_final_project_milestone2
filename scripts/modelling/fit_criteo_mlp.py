# Define a 2 hidden layer Sequential model with dropout and batch normalization model for avazu
criteo_mlp = Sequential([
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

criteo_mlp.compile(loss=binary_crossentropy, optimizer=adam, metrics=[accuracy,auc])
criteo_mlp_hist = criteo_mlp.fit(
    criteo_train_tfd,
    batch_size=100,
    epochs=50,
    validation_data=criteo_val_tfd,
    verbose=False
)
# Save model
criteo_mlp.save('models/mlp/criteo_mlp.keras')

# Save hist object
with open('models/mlp/criteo_hist.json','w') as f:
    json.dump(criteo_mlp_hist.history,f)
f.close()