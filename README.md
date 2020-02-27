### wikipedia_game.py

##### A python3 script that "plays" the wikipedia game, finding a route between two given wiki pages through links.

#### Required Packages:

- requests

#### File Structure:
    . wiki-game
    ├── _utils              (utility functions)
    |   ├── links.py        (functions to find page names, links, and backlinks)
    |   ├── search.py       (implementation of simple search and BFS)
    ├── README.md
    ├── requirements.txt
    └── wikipedia_game.py   (functional script)
    
#### Usage:

This package can be run as a single script via wikipedia_game.py:

```
python3 wikipedia_game.py "{start_page}" "{end_page}
```

#### Functionality:

The script directly accesses the Wikipedia API using the popular ```requests``` package for Python 3. First it checks 
for direct links between pages, followed by pages with a single intermediate link using links and backlinks. If there 
are two or more page hops, it finds the full path with an implementation of BFS (breadth-first search).