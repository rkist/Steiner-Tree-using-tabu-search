#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author: Gustavo Serra Scalet
Licença: GPLv3 ou mais recente
"""

# from color import *

def printGraph(graph):
	print "Graph structure:"
	first = min(graph.keys())
	sorted_vertex = [first,]
	# auxiliary
	def insert_vertex_if_not(edge):
		v = edge[0]
		try:
			sorted_vertex.index(v)
		except ValueError:  # not found
			sorted_vertex.append(v)

	for vertex in sorted_vertex:
		print "\n%03d:" % vertex,
		for edge in graph[vertex]:
			print "\t-> %03d, weight: %03d" % edge,
			insert_vertex_if_not(edge)
	print ""  # \n
	summary(graph)

def summary(graph):
	vertices = len(graph.keys())
	# we could optimize below but for what?!?
	edges = sum([len(i) for i in graph.values()])
	weight = sum([i[1] for vertex in graph.values() for i in vertex])
	print "\nGraph with %d vertices and %d edges. Total weight is %d" % (vertices, edges, weight)
