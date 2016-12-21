#coding:utf-8
import re, os
import MeCab
import word2vec

FILE_NAME = 'out.txt'

def parser_wiki(filename):
    m = MeCab.Tagger ("mecabrc")
    # perse wiki page
    f = open(filename)
    words = []
    for line in f.readlines():
        # remove tag
        if re.match('^<doc',line):
            pass
        elif re.match('^</doc',line):
            pass
        # remove line without text
        elif len(line)<1:
            pass
        else:
            # parser via mecab
            word = m.parse(line)
            tmp = word.split(',')
            tmp = tmp[0].split('\t')
            if len(tmp) > 1:
                words.append( tmp[0] )
'''
                # 品詞を区別して抽出
                c = tmp[1]
                if(c == '名詞'):
                    words.append(tmp[0])
                if(c == '動詞'):
                    words.append(tmp[0])
'''
    return words

def find_all_files(directory):
    # get file name in the directory recursively
    list = []
    for root, dirs, files in os.walk(directory):
        for file_ in files:
            full_path = os.path.join(root, file_)
            list.append(full_path)
    return list


dir = '/Users/kishi-lab/mogami/coupus/extracted/AC'
# get list of all file
list = find_all_files(dir)
f = open( FILE_NAME, 'a')
for filename in list:
    if re.match('^wiki_', filename):
        words = parser_wiki(filename)
        f.write(words)
f.close()
word2vec.create_model( FILE_NAME )
