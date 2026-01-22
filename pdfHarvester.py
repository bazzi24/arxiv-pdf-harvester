import arxiv
import os
import requests
import time
from concurrent.futures import ThreadPoolExecutor


SAVE_DIR = 'data'
MAX_WORKERS = 5  # Number of files to download simultaneously (Don't set it too high to avoid being blocked by arXiv)
KEYWORDS = ["LLM", 
            "RAG", 
            "Deep Learning", 
            "Artificial Intelligence"]

if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)

# Get the list of downloaded IDs to avoid duplicates
existing_ids = [f.split('_')[0] for f in os.listdir(SAVE_DIR) if f.endswith('.pdf')]

def download_one_file(result):
    """Load handling function for each individual file"""
    arxiv_id = result.entry_id.split('/')[-1]
    
    if arxiv_id in existing_ids:
        return f"It's available: {arxiv_id}"

    try:
        clean_title = "".join([c for c in result.title if c.isalnum() or c in (' ', '-')]).strip()
        filename = f"{arxiv_id}_{clean_title[:80]}.pdf"
        filepath = os.path.join(SAVE_DIR, filename)

        # Tải file
        response = requests.get(result.pdf_url, timeout=30)
        if response.status_code == 200:
            with open(filepath, 'wb') as f:
                f.write(response.content)
            return f"Success: {arxiv_id}"
        else:
            return f"Error {response.status_code}: {arxiv_id}"
    except Exception as e:
        return f"Loading error {arxiv_id}: {e}"

# 3. Chạy chương trình chính
def main():
    query_string = " OR ".join([f'all:"{k}"' for k in KEYWORDS])
    client = arxiv.Client(page_size=100, 
                          delay_seconds=3.0, 
                          num_retries=5)
    
    search = arxiv.Search(query=query_string, 
                          max_results=10000, 
                          sort_by=arxiv.SortCriterion.Relevance)

    print("Retrieving the list of articles from arXiv...")
    all_results = list(client.results(search))
    print(f"Find {len(all_results)} article. Start multi-threaded loading....")

    # Sử dụng ThreadPoolExecutor để tăng tốc
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        # Giao việc cho các luồng
        results = list(executor.map(download_one_file, all_results))

    # In báo cáo kết quả
    for res in results:
        if "Success" in res:
            print(res)

if __name__ == "__main__":
    main()