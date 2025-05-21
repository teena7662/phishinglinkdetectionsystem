
import re
from urllib.parse import urlparse

def extract_features(url):
    features = []
    features.append(len(url))
    features.append(1 if "@" in url else 0)
    features.append(1 if url.count('.') > 3 else 0)
    features.append(1 if url.startswith("http://") else 0)
    features.append(1 if "//" in urlparse(url).path else 0)
    return features
