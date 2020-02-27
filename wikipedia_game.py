#!/usr/bin/python3
# wikipedia_game.py
# written by Nicholas Poet on 2.26.2020

import sys
from utils.search import *


def main():
    # Get pages from user input
    start_page = get_page_name(sys.argv[1])
    end_page = get_page_name(sys.argv[2])

    # Get links and backlinks from given pages
    start_page_links = get_page_links(start_page)
    end_page_backlinks = get_page_backlinks(end_page)

    # Find page path
    path = find_link_path(start_page, end_page,
                          start_page_links, end_page_backlinks)

    # Print required output
    print(f"{' -> '.join(path)}")
    return


if __name__ == '__main__':
    main()
