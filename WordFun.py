import string
import random
import operator
from operator import itemgetter

class WordFun:
    
    def __init__(self, word_file):
        self.wordFile = word_file
        chunk = self.wordFile.read()
        self.words = chunk.split("\n")
        self.n_gram_index = {}
        self.n_gram_stats = {}
        return
    
    def find_n_gram_matches(self, n = 2):
        letters = list(string.ascii_lowercase)
        consonants = list(filter(lambda x: x not in ['a', 'e', 'i', 'o', 'u'], letters))
        chosen = random.sample(consonants, n)
        matches = list(filter(lambda x: "".join(chosen) in x, self.words))
        print("chosen = " + str(chosen))
        input("Press enter to continue...")
        print("matches = " + str(matches))
        return
    
    def gen_stats_of_n_grams(self, n = 2):
        n_words = 0
        letters = list(string.ascii_lowercase)
        consonants = list(filter(lambda x: x not in ['a', 'e', 'i', 'o', 'u'], letters))
        for word in self.words:
            length = len(word)
            if length >= n:
                for i in range(length - n + 1):
                    n_gram = word[i:(i+n)]
                    if (n_gram[0] in consonants) and (n_gram[1] in consonants):
                        #print("word = " + word + ", n_gram = " + n_gram)
                        if n_gram in self.n_gram_index:
                            wordlist = self.n_gram_index[n_gram]
                            count = self.n_gram_stats[n_gram]
                            self.n_gram_index[n_gram] = wordlist + [word]
                            self.n_gram_stats[n_gram] = count + 1
                        else:
                            self.n_gram_index[n_gram] = [word]
                            self.n_gram_stats[n_gram] = 1
            n_words = n_words + 1
            if n_words % 10000 == 0:
                print("word = " + word + ", n_words = " + str(n_words))
        self.n_gram_stats = sorted(self.n_gram_stats.items(), key = itemgetter(1), reverse = True)
        
        for (n_gram, count) in self.n_gram_stats:
            print("n_gram = " + n_gram + ", count = " + str(count))
        print(len(self.n_gram_stats))
        return
                
    
if __name__ == '__main__':
    word_file = open("C:\\Users\\bibudh.lahiri\\Desktop\\words.txt", "r") 
    wf = WordFun(word_file)
    #wf.find_n_gram_matches(2)
    wf.gen_stats_of_n_grams()
    