from time import sleep

from nltk import sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
import re
tfidf = TfidfVectorizer()
i=0
path_save = r"D:\\NLP\\Text representation 2\\Ouput\\TF_IDF\\"
file_name="TF_IDF document "
while True:
    i = i + 1
    path = r"D:\NLP\data english\Bai bao thu " + str(i) + ".txt"
    with open(path, mode='r', encoding="utf8") as f:
        origin_data = f.read()
        if origin_data == '':
            break
    new_data_ = re.sub(r"[^a-zA-Z0-9]", " ", origin_data)
    data = re.sub("[0-9]", "", new_data_)
    document = sent_tokenize(data)
    processed_docs = [doc.lower().replace(".", "") for doc in document]
    bow_rep_tfidf = tfidf.fit_transform(processed_docs)
    with open(path_save + file_name + str(i) + ".txt", mode='a', encoding="utf-8") as s:
        print("TF_IDF " + str(i)),
        s.write("\nIDF for all words in the vocabulary "+str(i)+"\n"),
        s.write(str(tfidf.idf_)),
        s.write("-" * 10),
        s.write("\nAll words in the vocabulary\n"),
        s.write(str(tfidf.get_feature_names())),
        s.write("-" * 10),
        s.write("\nTFIDF representation for all documents in our corpus\n"),
        s.write(str(bow_rep_tfidf.toarray())),
        s.write("-" * 10)
    #print(temp.toarray())
    if i>999:
        break

