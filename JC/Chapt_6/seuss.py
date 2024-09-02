f = open('JC\Chapt 6\seuss.txt', 'r')
word_freq = {}

for line in f:
    clean_line = line.strip()#remove \n

    for i in ['!', '?', '.', ',']: #remove punctuation
        clean_line = clean_line.replace(i, '')

    words = clean_line.title().split(" ")#capitalise first letter and split 

    for w in words:
        if w != '':
            if w in word_freq:
                word_freq[w] += 1

            else:
                word_freq[w] = 1

#print(word_freq)
def get_value(item):
    return item[1]
sorted_word_freq = dict(sorted(word_freq.items(), key=get_value, reverse=True))
#print(sorted_word_freq)

for k, v in sorted_word_freq.items():
    print(f"{k} repeated {v} times.")

f.close()