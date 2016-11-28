import requests
from BeautifulSoup import BeautifulSoup


def main():
    # url = raw_input('Enter a URL to Profile')
    url = 'http://abdulwahaab.ca'
    r = requests.get(url)
    print findLinks(r.text)


def getHtml(url):
    r = requests.get(url)
    findLinks(r.text)


def findLinks(html):
    soup = BeautifulSoup(html)
    links = []
    for link in soup.findAll('a', href=True):
        if (link['href'][0] != '#' and link['href'][0] != ''):
            links.append(str(link['href']))
            getHtml(links[-1])
    return links

if __name__ == '__main__':
    main()
