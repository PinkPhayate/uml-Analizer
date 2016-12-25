# -*- coding: utf-8 -*-
from gensim.models import word2vec
import logging
import sys
# -*- coding: utf-8 -*-
import gensim
import sys

def create_model(wakatigaki):
    # Word2Vecの学習に使用する分かち書き済みのテキストファイルの準備
    sentences = word2vec.Text8Corpus(wakatigaki)

    # Word2Vecのインスタンス作成
    # sentences : 対象となる分かち書きされているテキスト
    # size      : 出力するベクトルの次元数
    # min_count : この数値よりも登場回数が少ない単語は無視する
    # window    : 一つの単語に対してこの数値分だけ前後をチェックする
    model = word2vec.Word2Vec(sentences, size=200, min_count=20, window=15)

    # 学習結果を出力する
    model.save("sample.model")

def calc_sim(word1, word2):
	model.similarity(word1,word2)
# create model
model = gensim.models.Word2Vec.load('sample.model')

if __name__ == '__main__':
	print("if you'd like to quit, put quit to word1")
	while True:
		print("word1: ")
		word1 = sys.stdin.read()
		if word1 == 'QUIT':
			break
		print("word2: ")
		word2 = sys.stdin.read()

		# calcurate similarity
		model.similarity(word1,word2)
