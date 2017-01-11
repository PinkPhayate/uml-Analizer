# -*- coding: utf-8 -*-
from gensim.models import word2vec
import logging
import sys
import gensim
import sys
from gensim.models.doc2vec import Doc2Vec
from gensim.models.doc2vec import TaggedDocument


TEXT_FILE = '1207163046.txt'

def create_doc_model(docs):
    model = Doc2Vec(documents=training_docs, min_count=1, dm=0)
    model.save ( 'doc2vec.model' )

def calc_sim(word1, word2):
	model.similarity(word1,word2)
# create model
model = gensim.models.Word2Vec.load('sample.model')

def choose_words():

    f = open( TEXT_FILE)
    line = f.readline() # 1行を文字列として読み込む(改行文字も含まれる)
    list01 = []
    list01.append(line)
    # count=0
    while line:
        line = f.readline()
        list01.append(line)
        # count += 1
    f.close
    count = len(list01)
    print(list01)

    dict = {}
    index = 0
    for N1 in list01:
        for j in range (index, len(list01)):
            N2 = list01[j]
            N1 = N1.replace('\n', '')
            N2 = N2.replace('\n', '')
            if N1 != N2 and len(N1)>0 and len(N2)>0:
                similality = model.similarity(N1,N2)
                print(N1 +', '+ N2)
                print (similality)
        index += 1

def analyze_word( line ):
    node = m.parseToNode(line)
    words = []
    while node:
        # print (node.surface, node.feature)
        # pos = node.feature.split(",")[0]
        # if pos != '記号':
        # word_list += node.surface
        # print(node.surface)
        if len(node.surface) > 0:
            words.append(node.surface)
        node = node.next
    return words

if __name__ == '__main__':
    choose_words()
	# print("if you'd like to quit, put quit on word1")
	# while True:
	# 	print ( 'word1: ' )
	# 	word1 = input()
	# 	if word1 == 'quit':
	# 		break
	# 	print ( 'word2: ' )
	# 	word2 = input()
    #
	# 	# calcurate similarity
	# 	print( model.similarity(word1,word2) )
