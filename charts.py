import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data from the CSV file
df = pd.read_csv('Fixed_Books.csv')

# Remove leading and trailing whitespace from column names
df.columns = df.columns.str.strip()

# Extracting book titles and prices
book_titles = df['"Book title"']
# Clean the 'Price' column to remove non-numeric characters
df['Price'] = df['Price'].str.replace('£', '').astype(float)

# 1. Bar chart - Top 10 most expensive books
top_10_expensive_books = df.nlargest(10, 'Price')
plt.figure(figsize=(10, 4))
sns.barplot(x='Price', y='"Book title"', data=top_10_expensive_books, palette='viridis')
plt.title('Top 10 Most Expensive Books')
plt.xlabel('Price (£)')
plt.ylabel('Book Title')
plt.show()

# 2. Histogram - Distribution of book prices
plt.figure(figsize=(10, 6))
sns.histplot(df['Price'], bins=20, kde=True, color='skyblue')
plt.title('Distribution of Book Prices')
plt.xlabel('Price (£)')
plt.ylabel('Frequency')
plt.show()

# 3. Pie chart - Percentage of books in different price ranges
price_ranges = pd.cut(df['Price'], bins=[0, 20, 40, 60, 80], labels=['£0-£20', '£20-£40', '£40-£60', '£60+'])
price_range_counts = price_ranges.value_counts()
plt.figure(figsize=(8, 8))
plt.pie(price_range_counts, labels=price_range_counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
plt.title('Percentage of Books in Different Price Ranges')
plt.axis('equal')
plt.show()

# 4. Box plot - Distribution of book prices and detecting outliers
plt.figure(figsize=(10, 6))
sns.boxplot(y=df['Price'], color='lightblue')
plt.title('Distribution of Book Prices')
plt.ylabel('Price (£)')
plt.show()

# Compter le nombre de livres dans chaque catégorie d'évaluation
star_rating_counts = df['Star rating'].value_counts()

# Créer un diagramme à barres de la répartition des évaluations en étoiles
plt.figure(figsize=(10, 6))
star_rating_counts.plot(kind='bar', color='lightblue')
plt.title('Distribution of Star Ratings')
plt.xlabel('Star Rating')
plt.ylabel('Number of Books')
plt.show()