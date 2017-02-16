import math
import string
import nltk
from nltk.corpus import stopwords
from collections import Counter
from nltk.stem.porter import *
def get_tokens(text):
    lowers=text.lower()
    tokens=lowers.split(' ')
    return tokens
def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed
def tf(word, count):
    return count[word]
def n_containing(word, count_list):
    return sum(1 for count in count_list if word in count)
def idf(word, count_list):
    return math.log10(len(count_list) / (n_containing(word, count_list)))
def tfidf(word, count, count_list):
    return tf(word, count) * idf(word, count_list)
f=open('C:\Users\swy\Desktop\miss.txt')
fr=f.read()
fr=fr.replace('\"','')
fr=fr.replace('-','')
fr=fr.replace('Mr. ','Mr,')
fr=fr.replace('Mrs. ','Mrs,')
fr=fr.replace('. ','.')
fr=fr.replace('.\n','.')
for i in('!','?','\n'):
    fr=fr.replace(i,'.')
u=range(1,1000)
count=range(1,1000)
final=range(1,1000)
u[1],u[2],u[3],u[4],u[5],u[6],u[7],u[8],u[9],u[10],u[11],u[12],u[13],u[14],u[15],u[16],u[17],u[18],u[19],u[20],u[21],u[22],u[23],u[24],u[25],u[26],u[27],u[28],u[29],u[30],u[31],u[32],u[33],u[34],u[35],u[36],u[37],u[38],u[39],u[40],u[41],u[42],u[43],u[44],u[45],u[46]=fr.split('.',45)
for i in range(1,47):
    u[i]=u[i].replace('Mr,','Mr.')
    u[i]=u[i].replace('Mrs,','Mrs.')
    for j in (',','(',')',';'):
        u[i]=u[i].replace(j,'')
    tokens=get_tokens(u[i])
    filtered = [w for w in tokens if not w in stopwords.words('english')]
    stemmer = PorterStemmer()
    stemmed = stem_tokens(filtered, stemmer)
    count[i]=Counter(stemmed)
    print count[i]
countlist=[count[j] for j in range (1,47)]
for i in range(1,47):
    final[i] = {word: tfidf(word, count[i], countlist)/math.sqrt(sum(tfidf(word,count[i],countlist)*tfidf(word,count[i],countlist) for word in count[i])) for word in count[i]}
    print final[i]