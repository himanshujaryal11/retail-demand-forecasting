"""Basic preprocessing helpers for social-media sentiment text."""
import re
import html


def clean_text(text: str) -> str:
    """Normalize URLs, mentions, HTML entities, and whitespace.

    Keep negation words (for example, 'not') because they affect sentiment.
    """
    text = html.unescape(str(text))
    text = text.lower()
    text = re.sub(r"https?://\S+|www\.\S+", " URL ", text)
    text = re.sub(r"@\w+", " USER ", text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text
