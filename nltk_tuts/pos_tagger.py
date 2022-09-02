
from textblob import TextBlob as tb
from textblob.taggers import NLTKTagger

ap_tagger = NLTKTagger()
# This is verbose; we'll see a DRYer version later
b1 = tb("Beautiful is better than ugly.", pos_tagger=ap_tagger)
b2 = tb("Simple is better than complex.", pos_tagger=ap_tagger)
print(b1.tags)
# [('Beautiful', u'NNP'), ('is', u'VBZ'), ('better', u'JJR'), ('than', u'IN'), ('ugly', u'RB')]
print(b2.tags)