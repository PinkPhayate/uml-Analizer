import MeCab

def analyze_word(line):
    m = MeCab.Tagger ("mecabrc")
    m.parse('')
    # perse wiki page
    line = '紙幣振込み'
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



if __name__ == '__main__':
     f = open( '1207163046.txt')
     line = f.readline()
     while line:
         words = analyze_word(line)
         print (words)
         line = f.readline()
