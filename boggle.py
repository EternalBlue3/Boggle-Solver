import logging
import time
import random

def generate_random_board():
    out = []
    letters = "abcdefghijklmnopqrstuvwxyz"
    for r in range(100):
        out.append(letters[random.randint(0,25)])
    return ' '.join(out)

# I have no idea what bbbb is supposed to be, it is the worst variable in the history of python. However, it is the variable I chose and I hope you respect for the fact that I have no idea what I'm doing.
bbbb = raw_input("Enter the grid values: ").upper().split()

def timeit(method):
    def timed(*args, **kw):
        t1 = time.time()
        result = method(*args, **kw)
        print '%r %2.2f sec' % (method.__name__, time.time() -t1)
        return result

    return timed

def get_grid(grid, sizeXY):
    return_dict = {}
    for x in range(sizeXY):
        for y in range(sizeXY):
            return_dict.update({(x,y):str(grid[x*sizeXY+y])})
    return return_dict

def get_neighbours():
    neighbours = {}
    for position in grid:
        x, y = position
        positions = [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x + 1, y),
                     (x + 1, y + 1), (x, y + 1), (x - 1, y + 1), (x - 1, y)]
        neighbours[position] = [p for p in positions if 0 <= p[0] < X and 0 <= p[1] < Y]
    return neighbours


def path_to_word(path):
    return ''.join([grid[p] for p in path])

def search(path):
    word = path_to_word(path)
    logging.debug('%s: %s' % (path, word))
    if word not in stems:
        return
    if word in dictionary:
        paths.append(path)
    for next_pos in neighbours[path[-1]]:
        if next_pos not in path:
            search(path + [next_pos])
        else:
            logging.debug('skipping %s because in path' % grid[next_pos])

def get_dictionary():
    stems, dictionary = set(), set()
    with open('dictionary.txt') as f:
        for word in f:
            word = word.strip().upper()
            dictionary.add(word)

            for i in range(len(word)):
                stems.add(word[:i + 1])

    return dictionary, stems


def get_words():
    for position in grid:
        logging.info('searching %s' % str(position))
        search([position])
    return [path_to_word(p) for p in paths]


def print_grid(grid, X, Y):
    s = ''
    for x in range(X):
        for y in range(Y):
            s += grid[x, y] + ' '
        s += '\n'
    print s

def word_score(word):
    wl = len(word)
    if wl < 3:
        return 0
    if ((wl == 3) or (wl == 4)):
        return 1
    if wl == 5:
        return 2
    if wl == 6:
        return 3
    if wl == 7:
        return 5
    if wl >= 8:
        return 11

size = X, Y = 4, 4
grid = get_grid(bbbb, 4)
neighbours = get_neighbours()
dictionary, stems = get_dictionary()
paths = []
print_grid(grid, X, Y)
words = get_words()
wordset = set(words)
totalwords = len(wordset)
points = 0
for thingy in wordset: points = points + word_score(thingy)
    
print "Found "+str(totalwords) + " words:\n"
print("Word   Points")
print "--------------"
for item in sorted(wordset):
    print item+"\t"+str(word_score(item))
print "--------------"
print points, "Points in total"
