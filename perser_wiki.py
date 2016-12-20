import re
import MeCab

def perser_wiki(filename):
    m = MeCab.Tagger ("mecabrc")
    # perse wiki page
    f = open(filename)
    words = []
    for line in f.readlines():
        if re.match('^<doc',line):
            pass
        elif re.match('^</doc',line):
            pass
        elif len(line)<1:
            pass
        else:
            word = m.parse(line)
            tmp = word.split(',')
            tmp = tmp[0].split('\t')
            if len(tmp) > 1:
                c = tmp[1]
                if(c == '名詞'):
                    words.append(tmp[0])
                if(c == '動詞'):
                    words.append(tmp[0])
    return words
filename = '/Users/kishi-lab/mogami/coupus/text/AA/wiki_00'
words = perser_wiki(filename)
print (words)
