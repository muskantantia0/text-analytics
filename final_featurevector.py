import nltk.corpus
import re
import string
import pandas as pd
data = pd.read_csv('reviewamazondata.csv')

reviewer=data.reviewerID.tolist()
reviewer.insert(0,"reviewerID")
doc = data.reviewText.tolist()
a=type(doc)
punc = re.compile( '[%s]' % re.escape( string.punctuation ) )
term_vec = [ ]
for d in doc:
    d=str(d)
    d = d.lower()
    d = punc.sub( '', d )
    d= d.split(' ')
    term_vec.append(d)


# Remove stop words from term vec
from nltk.corpus import stopwords
stop_words = stopwords.words("english")
for i in range( 0, len( term_vec ) ):
    term_list = [ ]

    for term in term_vec[ i ]:
        if term not in stop_words:
            term_list.append( term )

    term_vec[ i ] = term_list
for i in range(0,len(term_vec)):
    term_vec[i]=' '.join(term_vec[i])
#print term_vec[1]

'''Making a dictionary using zip()'''
vec_dictionary = zip(reviewer,term_vec)

# print vec_dictionary[1:3]
#print type(vec_dictionary)

D=[]
import textmining
from textmining import TermDocumentMatrix
def termdocumentmatrix_example():
    tdm =textmining.TermDocumentMatrix()
    for i in range(0, len(vec_dictionary)):
            tdm.add_doc(vec_dictionary[i][1])


    for row in tdm.rows(cutoff=50):
        D.append(row)
    #tdm.write_csv('matrix7.csv', cutoff=100)
termdocumentmatrix_example()

v = zip(reviewer,D)
print v["reviewerID"]
final=pd.DataFrame.from_dict(v,orient='index',dtype=None)
print (final)

import csv
final.to_csv("test2.csv")


