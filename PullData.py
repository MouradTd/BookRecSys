import ssl
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

# Function to scrape book data from a page
def scrape_books_from_page(page_url):
    # Disable SSL certificate verification
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    
    # grab website and store in variable uclient
    uClient = urlopen(page_url, context=ssl_context)
    
    # read and close HTML
    page_html = uClient.read()
    uClient.close()
    
    # call BeautifulSoup for parsing
    page_soup = soup(page_html, "html.parser")
    
    # grabs all the products under list tag
    bookshelf = page_soup.findAll("li", {"class": "col-xs-6 col-sm-4 col-md-3 col-lg-3"})
    
    books_data = []
    for books in bookshelf:
        # collect title of all books
        book_title = books.h3.a["title"]
        
        # collect book price of all books
        book_price = books.findAll("p", {"class": "price_color"})[0].text.strip()
        
        star_rating_tag = books.find("p", class_="star-rating")
        if star_rating_tag is not None:
            star_rating = star_rating_tag.get('class')[1]  # The star rating is the second class
        else:
            star_rating = 'No rating'

        books_data.append((book_title, book_price, star_rating))
    
    return books_data

# Main function to scrape all books from the website
def scrape_all_books(base_url, total_pages):
    all_books_data = []
    for page_number in range(1, total_pages + 1):
        page_url = f"{base_url}/catalogue/page-{page_number}.html"
        books_data = scrape_books_from_page(page_url)
        all_books_data.extend(books_data)
    
    return all_books_data

# Main URL of the website
base_url = 'https://books.toscrape.com'
total_pages = 50  # Total number of pages

all_books = scrape_all_books(base_url, total_pages)

# Save the data to a CSV file
filename = "Books.csv"
with open(filename, "w") as f:
    f.write("Book title, Price, Star rating\n")
    for book_title, book_price, star_rating in all_books:
        f.write(f"{book_title}, {book_price}, {star_rating}\n")

print("All books scraped successfully!")
