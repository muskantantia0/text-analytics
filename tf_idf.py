import nltk.corpus
import re
import string
import pandas as pd
data = pd.read_csv('tf_idf.csv')

reviewer=data.id.tolist()
reviewer.insert(0,"reviewerID")
doc = data.title.tolist()
a=type(doc)
print len(doc)
punc = re.compile( '[%s]' % re.escape( string.punctuation ) )
term_vec = [ ]
for d in doc:
    d=str(d)
    d = d.lower()
    d = punc.sub( '', d )
    d= d.split(' ')
    term_vec.append(d)
wordlist = []
def flatten(lists):
    for numbers in lists:
        for x in numbers:
            wordlist.append(x)
    return wordlist

a=flatten(term_vec)
from math import log
print len(wordlist)
wordfreq = []
def wordListToFreqDict(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    d=dict(zip(wordlist, wordfreq))
    # for key, value in sorted(d.iteritems(), key=lambda (k, v): (v, k)):
    #     return "%s: %s" % (key, value)
    items = [(v, k) for k, v in d.items()]
    items.sort()
    items.reverse()  # so largest is first
    final1 = [(k,v,round(log(round((len(wordlist)/v),4),10),4),(v*(log((len(wordlist)/v),10)))) for v, k in items]
    return final1
finals =  wordListToFreqDict(wordlist)
print finals
