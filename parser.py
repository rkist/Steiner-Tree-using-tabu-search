#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author: Gustavo Serra Scalet
Licença: GPLv3 ou mais recente
"""

def steinerParser(source, verbose = False, args = []):
	"""
	Parses the source file and returns the structure
	"""
	from re import compile, search
	
	content = open(source).read().splitlines()  # list of all the lines of the source file
	_EDGE_REGEX = compile('E\s+(?P<origin>[0-9]*)\s+(?P<destiny>[0-9]*)\s+(?P<weight>[0-9]*)')  # for a common edge
	_TERMINAL_REGEX = compile('T\s+(?P<edge_name>[0-9]*)')  # for a terminal vertex

	# graph[x] = [(y,w),] : there is an edge with weight w from x to y 
	graph = {}
	# list of all the vertices that are terminals, so we'll have to find a path
	# with them that has minimal cost 
	terminals = []

	# auxiliary functions
	def insert(origin, data):
		"""Makes the insertion correct, creating a list when needed"""
		if graph.has_key(origin):
			graph[origin].append(data)
		else:
			graph[origin] = [data,]

	for line in content:
		clean_line = line.strip().upper()  # removing spaces on [0] and [-1] and uppering case
		edge_match = search(_EDGE_REGEX, clean_line)
		if edge_match:  # found an edge line description
			data = edge_match.groupdict()
			if verbose:
				print "Line '%s' is an edge description line with %s" % (line, str(data))
			# non-directional graph
			insert(int(data['origin']), (int(data['destiny']), int(data['weight'])))
			insert(int(data['destiny']), (int(data['origin']), int(data['weight'])))
			continue
		terminal_match = search(_TERMINAL_REGEX, clean_line)
		if terminal_match:  # terminal description line
			data = terminal_match.groupdict()
			if verbose:
				print "Line '%s' is a terminal description line with %s" % (line, str(data))
			terminals.append(int(data['edge_name']))
			# continue  # not needed, it's the end of this loop anyway
	# end for
	return graph, terminals

