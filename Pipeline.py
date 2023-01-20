from operator import itemgetter

from bs4 import BeautifulSoup
import requests
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from googletrans import Translator, constants
from nltk import PorterStemmer, WordNetLemmatizer, pos_tag
from nltk.corpus import wordnet
import nltk
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('wordnet')
# nltk.download('omw-1.4')
path_save = "D:/Natural Language Processing/new data english/"
file_name = "Bang Tin Thu "
i = 0
stop_word = []
while True:
    i = i + 1
    path = r"D:/Natural Language Processing/data english/Bai bao thu " + str(i) + ".txt"
    with open(path, mode='r',encoding="utf8") as f:
        data = f.read()
        if data == '':
            break
        translator = Translator()
        uni = data.encode("utf8")
        sentto = sent_tokenize(data)
        wordto = word_tokenize(data)
        ps = PorterStemmer()
        lemmatizer = WordNetLemmatizer()
        m = []
        m.append(wordto)
        stop_words = set(stopwords.words('english'))
        filtered_sentence = []
        for w in wordto:
            if w not in stop_words:
                filtered_sentence.append(w)
        print("Bang Tin Thu " + str(i))
        def pos_tagger(nltk_tag):
            if nltk_tag.startswith('J'):
                return wordnet.ADJ
            elif nltk_tag.startswith('V'):
                return wordnet.VERB
            elif nltk_tag.startswith('N'):
                return wordnet.NOUN
            elif nltk_tag.startswith('R'):
                return wordnet.ADV
            else:
                return None
        pos_tagged = pos_tag(word_tokenize(data))
        wordnet_tagged = list(map(lambda x: (x[0], pos_tagger(x[1])), pos_tagged))
        translated = translator.translate(data, src='cs', dest='vi')
        with open(path_save + file_name + str(i) + ".txt", mode='a', encoding="utf-8") as a:
            a.write("=======Unicode Normalization=======\n" + str(uni) + "\n"),
            a.write("=========Sent tokenize====\n"),
            for line in range(len(sentto)):
                a.write(str(sentto[line]) + "\n"),
            a.write("==========Word tokenize========\n" + str(wordto) + "\n"),
            a.write("=========Stop word========\n" + str(filtered_sentence) + "\n"),
            count = {}
            a.write("=====Sort the alphabet from high to low:===== \n")
            for x in wordto:
                if x in count:
                    count[x] += 1
                else:
                    count[x] = 1
            for x in sorted(count, key=count.get, reverse=True):
                a.write(str(x) + ": " + str(count[x]) + "\n"),
            a.write("=========Stemming============ \n")
            for s in wordto:
                a.write("Actual: " + s + " <==Stem=>> " + ps.stem(s).lower() + "\n")
            a.write("=========Lemmatization Simple======= \n")
            for w in wordto:
                a.write("Actual: %s  <==Lemma==> %s" % (w, lemmatizer.lemmatize(w))+"\n"),
            a.write("=========Lemmatization Advantaged Type POS TAG======= \n")
            lemmatized_sentence = []
            for word, tag in wordnet_tagged:
                if tag is None:
                    lemmatized_sentence.append(word)
                else:
                    a.write("Actual: %s  <==Lemma==> %s" % (word, lemmatizer.lemmatize(word, tag))+"\n")
                    lemmatized_sentence.append(lemmatizer.lemmatize(word, tag))
            lemmatized_sentence = " ".join(lemmatized_sentence)
            a.write("=========Lemmatization sentence Type POS TAG======= \n")
            a.write(lemmatized_sentence)
            a.write("\n=========Translated============ \n"+translated.text+"\n")
            if i>999:
                print("End data 1000 page")
                break
        f.close()
