#coding:utf-8
import re, os
import MeCab
# import word2vec

FILE_NAME = 'out.txt'
def get_words(l):
    print( type(l) )
    words = ''
    for word in l:
        # print( word )
        tmp = word.split(',')
        tmp = tmp[0].split('\t')
        # if class of word is signature, removed
        if len(tmp) > 1:
            c = tmp[1]
            if(c != '記号'):
                # save textfile
                print( tmp[0] )
                words += tmp[0] + ' '
    return words

def parser_wiki(filename):
    m = MeCab.Tagger ("mecabrc")
    m.parse('')
    # perse wiki page
    f = open(filename)
    word_list = ''
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
            # l = m.parse(line)

            node = m.parseToNode(line)
            while node:
                # print (node.surface, node.feature)
                pos = node.feature.split(",")[0]
                if pos != '記号':
                    word_list += node.surface + ' '
                node = node.next
    return word_list

def find_all_files(directory):
    # get file name in the directory recursively
    list = []
    for root, dirs, files in os.walk(directory):
        for file_ in files:
            full_path = os.path.join(root, file_)
            list.append(full_path)
    return list

if __name__ == "__main__":

    dir = '/Users/kishi-lab/mogami/coupus/extracted/'
    # get list of all file
    list = find_all_files(dir)
    for filename in list:
        array = filename.split('/')
        if re.match('^wiki_', array[-1]):
            f = open( FILE_NAME, 'a' )
            # logging
            filename = filename.encode('utf-8')
            print(filename);

            # get text wakatied
            words = parser_wiki(filename)
            f.write(words)
            f.close()
    # word2vec.create_model( FILE_NAME )
