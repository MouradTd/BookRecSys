# import math
# import pandas as pd
# from surprise import Dataset, Reader, SVD 
# from surprise.model_selection import train_test_split
# from surprise.accuracy import rmse ,mae
# import pickle

# # Load the dataset
# data = pd.read_csv('Fixed_Books.csv')
# data.columns = data.columns.str.strip()
# # Define the Reader object
# reader = Reader(rating_scale=(1, 5))
# print(data.columns)
# # Load the dataset into Surprise's Dataset object
# star_rating_mapping = {
#     'One': 1,
#     'Two': 2,
#     'Three': 3,
#     'Four': 4,
#     'Five': 5
# }

# data['Price'] = data['Price'].str.replace('£', '').astype(float)
# # Remove Space characters
# data['Star rating'] = data['Star rating'].str.strip()  
# data['Star rating'] = data['Star rating'].map(star_rating_mapping)

# dataset = Dataset.load_from_df(data, reader)

# # Split the data into training and testing sets
# trainset, testset = train_test_split(dataset, test_size=0.2, random_state=42)

# # Initialize the SVD algorithm
# model = SVD()

# # Train the model
# model.fit(trainset)
# # dump.dump('svd_model.pkl', model)
# filename = 'svd_model.pkl'
# pickle.dump(model, open(filename, 'wb'))


# # Make predictions on the test set
# predictions = model.test(testset)

# # Filter out predictions with nan true ratings
# filtered_predictions = [pred for pred in predictions if not math.isnan(pred.r_ui)]

# # Calculate RMSE (Root Mean Squared Error)
# accuracy = rmse(filtered_predictions)
# # Calculate MAE
# mae = mae(predictions)
# print('RMSE:', accuracy)


import math
import pandas as pd
from surprise import Dataset, Reader, SVD 
from surprise.model_selection import train_test_split
from surprise.accuracy import rmse, mae
import pickle

# Load the dataset
data = pd.read_csv('Fixed_Books.csv')
data.columns = data.columns.str.strip()

# Define the Reader object
reader = Reader(rating_scale=(1, 5))

# Load the dataset into Surprise's Dataset object
star_rating_mapping = {
    'One': 1,
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5
}

# Preprocessing steps
data['Price'] = data['Price'].str.replace('£', '').astype(float)
data['Star rating'] = data['Star rating'].str.strip()  
data['Star rating'] = data['Star rating'].map(star_rating_mapping)

# Select only the relevant columns
data = data[['User', 'Price', 'Star rating']]

# Load the dataset into Surprise's Dataset object
dataset = Dataset.load_from_df(data, reader)


# Split the data into training and testing sets
trainset, testset = train_test_split(dataset, test_size=0.2, random_state=42)

# Initialize the SVD algorithm
model = SVD()

# Train the model
model.fit(trainset)

# Save the model
filename = 'svd_model.pkl'
pickle.dump(model, open(filename, 'wb'))

# Make predictions on the test set
predictions = model.test(testset)

# Filter out predictions with nan true ratings
filtered_predictions = [pred for pred in predictions if not math.isnan(pred.r_ui)]

# Calculate RMSE (Root Mean Squared Error)
accuracy = rmse(filtered_predictions)

# Calculate MAE
mae = mae(predictions)
print('RMSE:', accuracy)

