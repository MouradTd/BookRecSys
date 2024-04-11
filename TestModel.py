from surprise import dump 
import pickle

# Load the model from the file
loaded_model = pickle.load(open('svd_model.pkl', 'rb'))

# Ask the user for their ID
user_id = input("Entrer votre Matricule : ")

# Ask the user for a list of books
books = input("Entrer le titre des Livres : ").split(',')

# Make predictions
for book in books:
    book = book.strip()  # Remove leading and trailing whitespace
    prediction = loaded_model.predict(user_id, book)
    print('Book:', prediction.iid, 'Estimated rating:', prediction.est)