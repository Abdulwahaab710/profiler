import requests


def main():
    url = raw_input('Enter a URL to Profile')
    r = requests.get(url)
    print r.text

if __name__ == '__main__':
    main()
