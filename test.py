import parser_wiki as pw
def test_find_all_files( directory ):
    list = pw.find_all_files( directory )
    print( list )
def test_parser_wiki(filename):
    words = pw.parser_wiki(filename)
    print( words )
def integrstion_test():
    directory = '/Users/kishi-lab/mogami/coupus/extracted/DT/'
    FILE_NAME = 'test-text.txt'

    list = pw.find_all_files( directory )
    for filename in list:
        print( filename )
        f = open( FILE_NAME, 'a' )
        words = pw.parser_wiki(filename)
        f.write(words)
        f.close()
if __name__ == "__main__":
    # directory = '/Users/kishi-lab/mogami/coupus/extracted/'
    # test_find_all_files( directory )
    filename = '/Users/kishi-lab/mogami/coupus/extracted/DT/wiki_99'
    test_parser_wiki( filename )
    # integrstion_test()
