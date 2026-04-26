```markdown
# Bitsclassic Scrapy Spider

A Scrapy spider that extracts product data (title, categories, URL, currency, and existence status) from [bitsclassic.com](https://bitsclassic.com).  
The scraped data is stored in a MongoDB database.

## Features

- Crawls all product categories and pages.
- Extracts product title, categories, URL, and availability.
- Saves items to MongoDB (configurable via settings).
- Respects `robots.txt` by default.

## Requirements

- Python 3.8+
- MongoDB (local or remote)
- Scrapy and dependencies listed in `requirements.txt`

## Installation

```bash
git clone https://github.com/amirhamidi2001/Bitsclassic-Scrapy.git
cd Bitsclassic-Scrapy
pip install -r requirements.txt
```

## Configuration

Edit `bitsclassic/settings.py` to set your MongoDB connection details:

```python
MONGODB_URI = "mongodb://localhost:27017"
MONGODB_DATABASE = "bitsclassic"
MONGODB_COLLECTION = "items"
```

## Usage

Run the spider:

```bash
scrapy crawl bitsclassic
```

## Project Structure

```
.
├── bitsclassic/
│   ├── spiders/
│   │   ├── bitsclassic_spider.py   # main spider
│   │   └── plugins.py              # helper functions
│   ├── items.py                    # item definition
│   ├── pipelines.py                # MongoDB pipeline
│   └── settings.py                 # Scrapy settings
├── scrapy.cfg
├── LICENSE
└── README.md
```

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Author

Amir Hamidi (2023)
```