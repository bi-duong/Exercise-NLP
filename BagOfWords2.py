from time import sleep

from nltk import sent_tokenize
from sklearn.feature_extraction.text import CountVectorizer
import re
count_vect = CountVectorizer(binary=True)
i=0
path_save = r"D:\\Natural Language Processing\\Text representation 2\\Ouput\\BagOfWords\\"
file_name="BagOfWords document "
while True:
    i = i + 1
    path = r"D:\Natural Language Processing\data english\Bai bao thu " + str(i) + ".txt"
    with open(path, mode='r', encoding="utf8") as f:
        origin_data = f.read()
        if origin_data == '':
            break
    new_data_ = re.sub(r"[^a-zA-Z0-9]", " ", origin_data)
    data = re.sub("[0-9]", "", new_data_)
    document = sent_tokenize(data)
    processed_docs = [doc.lower().replace(".", "") for doc in document]
    bow_rep = count_vect.fit_transform(processed_docs)
    with open(path_save + file_name + str(i) + ".txt", mode='a', encoding="utf-8") as s:
        s.write("\nBoW with binary vectors for "+str(i)+"\n"),
        print("\nBoW with binary vectors for " + str(i) + "\n"),
        count_vect.fit(processed_docs)
        s.write(str(bow_rep[0].toarray()))
    if i>999:
        break
