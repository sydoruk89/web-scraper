from web_scraper import __version__
from web_scraper.scraper import get_citations_needed_by_section, get_citations_needed_count, get_citations_needed_report
import pytest

def test_version():
    assert __version__ == '0.1.0'

def test_get_citations_needed_count():
    actual = get_citations_needed_count('https://en.wikipedia.org/wiki/Stock_market')
    expected = 5
    assert actual == expected

def test_get_citations_needed_report():
    text = get_citations_needed_report('https://en.wikipedia.org/wiki/Stock_market')
    actual = text.count('[citation needed]')
    expected = 5
    assert actual == expected

def test_get_citations_needed_by_section():
    sections = get_citations_needed_by_section('https://en.wikipedia.org/wiki/Stock_market')
    actual1 = sections.count('History')
    actual2 = sections.count('Importance')
    expected = 1
    assert actual1 == expected
    assert actual2 == expected