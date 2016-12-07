import gensim, pprint, csv, ew
from gensim.models import word2vec
LEARNING_DATA = 'corpass.txt'
TEST_DATA = './Eclipse_bugs_36k.csv'

BORDER = 0.6
def escape(s, quoted=u'\'"\\', escape=u'\\'):
    return re.sub(
            u'[%s]' % re.escape(quoted),
            lambda mo: escape + mo.group(),
            s.decode('utf-8'))

sentences = []

#get data for learning
# f = open(LEARNING_DATA)
# lines = f.readlines()
# f.close()
# #make a list of learning data
# for line in lines:
#     sentences.append(escape(line.replace(","," ").replace('\n', '')).strip().split(" "))

# sentences = word2vec.Text8Corpus(LEARNING_DATA)
# model = word2vec.Word2Vec(sentences, size=100)
# model.save("sample.model")


#  Create model
fi = open(sys.argv[1], 'r')
fo = open(sys.argv[2], 'w')

line = fi.readline()
while line:
    sentences.append(line)
    line = fi.readline()
#  create model
model = Word2Vec(sentences, size=100, window=5, min_count=5, workers=4)


fi.close()
fo.close()


model = word2vec.Word2Vec.load("sample.model")
# while(1):


# categories = ['bookmarks','history','general','preferences','pocket','security','build','tab','sync']
categories = [
# 'Android',
# 'Base',
# 'BASIC',
# 'Calc',
# 'Chart',
# 'Documentation',
# 'Draw',
# 'Extensions',
# 'Formula',
# 'framework',
# 'General',
# 'graphics',
# 'Impress',
# 'Installation',
# 'iOS',
# 'LibreOffice',
# 'Linguistic',
# 'Localization',
# 'PDF',
# 'storage',
# 'UI',
# 'Writer'
"APT","Core","Debug","Doc","Text","UI"
]
# main stream
while(1):
    print "mode?:"
    mode = raw_input()
#     if mode == "demo":
#         print "input a word:"
#         input_line1 = raw_input()
#         labeledSentences = gensim.models.doc2vec.LabeledListSentence(sentences)
#         model = gensim.models.doc2vec.Doc2Vec(labeledSentences, min_count=0)
#         print model.most_similar_words(input_line1,topn=10)
#     elif mode == "example":
#         print "input a sentence:"
#         input_line = raw_input()
#         sentences.append(input_line.split(' '))
#         labeledSentences = gensim.models.doc2vec.LabeledListSentence(sentences)
#         model = gensim.models.doc2vec.Doc2Vec(labeledSentences, min_count=0)
#         target_label = "SENT_" + str(len(sentences) - 1)
#         ans = model.most_similar_labels(target_label,topn=5)
#         print("")
#         print "similar sentences"
#         print " ".join(sentences[int(ans[0][0][5:])])
#         print str(ans[0][1])
#         print("")
#         print " ".join(sentences[int(ans[1][0][5:])])
#         print str(ans[1][1])
#         print("")
#         print " ".join(sentences[int(ans[2][0][5:])])
#         print str(ans[2][1])
#         print("")
#         print model.most_similar(input_line.split(' '))
#         print("")
#         print "category much rate"
#         category_rank = []
#         for category in categories:
#             print category
#             print model.n_similarity(input_line.split(' '), [category])
#     elif mode == "similar":
#         print "input a num:"
#         input_line = raw_input()
#         labeledSentences = gensim.models.doc2vec.LabeledListSentence(sentences)
#         model = gensim.models.doc2vec.Doc2Vec(labeledSentences, min_count=0)
#         print model.most_similar("SENT_"+input_line)
    if mode == "demo":
        print "word?:"
        word = raw_input().strip()
        if(word == "exit"):
            break
        try:
            for x, y in model.most_similar(positive=[word]):
                print x, y
        except:
            print "something's wrong.try again."
    if mode == "exit":
        exit()
    if mode == "test":
        matched = 0
        total = 0
        #get data for the test
        with open(TEST_DATA, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                sentences.append(escape(row[0]).replace(","," ").strip().split())
        #make the labeled sentences from data list
        # labeledSentences = gensim.models.doc2vec.LabeledListSentence(sentences)
        #learning
        # model = gensim.models.doc2vec.Doc2Vec(labeledSentences, min_count=0)
        result = []
        with open(TEST_DATA, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                sentence = escape(row[0]).replace(","," ").strip().split()
                print " ".join(sentence)
                print row[1]
                most_sim = ""
                second_sim = ""
                third_sim = ""
                sim_num = 0
                sec_num = 0
                thi_num = 0
                for word in sentence:
                    print word
                    for category in categories:
                        try:
                            tmp = model.similarity(word.encode('utf_8').lower(), category.lower())
                        except:
                            break
                        print tmp
                        if(tmp > sim_num):
                            thi_num = sec_num
                            third_sim = second_sim
                            sec_num = sim_num
                            second_sim = most_sim
                            sim_num = tmp
                            most_sim = category
                        elif(tmp > sec_num):
                            thi_num = sec_num
                            third_sim = second_sim
                            second_sim = category
                            sec_num = tmp
                        elif(tmp > thi_num):
                            third_sim = category
                            thi_num = tmp
                print most_sim
                print sim_num
                # if (most_sim == row[1] or second_sim == row[1] or third_sim == row[1]):
                if (most_sim == row[1]):
                    matched += 1
                total += 1
                # result.append([" ".join(sentence),row[1],most_sim,sim_num])
        # with open('result.csv', 'w') as f:
        #     writer = csv.writer(f, lineterminator='\n')
        #     for list in result:
        #         writer.writerow(list)
        print "matched:" + str(matched) + ",total:" + str(total)
        print str(100.0 * (float(matched)/total)) + "%matched"
#     else:
#         print "that mode doesn't exist"



# print model.most_similar_words(positive=['SENT_0', 'SENT_1'], negative=['SENT_2'], topn=5)
