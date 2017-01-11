#coding:utf-8
import re, os
import MeCab
# import word2vec

FILE_NAME = 'out.txt'

def parser_wiki(filename):
    m = MeCab.Tagger ("mecabrc")
    m.parse('')
    doc = []
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
                    # word_list += node.surface + ' '
                    doc.append( node.surface )
                node = node.next
    return doc


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
    training_docs = []
    for filename in list:
        array = filename.split('/')
        if re.match('^wiki_', array[-1]):
            f = open( FILE_NAME, 'a' )
            # logging
            filename = filename.encode('utf-8')
            print(filename);

            # get text wakatied
            doc = parser_wiki(filename)
            sent = TaggedDocument(words= doc, tags=['d4'])
            # put document array
            training_docs.append( sent )
            # write document
            f.write(doc)
            f.close()

    # word2vec.create_model( FILE_NAME )
