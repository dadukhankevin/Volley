# Import necessary libraries
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.datasets import boston_housing

# Load the Boston Housing Prices dataset
(X_train, y_train), (X_test, y_test) = boston_housing.load_data()

# Standardize the data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Define a sequential model
model = Sequential()

# Add a single dense layer with one neuron (output) and input shape of 13 (number of features)
model.add(Dense(units=1, input_shape=(13,)))

# Compile the model with a mean squared error loss function and stochastic gradient descent optimizer
model.compile(optimizer='sgd', loss='mean_squared_error')

# Train the model on the training data
model.fit(X_train_scaled, y_train, epochs=100, verbose=0)

# Evaluate the model on the test data
loss = model.evaluate(X_test_scaled, y_test)
print(f"Test Loss: {loss}")

# Make predictions on new data
new_data = X_test_scaled[:2]  # Example: Using the first two instances from the test set
predictions = model.predict(new_data)

# Print the predictions
print("Predictions:")
print(predictions)
