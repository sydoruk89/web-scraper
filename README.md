# Web Scraper

**Author:** Roman Sydoruk **Version:** 1.0.0

## Description

THe web scraper reports the number of citations needed and identifies those cases AND include the relevant passage.

## Architecture

* Python 3.8.3
* Poetry
* Pytest

## API 
- Count function must named **get_citations_needed_count** \
get_citations_needed takes in a url and returns an integer
- Report function named **get_citations_needed_report** \
get_citations_needed_report takes in a url and returns a string. The string formatted with each citation needed on own line, in order found.
- Module named **scraper.py**
- additional function named **get_citations_needed_by_section** which organizes the needed citations by section 


[Link](https://github.com/sydoruk89/web-scraper)