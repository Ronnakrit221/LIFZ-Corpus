from lifz_corpus.fetcher import fetch_url


result = fetch_url("https://example.com")

print("Success:", result["success"])
print("Status:", result.get("status_code"))
print("Content-Type:", result.get("content_type"))
print("Fetched at:", result.get("fetched_at"))
print()
print(result.get("html", "")[:500])

print("**********************************************************************************")
print(result)