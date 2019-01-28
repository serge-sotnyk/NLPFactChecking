# NLPFactChecking

## Team Name: BenchCrawlers

### Team Members:
* Adnan Manzoor :   6830516
* Numan Ijaz :      6845454
* Ayaz Maqbool :    6845575

### Approach:
Our solution reads the ```test.tsv``` file in the solver folder and processes every fact line-by-line. The following steps are performed for every fact:

**Named Entities Extraction:**
* The fact is passed to `extract_named_entities` method of `FactEntityExtraction` class.
* The pre-processing of the fact begins.
* The fact is tokenized using nltk's [word_tokenize](https://www.nltk.org/_modules/nltk/tokenize.html) method.
* This tokenized fact is then passed to nltk's [pos_tag](https://www.nltk.org/book/ch05.html) method.
* Pre-processing ends here. Now the tokens of the fact along with `parts of speech (pos)` tags will be used by nltk's [ne_chunk](https://www.nltk.org/api/nltk.chunk.html#nltk.chunk.ne_chunk) method. Which returns the tree of named entities (NEs).
* This tree of NEs is then passed to `get_continuous_chunks` method (borrowed from the internet) of the same class. This method will extract list of plain NEs from the tree.

***Using Wikipedia to verify the fact:***
* Once NEs are found in the fact, our solution fetches Wikipedia page for every entity and stores the page. If the page against an entity is already fetched it will be retrieved from the cache.
`For a single run of the program, our solution caches every page it retrieves from Wikipedia in the memory. If the data set to be tested is very large, it will consume much of the memory.`
* Once the fetching is complete for the NEs of a fact, our solution will check if NEs of the fact occur on the same page.
* `num_of_common_occurences` is the count for common occurences of both NEs in the fact.
* `total_num_of_occurences` is the count of all the comparisons made for the NEs.
* The ration of `num_of_common_occurences` to `total_num_of_occurences` is calculated. If the value of the ratio is above 0.7, our solution will result 1.0, otherwise our solution returns 0.0.

***Pre-requisites:***
* While running the program, the system `must be connected` to internet. (firewalls may interrupt the program).

***Known Errors/Drawbacks:***
* If NEs are on the same page to achieve the ratio of 0.7 and above, our program will return 1.0 regardless of the relationship (predicate) between them.
* If a Named Entity is too generic that more than one Wikipedia pages exist for it, it would not be able to decide which page to fetch. Hence our program will return 0.0.
* If there is no page for an NE in Wikipedia our program will still return 0.0.


### Installing

To install the tool, clone the repository from GitHub and then run the command:

```
python setup.py install
```

**On Ubuntu use the following command (after making sure pip3 is installed, which will also install setuptools):**

```
sudo python3 setup.py install
```

### Usage

From the command line, simply call the main module of the tool using the following keyword:

```
factchecker
```

### Result

The program takes 5-10 minutes to finish. The final results can be seen from within the repo in the following file:

```
result.ttl
```
