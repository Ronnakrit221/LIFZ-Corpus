from bs4 import BeautifulSoup


def extract_text(html: str) -> str:
    """
    Extract readable text from raw HTML.
    """

    soup = BeautifulSoup(html, "html.parser")

    for tag in soup([
        "script",
        "style",
        "noscript",
        "svg",
        "iframe",
    ]):
        tag.decompose()

    text_parts = soup.stripped_strings
    text = " ".join(text_parts)

    return text