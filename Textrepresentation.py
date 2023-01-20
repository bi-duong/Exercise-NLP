import nltk
from nltk import sent_tokenize, word_tokenize
import re
# nltk.download('punkt')
from numpy import array, float64, double
from numpy import argmax
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import pandas as pd
file_name = "Tu xay ma nguon "
file_name2="Bien doi bo tu vung xai thu vien sklearn cua "
file_name3="Kho tu vung "
path_save = r"D:\\Natural Language Processing\\Text Representation\\"
i = 0
count = 0
vocab = {}
arr = []
def get_one_hot_vector(some_string):
    onehot_encoded = []
    for Word in some_string.split():
        temp = [0] * len(vocab)
        if Word in vocab:
            temp[vocab[Word] - 1] = 1
        onehot_encoded.append(temp)
    return onehot_encoded
label_encoder = LabelEncoder()
onehot_encoder = OneHotEncoder(sparse=False, dtype=float64)
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
        for doc in processed_docs:
            for word in doc.split():
                if word not in vocab:
                    count = count + 1
                    vocab[word] = count
    if i>999:
        break
    f.close()
###Kho tu vung
with open(path_save + file_name3 + str(i) + " file"+".txt", mode='a', encoding="utf-8") as save3:
    save3.write("====Kho tu vung 1 nghin file==== \n"),
    save3.write(str(vocab)),
    print("Da co kho tu vung")
# ### Tu xay dung ma nguon
with open(path_save + file_name + str(i) +" file"+ ".txt", mode='a', encoding="utf-8") as save:
    save.write("\n====Bien doi tu vung====\n"),
    save.write(str(get_one_hot_vector(' '.join(map(str, vocab))))),
    save.write("\n====Bien doi van ban====\n"),
    save.write(str(get_one_hot_vector(processed_docs[0]))),
    print("Da bieu dien bo tu vung va cac van ban thanh One-hot Vector bang cach tu xay dung ma nguon")

### Xu dung thu vien sklearn
with open(path_save + file_name2 + str(i) +" file"+ ".txt", mode='a', encoding="utf-8") as save2:
    for v in vocab.keys():
        arr.append(v)
    save2.write("\n====Bieu dien tu trong bo tu vung====")
    integer_encoded = label_encoder.fit_transform(arr)
    save2.write("\n**Label Encoded 1 to "+str(i)+":**\n"),
    save2.write(str(integer_encoded)),
    integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
    onehot_encoded = onehot_encoder.fit_transform(integer_encoded)
    save2.write("\n**Onehot Encoded Matrix 1 to "+str(i)+":**\n"),
    save2.write(str(onehot_encoded))
    print("Da bieu dien bo tung vung bang thu vien sklearn")
print("Chuong trinh ket thuc")









