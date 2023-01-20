from nltk import sent_tokenize
from sklearn.feature_extraction.text import CountVectorizer
import re
count_vect = CountVectorizer()
i=0
path_save = r"D:\\Natural Language Processing\\Text representation 2\\Ouput\\BagOfNGrams\\"
file_name="BagOfNGrams document "
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
    count_vect = CountVectorizer(ngram_range=(1,3))
    bow_rep = count_vect.fit_transform(processed_docs)
    with open(path_save + file_name + str(i) + ".txt", mode='a', encoding="utf-8") as s:
        print("Bag Of NGrams document " + str(i)),
        s.write("\nOut vocabulary in document "+str(i)+":\n"),
        s.write(str(count_vect.vocabulary_)),
        s.write("\nBow representation for "+str(i)+":\n"),
        s.write(str(bow_rep[0].toarray())),
        # print(bow_rep[0].toarray())

    # print("BoW representation for "+str(i)+":\n", bow_rep[0].toarray())
    if i>999:
        break
