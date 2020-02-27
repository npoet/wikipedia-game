#!/usr/bin/python3
# links.py
# written by Nicholas Poet on 2.26.2020

import requests

URL = "https://en.wikipedia.org/w/api.php"


def get_page_name(req_page):
	""" Gets official page name from redirect (if applicable) for
		search purposes

	Args:
		req_page (str): The (incomplete) title of the requested Wikipedia page

	Returns:
		Default Wikipedia redirect result for input title
	"""
	s = requests.session()
	params = {
		"action": "query",
		"format": "json",
		"list": "search",
		"srsearch": req_page
	}
	req = s.get(url=URL, params=params).json()
	name = req['query']['search'][0]['title']
	return name


def get_page_links(req_page):
	""" Gets interwiki page links embedded on a given page (given a Wikipedia
		page title) 
	
	Args:
		req_page (str): The title of the requested Wikipedia page

	Returns:
		A list of pages that the given page links to
	"""
	s = requests.session()
	links_list = []
	params = {
		"action": "query",
		"format": "json",
		"titles": req_page,
		"prop": "links",
		"pllimit": 500,
	}
	# get initial page links (max 500 per request through wikipedia's GET API)
	req_init = s.get(url=URL, params=params).json()
	return_data_init = req_init['query']['pages']
	for key, value in return_data_init.items():
		for link in value["links"]:
			links_list.append(link["title"])
	# get remaining page links (if applicable)
	while 'continue' in s.get(url=URL, params=params).json():
		params = {
			"action": "query",
			"format": "json",
			"titles": req_page,
			"prop": "links",
			"pllimit": 500,
			"plcontinue": s.get(url=URL, params=params).json()['continue']['plcontinue']
		}
		req_next = s.get(url=URL, params=params).json()
		return_data_next = req_next['query']['pages']
		for key, value in return_data_next.items():
			for link in value["links"]:
				links_list.append(link["title"])
	return links_list


def get_page_backlinks(req_page):
	""" Gets page backlinks for a given wikipedia page title

	Args:
		req_page (string): The title of the requested Wikipedia page

	Returns:
		A list of pages that link to the given page
	"""
	s = requests.session()
	backlinks_list = []
	params = {
		"action": "query",
		"format": "json",
		"list": "backlinks",
		"bltitle": req_page,
		"bllimit": 500
	}
	# get top 500 (maximum request) backlinks to the given page to assist search
	req_init = s.get(url=URL, params=params).json()
	return_data_init = req_init['query']['backlinks']
	for link in return_data_init:
		backlinks_list.append(link["title"])
	# get remaining page links (if applicable)
	while 'continue' in s.get(url=URL, params=params).json():
		params = {
			"action": "query",
			"format": "json",
			"list": "backlinks",
			"bltitle": req_page,
			"bllimit": 500,
			"blcontinue": s.get(url=URL, params=params).json()['continue']['blcontinue']
		}
		req_next = s.get(url=URL, params=params).json()
		return_data_next = req_next['query']['backlinks']
		for link in return_data_next:
			backlinks_list.append(link["title"])
	return backlinks_list
