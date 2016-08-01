import glob, os
import csv
os.chdir("NLP")
l1=[]
for file in glob.glob("*.txt"):
    f_name = file
    file = open(file, "r")
    term_list=[]
    for line in file:
      term_list.append(line)
    b=len(term_list)
    import re
    import pandas as pd
    import string
    from nltk.corpus import stopwords
    lst = []
    def x(doc):
        for i in range(0, len(doc)):
            if isinstance(doc[i], str):
                doc1 = doc[i][doc[i].find(">") + 1: doc[i].find("<")]
                doc2 = re.sub("[^a-zA-Z]", " ", doc1)
                lower_case_words = doc2.lower()
                words = lower_case_words.split()
                from nltk.corpus import stopwords
                remove_stop = [w for w in words if not w in stopwords.words("english")]
                lst.append(remove_stop)

        return lst
    x(term_list)
# print lst
    wordlist = []
    def flatten(lst):
        for numbers in lst:
            for x in numbers:
                wordlist.append(x)
        return wordlist
    flatten(lst)
# print wordlist
    uni=[]
    for w in wordlist:
        if w not in uni:
          uni.append(w)
    a=len(uni)
    l=[]
    l.append(f_name)
    l.append(b)
    l.append(a)
    l1.append(l)
df2 = pd.DataFrame(l1,columns=['file', 'sentences','words'])
print df2
print "the total no of sentences are %s" %(sum(df2["sentences"]))

print "the total no of words are %s" %(sum(df2["words"]))
