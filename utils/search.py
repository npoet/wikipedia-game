#!/usr/bin/python3
# search.py
# written by Nicholas Poet on 2.26.2020

from utils.links import *


def find_link_path(start_page, end_page, links, backlinks):
	""" Takes the return values of get_page_links and get_page_backlinks
		from links.py and searches for a link path between the given pages

	Args:
		start_page (string):
		end_page (string):
		links (iterator object):
		backlinks (iterator object):

	Returns:
		List of intermediary pages in order if they exist (starting with
		start_page and ending with end_page), or returns list containing
		only end page for a direct link.
	"""

	# first check for direct page links
	if end_page in links:
		return [start_page, end_page]

	# next check for single intermediary link using backlinks
	for page in links:
		if page in backlinks:
			return [start_page, page, end_page]

	# attempt breadth-first search
	graph = {start_page: {
		'title': start_page,
		'parent': None
	}}
	queue = [graph[start_page]]
	while queue:
		current_page = queue[0]
		queue = queue[1:]
		current_page_links = get_page_links(current_page)
		for link in current_page_links:
			if link not in graph:
				graph[link] = {
					'title': link,
					'parent': current_page
				}
				if link == end_page:
					p = []  # temporary variable to declare path
					path = gen_path(graph, graph[link], p)
					path = path.reverse()	# path orignally started with end page
					return path
			queue.append(graph[link])


def gen_path(graph, node, p):
	""" Generates path to desired Wikipedia page from graph traversal

	Args:
		graph (dict): graph of connected page links generated by breadth-first search
		node (dict: current graph node
		p (list): pointer to path list

	Returns:
		Completed path list
	"""
	if node['parent']:
		p.append(node['parent']['title'])
		gen_path(graph, graph[node['parent']], p)
	return p
