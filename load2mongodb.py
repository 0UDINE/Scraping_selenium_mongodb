from pymongo import MongoClient
from scraper import get_scraped_books


client = MongoClient("mongodb://localhost:27017/")
db = client["ScrapedData"]
collection = db["Books"]


def run_pipeline():
    print("Démarrage du scraping...")
    books = get_scraped_books(pages=2)

    if books:
        collection.delete_many({})
        collection.insert_many(books)
        print(f"✅ {collection.count_documents({})} livres stockés dans MongoDB.")


if __name__ == "__main__":
    run_pipeline()