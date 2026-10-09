from lifz_corpus.fetcher import fetch_url
from lifz_corpus.extractor import extract_text

url = "https://example.com"

result = fetch_url(url)

if result["success"]:
    text = extract_text(result["html"])

    print("RESULT:")
    print(repr(text))

    print("\nNORMAL PRINT:")
    print(text)
else:
    print("ERROR:", result["error"])