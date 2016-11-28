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
    emails = []
    githubs = []
    facebook = []
    for link in soup.findAll('a', href=True):
        if (link['href'][0] != '#' and link['href'][0] != ''):
            if('@' in link['href']):
                print '[*] found an email %s' % link['href']
                emails.append(link['href'])
            elif('github' in link['href']):
                print '[*] found a github %s' % link['href']
                githubs.append(link['href'])
            elif('facebook' in link['href']):
                print '[*] found a facebook %s' % link['href']
                facebook.append(link['href'])
            else:
                links.append(str(link['href']))
                print '[*] found %s' % links[-1]
                getHtml(links[-1])
    return {'links': links, 'emails': emails, 'facebook': facebook, 'githubs': githubs}

if __name__ == '__main__':
    main()
