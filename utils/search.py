#!/usr/bin/python3
# search.py
# written by Nicholas Poet on 2.26.2020


def find_link_path(start_page, end_page, links_iter, backlinks_iter):
    """ Takes the return values of get_page_links and get_page_backlinks
        from links.py and searches for a link path between the given pages

    Args:
        start_page (string):
        end_page (string):
        links_iter (iterator object):
        backlinks_iter (iterator object):

    Returns:
        List of intermediary pages in order if they exist (starting with
        start_page and ending with end_page), or returns list containing
        only end page for a direct link.
    """

    # first check for direct page links
    if end_page in links_iter:
        return [start_page, end_page]

    # next check for single intermediary link
    # TODO: better search style over bruteforce
    for obj in links_iter:
        if obj in backlinks_iter:
            return [start_page, obj.title(), end_page]

    # finally, use search method to enumerate link path from all included links/backlinks
    # TODO
