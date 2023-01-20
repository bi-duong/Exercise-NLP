import nltk
from nltk import sent_tokenize, word_tokenize
import re
# nltk.download('punkt')
from numpy import array, float64, double
from numpy import argmax
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import pandas as pd
file_name4="Bien doi van pham sai thu vien thu "
path_save = "/Text Representation/"
path_save2 = r"D:\\Natural Language Processing\\Text Representation\\Bien doi van ban xai thu vien\\"
i = 0
count = 0
vocab = {}
label_encoder = LabelEncoder()
onehot_encoder = OneHotEncoder(sparse=False, dtype=float64)
while True:
    arrs = []
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
        for doc in processed_docs:
            for word in doc.split():
                if word not in vocab:
                    count = count + 1
                    vocab[word] = count
        with open(path_save2 + file_name4 + str(i) + ".txt", mode='a', encoding="utf-8") as save4:
            sl = data.split()
            print("Bien doi van ban thu " + str(i) + " bang thu vien sklearn")
            save4.write("\n=====Bien doi van ban thu " + str(i) + "======\n"),
            integer_encoded = label_encoder.fit_transform(sl)
            save4.write("\n**Label Encoded  " + str(i) + ":**\n"),
            save4.write(str(integer_encoded)),
            integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
            onehot_encoded = onehot_encoder.fit_transform(integer_encoded)
            save4.write("\n**Onehot Encoded Matrix  " + str(i) + ":**\n"),
            save4.write(str(onehot_encoded))

    if i>999:
        break

















