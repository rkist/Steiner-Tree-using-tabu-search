#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author: Gustavo Serra Scalet
Licença: GPLv3 ou mais recente
"""

# Keep this in mind:
# graph[x] = (y,w) : there is an edge with weight w from x to y 

def findKruskal(graph, terminals):
	"""
	Returns a minimum graph that includes all the terminals using kruskal algorithm
	"""
	# FIXME: this ain't kruskal!!
	return getAnyGraph(graph, terminals)

def getAnyGraph(graph, terminals):
	"""Find edge-shortest graph with terminals very fast!"""
	initial_graph = {}

	if True:  # new
		for u_index, u in enumerate(terminals):
			# gets the next vertex from the terminals
			if u == terminals[-1]:
				v = terminals[0]  # the last has to be connected with the first
			else:
				v = terminals[u_index+1]
			# put the edge between those terminals vertices in our graph
			initial_graph[u] = filter(lambda x: x[0] == v, graph[u])

	else:
		for u_index, u in enumerate(terminals):
			list_of_missing_terminals_indexes = range(u_index, len(terminals))  # from u -> last terminal
			for v_index in list_of_missing_terminals_indexes:
				v = terminals[v_index]

				# function that returns true when this edge links the vertex v
				f = lambda edge: edge[0] == v

				desired_edge = filter(f, graph[u])  # getting the edge u -> v
				initial_graph.append(desired_edge)
	return initial_graph

# Unused!!
# def checkVertex(u, edge):
# 	"""Check if this edge has the vertex u"""
# 	return ((edge[0] is u) or (edge[1] is u))
