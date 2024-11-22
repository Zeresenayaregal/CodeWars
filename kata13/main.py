import re
from collections import Counter

def top_3_words(text):
    words = re.findall(r"[a-zA-Z']+", text)    
    word_counts = Counter([word.lower() for word in words if re.search(r"[a-zA-Z]", word)])
    
    return [word for word, _ in word_counts.most_common(3)]