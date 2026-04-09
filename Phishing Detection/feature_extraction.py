import re

def extract_features(url):
    features = []

    features.append(len(url))
    features.append(1 if "https" in url else 0)
    features.append(url.count('.'))
    features.append(len(re.findall(r'[^\w]', url)))
    features.append(1 if re.search(r'\d+\.\d+\.\d+\.\d+', url) else 0)
    features.append(1 if '@' in url else 0)
    features.append(1 if '-' in url else 0)

    # Extra features
    features.append(1 if "login" in url else 0)
    features.append(1 if "secure" in url else 0)
    features.append(1 if "bank" in url else 0)

    return features
def explain_url(url):
    reasons = []

    if "login" in url:
        reasons.append("Contains suspicious keyword 'login'")
    if "@" in url:
        reasons.append("Contains '@' symbol")
    if url.startswith("http://"):
        reasons.append("Not secure (uses HTTP)")
    if len(url) > 75:
        reasons.append("URL is too long")
    if "-" in url:
        reasons.append("Contains '-' symbol (common in phishing)")

    return reasons