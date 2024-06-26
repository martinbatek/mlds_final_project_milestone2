# Define a 2 hidden layer Sequential model with dropout and batch normalization model for kdd12
kdd12_mlp = Sequential([
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

kdd12_mlp.compile(loss=binary_crossentropy, optimizer=adam, metrics=[accuracy,auc])
kdd12_mlp_hist = kdd12_mlp.fit(
    kdd12_train_tfd,
    batch_size=100,
    epochs=50,
    validation_data=kdd12_val_tfd,
    verbose=False
)
# Print summary of the MLP Model
print(kdd12_mlp.summary())

# Save model
kdd12_mlp.save('models/mlp/kdd12_mlp.keras')

# Save hist object
with open('models/mlp/kdd12_hist.json','w') as f:
    json.dump(kdd12_mlp_hist.history,f)
f.close()