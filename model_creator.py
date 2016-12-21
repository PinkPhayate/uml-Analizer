# -*- coding: utf-8 -*-
from gensim.models import word2vec
import logging

'''
param1 -> filename to read
param2 -> filename to write
'''

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# fi = open(sys.argv[1], 'r')
# sentences = word2vec.Text8Corpus('out.txt')
sentences = word2vec.Text8Corpus( sys.argv[1] )

'''
# if you read sentences text, use below
sentences = word2vec.LineSentence(sys.argv[1])
'''


model = word2vec.Word2Vec(sentences, size=200, min_count=1, window=15)

# 学習結果を出力する
model.save( sys.argv[2])

if __name__ == '__main__':
    print "end"
