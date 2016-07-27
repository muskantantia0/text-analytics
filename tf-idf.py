# Please download the libraries string,re,nltk

import string
import re
import csv
import pandas as pd
import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import wordpunct_tokenize
from nltk.stem.porter import PorterStemmer
from math import log

'''reading the csv file'''
data = pd.read_csv('loan_test.csv')

'''subset the data where loan status is fully paid'''
fully_paid=data.loc[data['loan_status'] == 'Fully Paid']
charged=data.loc[data['loan_status'] == 'Charged Off']

'''extracting the desc column to list for fully paid customers'''
doc = fully_paid.desc.tolist()
lst = []
def x(doc):

    for i in range(0, len(doc)):
        if isinstance(doc[i], str):
            doc1 = doc[i][doc[i].find(">") + 1: doc[i].find("<")]
            '''to remove punctuations'''
            doc2 = re.sub("[^a-zA-Z]", " ", doc1)
            '''splitting and converting into lower case'''
            lower_case_words = doc2.lower()
            words = lower_case_words.split()
            '''To remove stop words'''
            from nltk.corpus import stopwords
            remove_stop = [w for w in words if not w in stopwords.words("english")]
            lst.append(remove_stop)

    return lst
x(doc)

wordlist = []
def flatten(lst):
    for numbers in lst:
        for x in numbers:
            wordlist.append(x)
    return wordlist
flatten(lst)

''' Stemming'''
stems = []
def tokenize(wordlist):
    # tokens = word_tokenize(wordlist)
    for item in wordlist:
        stems.append(PorterStemmer().stem(item))
    return stems
tokenize(wordlist)


'''calculating words and its frequency'''
wordfreq = []
def wordListToFreqDict(stems):
    wordfreq = [stems.count(p) for p in stems]
    d=dict(zip(stems, wordfreq))
    return d
finals =  wordListToFreqDict(stems)
# print finals
print len(finals)
final_lst= [(v,k) for k, v in finals.items()]
final_lst.sort()
final_lst.reverse()
final_words_FP=pd.DataFrame(final_lst,columns=['tf','words'])
print final_words_FP


'''extracting the desc column to list for  for charged off  customers'''
############ charged off########
doc = charged.desc.tolist()
lst1 = []
def x(doc):

    for i in range(0, len(doc)):
        if isinstance(doc[i], str):
            doc1 = doc[i][doc[i].find(">") + 1: doc[i].find("<")]
            doc2 = re.sub("[^a-zA-Z]", " ", doc1)
            lower_case_words = doc2.lower()
            words = lower_case_words.split()
            '''To remove stop words'''
            from nltk.corpus import stopwords
            remove_stop = [w for w in words if not w in stopwords.words("english")]
            lst1.append(remove_stop)

    return lst1
x(doc)
wordlist = []
def flatten(lst1):
    for numbers in lst1:
        for x in numbers:
            wordlist.append(x)
    return wordlist
flatten(lst1)

# ""Stemming""""""
stems1 = []
def tokenize(wordlist):
    # tokens = word_tokenize(wordlist)
    for item in wordlist:
        stems1.append(PorterStemmer().stem(item))
    return stems1
tokenize(wordlist)


from math import log
wordfreq = []
def wordListToFreqDict(stems):
    wordfreq = [stems1.count(p) for p in stems1]
    d=dict(zip(stems, wordfreq))
    return d
finals1 =  wordListToFreqDict(stems1)
# print finals1
print len(finals1)
final_lst1= [(v,k) for k, v in finals1.items()]
final_lst1.sort()
final_lst1.reverse()
final_words_CO=pd.DataFrame(final_lst1,columns=['tf','words'])
print final_words_CO

'''finding similar words that occur in both the dataframes and selecting top20 by tf*idf'''
commom_words={}
for k, v in finals.items() :
    for k1,v1 in finals1.items():
        if k==k1:
            a=finals1.get(k)
            v_idf1=(a*(log((len(stems1)/a),10)))
            v_idf =(v*(log((len(stems)/v),10)))
            diff=round(abs(v_idf-v_idf1),3)
            commom_words[k]=diff
# print commom_words
print len(commom_words)
mof= [(v,k) for k, v in commom_words.items()]
mof.sort()
mof.reverse()
df=pd.DataFrame(mof,columns=['tf*idf','words'])
''' selecting top 20 '''
top=20
df1=df[0:top]
df2=df[0:top]
# print df1



'''create a term tocument matrix for fully paid'''
id = fully_paid.id.tolist()
ls=df1.words.tolist()
ls1=['usersid']
[ls1.append(z) for z in ls]

print ls1

allones=[]
for i in range(0,len(lst)):
    ones = [id[i]]
    for words in ls:
        if words in lst[i]:
            ones.append(1)
        else:
            ones.append(0)
    allones.append(ones)
print allones
''' creating a csv file'''
df2 = pd.DataFrame(allones, columns=list(ls1))
print df2
df2.to_csv("tf_idf_fullypaid.csv")

'''create a term tocument matrix for charged off'''
id = charged.id.tolist()
ls=df1.words.tolist()
ls2=['usersid']
[ls2.append(z) for z in ls]
allones1=[]
for i in range(0,len(lst1)):
    ones = [id[i]]
    for words in ls:
        if words in lst[i]:
            ones.append(1)
        else:
            ones.append(0)
    allones1.append(ones)
print allones

''' creating a csv file'''
df3 = pd.DataFrame(allones1, columns=list(ls2))
print df3
''' creating a csv file'''
df3.to_csv("tf_idf_charged.csv")















