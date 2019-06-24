from gensim.matutils import corpus2csc
from gensim.corpora import Dictionary
import json
import string
import numpy as np
import math
import collections
import networkx as nx
from nltk.corpus import stopwords



#s=set(stopwords.words('english'))
#s = ["a", "the", "an", "and", "that", "they", "of", "on"]
s = ['makes', 'many', 'way','also','theres','lot','see','dont','people','today','one','america', 'american', 'americans' ,'all', 'just', 'being', 'over', 'both', 'through', 'yourselves', 'its', 'before', 'herself', 'had', 'should', 'to', 'only', 'under', 'ours', 'has', 'do', 'them', 'his', 'very', 'they', 'not', 'during', 'now', 'him', 'nor', 'did', 'this', 'she', 'each', 'further', 'where', 'few', 'because', 'doing', 'some', 'are', 'our', 'ourselves', 'out', 'what', 'for', 'while', 'does', 'above', 'between', 't', 'be', 'we', 'who', 'were', 'here', 'hers', 'by', 'on', 'about', 'of', 'against', 's', 'or', 'own', 'into', 'yourself', 'down', 'your', 'from', 'her', 'their', 'there', 'been', 'whom', 'too', 'themselves', 'was', 'until', 'more', 'himself', 'that', 'but', 'don', 'with', 'than', 'those', 'he', 'me', 'myself', 'these', 'up', 'will', 'below', 'can', 'theirs', 'my', 'and', 'then', 'is', 'am', 'it', 'an', 'as', 'itself', 'at', 'have', 'in', 'any', 'if', 'again', 'no', 'when', 'same', 'how', 'other', 'which', 'you', 'after', 'most', 'such', 'why', 'a', 'off', 'i', 'yours', 'so', 'the', 'having', 'once']

f = open("formatted_citizenship.json", "r")
d = json.load(f)

minimum_count_for_link = 4


corpus = []
for x in d:
	thing = d[x]["text"].lower().translate(str.maketrans('', '', string.punctuation))
	tfiltered = list(filter(lambda w: not w in s, thing.split()))

	corpus.append(tfiltered)

dct = Dictionary(corpus)
bow_corpus = [dct.doc2bow(line) for line in corpus]
term_doc_mat = corpus2csc(bow_corpus)





from collections import OrderedDict

document = corpus
names = dct.values()


occurrences = OrderedDict((name, OrderedDict((name, 0) for name in names)) for name in names)

# Find the co-occurrences:
for l in document:
	for i in range(len(l)):
		print(l[i - 5:i] + l[i + 5:])
		for item in l[i - 5:i] + l[i + 5:]:
			occurrences[l[i]][item] += 1


# Print the matrix

wcounts = dict()

for x in occurrences.keys():
	wcounts[x] = 0

for d in corpus:
	for w in d:
		wcounts[w] += 1

graphd = {
	"nodes" : [],
	"links" : []
}


ease_id_dict = dict()

for x in dct.keys():
	ease_id_dict[dct[x]] = x


for x in wcounts.keys():
	graphd["nodes"].append({
		"id" : x,
		"word" : x,
		"count" : wcounts[x], 
		"linked" : 0
		})


edges = dict()
for x in occurrences.keys():
	for y in occurrences[x].keys():
		st1 = x + ":" + y
		st2 = x + ":" + y
		if st1 not in edges and st2 not in edges:
			if occurrences[x][y] > minimum_count_for_link:
				edges[st1] = {
				"source" : x,
				"target" : y,
				"weight" : occurrences[x][y]
				}

		elif st1 not in edges:
			edges[st2]["weight"] += occurrences[x][y]
		else:
			edges[st1]["weight"] += occurrences[x][y]

graphd["links"] = list(edges.values())

ngraph = nx.node_link_graph(graphd, multigraph=False)

for x in graphd["links"]:
	t1 = x["source"]
	t2 = x["target"]
	for y in graphd["nodes"]:
		if y["id"] == t1 or y["id"] == t2:
			y["linked"] += 1


#print(ngraph.edges)
#print(nx.clustering(ngraph))
json.dump(graphd, open("data.json", "w"), indent=4)





		
#print(graphd)











