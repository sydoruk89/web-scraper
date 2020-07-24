import requests
from bs4 import BeautifulSoup

def get_citations_needed_count(URL):
    """
    This function takes in a url and returns an integer that represents quantity of neeeded citation.
    """
    response = requests.get(URL)

    content = response.content

    soup = BeautifulSoup(content, 'html.parser')

    #result = soup.find_all(class_='noprint Inline-Template Template-Fact')

    result = soup.find_all(text='citation needed')

    return(len(result))

quantity = get_citations_needed_count('https://en.wikipedia.org/wiki/Stock_market')

print(quantity)

def get_citations_needed_report(URL):
    """
    This function takes in a url and returns a string with each citation needed on own line, in order found.
    """

    response = requests.get(URL)

    content = response.content

    soup = BeautifulSoup(content, 'html.parser')

    result = soup.find_all(class_='noprint Inline-Template Template-Fact')
    needed = ''
    for el in result:
        res = el.find_parent().get_text()
        if res not in needed:
            needed += f'\n Citation needed for: \n {res}'
    return needed

print(get_citations_needed_report('https://en.wikipedia.org/wiki/Stock_market'))

def get_citations_needed_by_section(URL):
    """
    This function takes in a url and returns a string with a section name.
    """
    response = requests.get(URL)

    content = response.content

    soup = BeautifulSoup(content, 'html.parser')
    text = ''
    result = soup.find_all(class_='noprint Inline-Template Template-Fact')
    for el in result:
        res = el.find_parent().find_previous_sibling('h2').find(class_='mw-headline').get_text()
        if res not in text:
            text += f'\n A citation needed in the section: \n {res} \n'
    return text

print(get_citations_needed_by_section('https://en.wikipedia.org/wiki/Stock_market'))