from gensim.models import Word2Vec
import warnings
import re
from nltk import sent_tokenize, word_tokenize
from nltk.corpus import words
import nltk
#nltk.download('words')
#ở đây em sử dụng kho từ vựng đã có sẵn trước đó khi thu thập dữ liệu hoặc ta có thể sử dụng thư viện nltk để gọi kho từ vựng có sẵn
vocab = {}
i=0
count = 0
ar=[]
#Kho từ vựng có sẵn
word_list = words.words()
# print(word_list)
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
        for doc in processed_docs:
            for word in doc.split():
                if word not in vocab:
                    count = count + 1
                    vocab[word] = count
    if i>999:
        break
    f.close()
for v in vocab.keys():
    ar.append(v)
warnings.filterwarnings('ignore')
# corpus = [['dog', 'bites', 'man'], ["man", "bites", "dog"], ["dog", "eats", "meat"], ["man", "eats", "food"]]
# # Training the model
corpus=[ar ,ar ]
model_cbow = Word2Vec(corpus, min_count=1, sg=0)  # using CBOW Architecture for trainnig
# # Summarize the loaded model
print(model_cbow)
# # Summarize vocabulary
words = list(model_cbow.wv.vocab)
print(words)
# # Acess vector for one word

val = input("Enter your vocabulary: ")
print("Vector "+str(len(model_cbow[val])))
print(model_cbow[val])