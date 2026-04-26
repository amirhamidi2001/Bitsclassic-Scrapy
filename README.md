```markdown
# Bitsclassic Scrapy Spider

A Scrapy spider that extracts product data (title, categories, URL, currency, and availability status) from [bitsclassic.com](https://bitsclassic.com).  
The scraped data is stored in a MongoDB database.

---

## ✨ Features

- Crawls all product categories and paginated pages
- Extracts:
  - Product title
  - Categories
  - Product URL
  - Currency
  - Availability status
- Stores scraped data in MongoDB
- Respects `robots.txt`

---

## 🛠 Requirements

- Python 3.8+
- MongoDB (local or remote instance)
- Dependencies listed in `requirements.txt`

---

## 📦 Installation

```bash
git clone https://github.com/amirhamidi2001/Bitsclassic-Scrapy.git
cd Bitsclassic-Scrapy
pip install -r requirements.txt
```

Make sure MongoDB is running before starting the spider.

---

## ⚙️ Configuration

MongoDB settings are defined in:

```
bitsclassic/bitsclassic/settings.py
```

Update the following variables if needed:

```python
MONGODB_URI = "mongodb://localhost:27017"
MONGODB_DATABASE = "bitsclassic"
MONGODB_COLLECTION = "items"
```

---

## ▶️ Usage

```bash
cd bitsclassic
scrapy crawl bitsclassic
```

---

## 📁 Project Structure

```
.
├── bitsclassic/
│   ├── bitsclassic/
│   │   ├── __init__.py
│   │   ├── items.py
│   │   ├── middlewares.py
│   │   ├── pipelines.py
│   │   ├── settings.py
│   │   └── spiders/
│   │       ├── bitsclassic_spider.py
│   │       ├── plugins.py
│   │       └── __init__.py
│   └── scrapy.cfg
├── LICENSE
├── README.md
└── requirements.txt
```

---

## 🗄 Database

The spider uses a custom MongoDB pipeline defined in:

```
bitsclassic/bitsclassic/pipelines.py
```

Ensure your MongoDB server is accessible using the configured URI.

---

## 📄 License

This project is licensed under the MIT License.  
See the `LICENSE` file for details.

---

## 👤 Author

Amir Hamidi  
GitHub: https://github.com/amirhamidi2001