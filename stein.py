#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author: Gustavo Serra Scalet
Licença: GPLv3 ou mais recente
"""

__VERSION__ = 0.1
MINIMUM_ARGS = 1

from parser import steinerParser
from kruskal import findKruskal
from output import printGraph

def main(source, verbose, args):
	"""Most top-level abstraction for the algorithm workflow"""
	graph, terminals = steinerParser(source, verbose, args)
	# with this graph we can get all vertices with graph.keys()
	init_subgraph = findKruskal(graph, terminals)
	printGraph(init_subgraph)
	# great_subgraph = doTabuMagic(graph, terminals, init_subgraph)


if __name__ == "__main__":
	"""Controling initialization"""
	from sys import argv, exit
	from os import sep
	from optparse import OptionParser
	
	usage = """usage: %prog SOURCE_FILE [-v --verbose]
Parses input SOURCE_FILE to the desired structure"""
	parser = OptionParser(usage,
			description=steinerParser.__doc__.replace('\t',''),
			version="%%prog %s" % __VERSION__)
	parser.add_option('-v', '--verbose', dest='verbose', action="store_true",
		default=False, help="Verbose")

	(opt, args) = parser.parse_args(argv)
	
	if len(args) < MINIMUM_ARGS + 1:
		# not enough arguments
		print """ERROR: not enough arguments.
Try `%s --help' for more information""" % args[0].split(sep)[-1]
		exit(1)
	else:
		source = args[1]
	verbose = opt.verbose
	main(source, verbose, args)

