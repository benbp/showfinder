### Find tour dates in your city for the artists you like

This is a lightweight/simple-minded web scraper for parsing artist websites and extracting 
information about upcoming tour dates in your city.

### Installation

```
pip install scrapy
```
If you don't have pip, see [here](https://pip.pypa.io/en/latest/installing.html)

### Usage
First, create a urls.txt file in csv format with a line for each artist you want to search for that looks like:

```<artist name>,<artist website>```

See the urls.txt.example file for an example.

**To run**: type ```./scrape.py <city>``` in your shell. 

Requires Python 2.6 or above. Python 3 is not currently supported because it is not supported by the [scrapy](http://scrapyd.readthedocs.org/en/latest/install.html) library.

### TODO
- This only works on about 50% of websites at this point in time. Improve the parser.
    - Appears not work with anchor links
    - Regex needs to be updated for relative links with no path prefix (e.g. href='tour.html')
- Add date parsing to get the actual tour dates for <city>
- Do a date comparison so we don't print shows that already happened
- Allow specifying a time range to search for (e.g. only shows within the next 3 months)
- Duplicates are printed if multiple matches are found on different pages for the same website

#### Sample output
```
$ ./scrape.py seattle
Searching artists:
[['Kidd Pivot', 'http://www.kiddpivot.org'], ['Hiromi Uehara', 'http://www.hiromiuehara.com'], ['Robert Glasper', 'http://www.robertglasper.com'], ['Gregory Porter', 'http://www.gregoryporter.com']]
--------------------------------------------------------------------------------
Hiromi Uehara is coming to seattle! (see http://www.hiromiuehara.com/schedule/tour.html)
Kidd Pivot is coming to seattle! (see http://www.kiddpivot.org/upcoming-tours/)
Gregory Porter is coming to seattle! (see http://www.gregoryporter.com/tours/)
--------------------------------------------------------------------------------
DONE
$
```
