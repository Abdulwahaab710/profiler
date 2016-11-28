import requests
from BeautifulSoup import BeautifulSoup


def main():
    # url = raw_input('Enter a URL to Profile')
    url = 'http://abdulwahaab.ca'
    r = requests.get(url)
    print findLinks(r.text)


def findLinks(html):
    soup = BeautifulSoup(html)
    links = []
    for href in soup.findAll('a', href=True):
        if (href['href'][0] != '#' and href['href'][0] != ''):
            links.append(str( href['href'] ))
    return links

if __name__ == '__main__':
    main()
