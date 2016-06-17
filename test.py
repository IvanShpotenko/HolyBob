from nltk.corpus import wordnet as wn
adjectives =[synset.name().split('.')[0] for synset in list(wn.all_synsets('a'))]
with open('text.txt','w') as fh:
    for adj in adjectives:
        fh.write(adj+'\n')