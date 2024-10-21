import tensorflow as tf
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('housepricedata.csv')
print(df.head())

# Prepare the data
dataset = df.values
X = dataset[:, 0:10]  # Features
Y = dataset[:, 10]     # Target variable

# Scale the features
min_max_scaler = preprocessing.MinMaxScaler()
X_scale = min_max_scaler.fit_transform(X)
print(X_scale)

# Split the dataset
X_train, X_val_and_test, Y_train, Y_val_and_test = train_test_split(X_scale, Y, test_size=0.3)
X_val, X_test, Y_val, Y_test = train_test_split(X_val_and_test, Y_val_and_test, test_size=0.5)
print(X_train.shape, X_val.shape, X_test.shape, Y_train.shape, Y_val.shape, Y_test.shape)

# Build the model
model = Sequential([
    Dense(32, activation='relu', input_shape=(10,)),
    Dense(32, activation='relu'),
    Dense(1, activation='linear'),  # Use linear activation for regression
])

# Compile the model
model.compile(optimizer='sgd', loss='mean_squared_error', metrics=['mae'])  # Use MSE for regression

# Train the model
hist = model.fit(X_train, Y_train, batch_size=32, epochs=100, validation_data=(X_val, Y_val))

# Evaluate the model
test_loss, test_mae = model.evaluate(X_test, Y_test)
print(f'Test MAE: {test_mae}')

# Plotting training and validation loss
plt.plot(hist.history['loss'], label='Train Loss')
plt.plot(hist.history['val_loss'], label='Validation Loss')
plt.title('Model Loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(loc='upper right')
plt.show()

# Optionally plot MAE as well if needed
plt.plot(hist.history['mae'], label='Train MAE')
plt.plot(hist.history['val_mae'], label='Validation MAE')
plt.title('Model MAE')
plt.ylabel('MAE')
plt.xlabel('Epoch')
plt.legend(loc='upper right')
plt.show()
