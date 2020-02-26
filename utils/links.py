#!/usr/bin/python3
# links.py
# written by Nicholas Poet on 2.26.2020

import pywikibot


def get_page_links(req_page):
	""" Gets interwiki page links embedded on a given page (given a Wikipedia 
		page title) 
	
	Args:
		req_page (string): The title of the requested Wikipedia page

	Returns:
		An iterator of pages that the given page links to
	"""
	wiki = pywikibot.Site()
	page = pywikibot.Page(wiki, req_page)
	return page.interwiki()


def get_page_backlinks(req_page):
	""" Gets page backlinks for a given wikipedia page title
	
	Args:
		req_page (string): The title of the requested Wikipedia page
		
	Returns:
		An iterator of pages that link to the given page
	"""
	wiki = pywikibot.Site()
	page = pywikibot.Page(wiki, req_page)
	return page.backlinks()
