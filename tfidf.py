#coding=utf-8
import math
import string
import nltk
from nltk.corpus import stopwords
from collections import Counter
from nltk.stem.porter import *
def get_tokens(text):  #分词
    lowers=text.lower()
    tokens=lowers.split(' ')
    return tokens
def stem_tokens(tokens, stemmer): #按照相同词根归并
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed
def tf(word, count): #计算tf
    return count[word]
def n_containing(word, count_list): #计算包含某词的句子数
    return sum(1 for count in count_list if word in count)
def idf(word, count_list): #计算idf
    return math.log10(len(count_list) / (n_containing(word, count_list)))
def tfidf(word, count, count_list): #计算tf*idf
    return tf(word, count) * idf(word, count_list)
f=open('C:\Users\swy\Desktop\miss.txt')
fr=f.read()
fr=fr.replace('\"','')
fr=fr.replace('-','')
fr=fr.replace('Mr. ','Mr,') #Mr.的“.”很容易与巨好混淆，先去掉，随后再补充上
fr=fr.replace('Mrs. ','Mrs,')
fr=fr.replace('. ','.')
fr=fr.replace('.\n','.')
for i in('!','?','\n'): #将换行的符号全部替换成“.”用来分句
    fr=fr.replace(i,'.')
length = fr.count(".")
print length
u=range(1,1000)
count=range(1,1000)
final=range(1,1000)
u[1:length]=fr.split('.',length-1)
for i in range(1,length):
    u[i]=u[i].replace('Mr,','Mr.') #去掉逗号等分句时不会去掉的符号
    u[i]=u[i].replace('Mrs,','Mrs.')
    for j in (',','(',')',';'):
        u[i]=u[i].replace(j,'') #去停用词
    tokens=get_tokens(u[i])
    filtered = [w for w in tokens if not w in stopwords.words('english')]
    stemmer = PorterStemmer()
    stemmed = stem_tokens(filtered, stemmer)
    count[i]=Counter(stemmed)
    print count[i]
countlist=[count[j] for j in range (1,length)]
for i in range(1,length):
    final[i] = {word: tfidf(word, count[i], countlist)/math.sqrt(sum(tfidf(word,count[i],countlist)*tfidf(word,count[i],countlist) for word in count[i])) for word in count[i]}
    print final[i]