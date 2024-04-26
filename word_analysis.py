from collections import Counter
from io import BytesIO
from typing import Iterable, List
import string

from matplotlib import pyplot as plt
from wordcloud import WordCloud

def float_check(word: str):
    try:
        float(word)
        return True
    except ValueError:
        return False


def common_words_list(messages: Iterable, words_count: int) -> List[str]:
    import nltk
    nltk.download('stopwords')
    from nltk.corpus import stopwords

    words_list = []

    stop_words = set(
        stopwords.words('russian')+
        list(string.punctuation)+ 
        list(string.digits)
    )

    for message in messages:
        if message.text:
            words_list.extend(
                [
                    x for x in message.text.lower().split() 
                    if x not in stop_words and not x.isdigit()
                    and not float_check(x)
                ]
            )
    counter = Counter(words_list)
    c = counter.most_common(words_count)
    return [x[0] for x in c]


def words_cloud(words: List[str]) -> bytes:
    text = ' '.join(words)
    text = text.replace('.', '_')
    
    wordcloud = WordCloud(
        width=800, height=400, background_color='white', margin=40
    ).generate(text)
    
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off") 
    img_buffer = BytesIO()
    plt.savefig(img_buffer, format='PNG')
    img_buffer.seek(0)
    plt.close()
    return img_buffer.getvalue()