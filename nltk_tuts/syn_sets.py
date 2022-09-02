from textblob import Word
from textblob.wordnet import Synset

word = Word("plant")

#  A synonym set, or synset, is a group of synonyms.
print (word.synsets[:5])

#  Definition of these synsets
print word.definitions

# The synonyms contained within a synset are called lemmas
plant = word.synsets[1]
print plant.lemma_names

# hypernyms are the synsets that are more general
# hyponyms are the synsets that are more specific

print plant.hypernyms()

print plant.hyponyms()[:3]

# holonyms are things that the item is contained in
# meronyms are components or substances that make up the item

plant.member_holonyms()
plant.part_meronyms()