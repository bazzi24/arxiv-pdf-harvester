# arXiv PDF Harvester 

A powerful tool for automating the search and download of research papers from arXiv, specifically optimized for generating input data for **RAG (Retrieval-Augmented Generation)** systems.

## Key Features
- **Multi-keyword search:** Supports complex queries with logical operators (AND, OR).

- **Multi-threading:** Uses `ThreadPoolExecutor` to significantly increase upload speed.

- **Absolute deduplication:** Automatically checks local article IDs to avoid re-downloading files that already exist.

- **Smart file names:** Automatically cleans article titles and appends arXiv IDs to file names for easier management.

- **Secure Structure:** Integrates a delay and retry mechanism to avoid IP blocking by the arXiv API.

## Installation

1. **Clone repository:**
```bash
git clone https://github.com/bazzi24/arxiv-pdf-harvester.git
cd arxiv-pdf-harvester
```

 2. **Setting up a virtual environment**
```bash
python3 -m venv venv or python -m venv venv
# Linux:
source venv/bin/activate
# Windows:
source venv\Scripts\activate
```

3. **Install requirements**
```bash
pip install -r requirements.txt
```

4. **Run**
```bash
python3 python pdfHarvester.py
or
python python pdfHarvester.py
```

5. **Note**
- This project complies with the arXiv API terms of service. Please do not set the MAX_WORKERS value too high to ensure it does not overload the arXiv servers.

6. **Contribute**
- If you have ideas for improvements (e.g., integrating OCR or automatically extracting metadata), please create an Issue or submit a Pull Request <3
