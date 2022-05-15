import json
import os
import gzip
import random
from collections import defaultdict

# MAX_PAIR_SIZE = 50000

# def get_language(id, sentences_by_language):
#     for code in sentences_by_language:
#         if id in sentences_by_language[code]:
#             return code
#     return None

# def format_pair(orig, trans):
#     return f"{orig}-{trans}"


# def process_sentences(languages):
#     sentences_by_language = defaultdict(dict)
#     with open("sentences.csv") as f:
#         for line in f:
#             id, code, sentence = line.rstrip().split("\t")
#             if code in languages:
#                 sentences_by_language[code][int(id)] = sentence
#     return sentences_by_language


# with open("languages.json") as f:
#     languages = json.load(f)

# sentences_by_language = process_sentences(languages)
# sentence_pairs = defaultdict(list)

# i = 0
# with open("links.csv") as f:
#     for line in f:
#         orig_id, trans_id = [int(id) for id in line.rstrip().split("\t")]
#         orig_code = get_language(orig_id, sentences_by_language)
#         trans_code = get_language(trans_id, sentences_by_language)

#         if orig_code == trans_code or orig_code not in languages or trans_code not in languages:
#             continue

#         orig_sentence = sentences_by_language[orig_code][orig_id]
#         trans_sentence = sentences_by_language[trans_code][trans_id]

#         if orig_code < trans_code:
#             sentence_pairs[format_pair(orig_code, trans_code)].append([orig_sentence, trans_sentence])
#         else:
#             sentence_pairs[format_pair(trans_code, orig_code)].append([trans_sentence, orig_sentence])

#         i += 1
#         if i % 1000 == 0:
#             print(i)


# for pair in sentence_pairs:
#     random.shuffle(sentence_pairs[pair])
#     pairs = sentence_pairs[pair][:MAX_PAIR_SIZE]

#     if(len(pairs) > 500):
#         content = json.dumps(pairs, ensure_ascii=False).encode("utf-8")
#         with gzip.open(f"./data/{pair}.json.gz", 'wb') as f:
#             f.write(content)

meta = {}
for file in os.listdir("./data"):
    size = os.path.getsize(f"./data/{file}")
    pair = file.replace(".json.gz", "")
    meta[pair] = size

with open("meta.json", "w") as f:
    json.dump(meta, f, indent=2)
