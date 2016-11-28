import requests
from BeautifulSoup import BeautifulSoup


def main():
    # url = raw_input('Enter a URL to Profile')
    url = 'http://abdulwahaab.ca'
    r = requests.get(url)
    print findLinks(r.text)


def findLinks(html):
    soup = BeautifulSoup(html)
    return soup.findAll('a')


if __name__ == '__main__':
    main()
