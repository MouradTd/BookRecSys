import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.manifold import LocallyLinearEmbedding, TSNE
from sklearn.preprocessing import LabelEncoder

# One column Price

# Load the data from the CSV file
df = pd.read_csv('Fixed_Books.csv')
df.columns = df.columns.str.strip()

# Extracting book titles, prices, and star ratings
book_titles = df['"Book title"']
book_prices = df['Price'].str.replace('£', '').str.strip().astype(float)
star_ratings = df['Star rating']

# Encode star ratings into numerical values
label_encoder = LabelEncoder()
star_ratings_encoded = label_encoder.fit_transform(star_ratings)

# Combine prices and star ratings into a single feature
features = pd.concat([book_prices, pd.Series(star_ratings_encoded, name='Star rating')], axis=1)

# Apply PCA
pca = PCA(n_components=1)
pca_result = pca.fit_transform(features)

# Apply Locally Linear Embeddings
lle = LocallyLinearEmbedding(n_components=1, n_neighbors=7)
lle_result = lle.fit_transform(features)

# Apply t-SNE
tsne = TSNE(n_components=1, perplexity=15)
tsne_result = tsne.fit_transform(features)

# Plot the results
plt.figure(figsize=(16, 6))

plt.subplot(1, 3, 1)
plt.scatter(pca_result[:, 0], [0] * len(pca_result), c=book_prices, cmap='viridis')
plt.title('PCA')

plt.subplot(1, 3, 2)
plt.scatter(lle_result[:, 0], [0] * len(lle_result), c=book_prices, cmap='viridis')
plt.title('Locally Linear Embeddings')

plt.subplot(1, 3, 3)
plt.scatter(tsne_result[:, 0], [0] * len(tsne_result), c=book_prices, cmap='viridis')
plt.title('t-SNE')

plt.tight_layout()
plt.show()

# two columns Star rating and Price



# Encode star ratings into numerical values
label_encoder = LabelEncoder()
star_ratings_encoded = label_encoder.fit_transform(star_ratings)

# Combine prices and star ratings into a single feature matrix
X = pd.concat([book_prices, pd.Series(star_ratings_encoded, name='Star rating')], axis=1)

# Apply PCA
pca = PCA(n_components=2)
pca_result = pca.fit_transform(X)

# Apply Locally Linear Embeddings
lle = LocallyLinearEmbedding(n_components=2, n_neighbors=7)
lle_result = lle.fit_transform(X)

# Apply t-SNE
tsne = TSNE(n_components=2, perplexity=15)
tsne_result = tsne.fit_transform(X)

# Plot the results
plt.figure(figsize=(16, 6))

plt.subplot(1, 3, 1)
plt.scatter(pca_result[:, 0], pca_result[:, 1], c=book_prices, cmap='viridis')
plt.title('PCA')

plt.colorbar(label='Price (£)')

plt.subplot(1, 3, 2)
plt.scatter(lle_result[:, 0], lle_result[:, 1], c=book_prices, cmap='viridis')
plt.title('Locally Linear Embeddings')

plt.colorbar(label='Price (£)')

plt.subplot(1, 3, 3)
plt.scatter(tsne_result[:, 0], tsne_result[:, 1], c=book_prices, cmap='viridis')
plt.title('t-SNE')

plt.colorbar(label='Price (£)')

plt.tight_layout()
plt.show()



