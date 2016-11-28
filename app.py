import requests
from BeautifulSoup import BeautifulSoup


def main():
    # url = raw_input('Enter a URL to Profile')
    url = 'http://abdulwahaab.ca'
    r = requests.get(url)
    findLinks(r.text)


def getHtml(url):
    try:
        r = requests.get(url)
        findLinks(r.text)
    except requests.exceptions.InvalidSchema:
        r = requests.get(
            str(
                'http://' + url
            )
        )
        findLinks(r.text)
    except requests.exceptions.MissingSchema:
        print '[*] Invalid url %s' % url


def findLinks(html):
    soup = BeautifulSoup(html)
    links = []
    for link in soup.findAll('a', href=True):
        if (link['href'][0] != '#' and link['href'][0] != ''):
            links.append(str(link['href']))
            print '[*] found %s' % links[-1]
            # getHtml(links[-1])
    return links

if __name__ == '__main__':
    main()
