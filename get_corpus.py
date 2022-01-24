from src.utils.cfg import CFG
from collections import Counter
import spacy

nlp = spacy.load("en_core_web_sm")

punc = """!()-[]{};:'"\,<>./?@#$%^&*_~"""
save_path = CFG.save_path

with open(save_path + "corpus.txt", "r") as f:
    corpus = f.read()

nlp.max_length = 4716410
doc = nlp(corpus)

print(len(doc.sents))
# words = corpus.split()

# corpus_filtered = corpus
# for ele in corpus_filtered:
#     if ele in punc:
#         corpus_filtered = corpus_filtered.replace(ele, "")
# corpus_filtered = corpus_filtered.lower()

# words_filtered = corpus_filtered.split()
# words_filtered_count = Counter(words_filtered)

# print(f"No. of words: {len(words)}")
# print(f"No. of unique words: {len(set(words))}")
# print(f"No. of words: {len(words_filtered)}")
# print(f"No. of unique words: {len(set(words_filtered))}")
