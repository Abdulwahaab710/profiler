import requests
from BeautifulSoup import BeautifulSoup
import re
import sys


def main(url=None):
    # url = raw_input('Enter a URL to Profile')
    url = sys.argv[1] if len(sys.argv) > 1 else raw_input('Enter a URL>> ')
    # url = 'abdulwahaab.ca'
    getHtml(url)


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
    except requests.exceptions.ConnectionError:
        print '[*] %s is unreachable' % url


def findLinks(html):
    soup = BeautifulSoup(html)
    links = []
    emails = []
    githubs = []
    twitter = []
    facebook = []
    links = soup.findAll('a', href=True)
    for index, link in enumerate(links):
        if (len(link['href']) > 0):
            if (link['href'][0] != '#' and link['href'][0] != ''):
                if('@' in link['href'] and 'twitter' not in link['href']):
                    print '[*] found an email %s' % link['href']
                    emails.append(
                        re.search(
                            "(?<=:)([a-zA-Z]|\d|@|\.)+",
                            link['href']
                        ).group()
                    )
                elif('github' in link['href']):
                    print '[*] found a github %s' % link['href']
                    githubs.append(link['href'])
                elif('facebook' in link['href']):
                    print '[*] found a facebook %s' % link['href']
                    facebook.append(link['href'])
                elif('twitter' in link['href']):
                    print '[*] found a twitter %s' % link['href']
                    twitter.append(link['href'])
                else:
                    print link['href']
                    links.append(str(link['href']))
                    print '[*] found %s' % links[-1]
                    getHtml(links[-1])
    return {
        'links': links,
        'emails': emails,
        'facebook': facebook,
        'githubs': githubs
    }

if __name__ == '__main__':
    main()
