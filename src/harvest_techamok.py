# Module automatically harvests the Techamok Best Pics of the month website

import requests


def main():
    # Main function
    print('Techamok Harvester')
    # TODO: make multithreaded / multiprocess to download more images at once
    for i in range(0, 271):
        url = f'http://www.techamok.com/pics//17/dec/best/best{i:03}.jpg'
        filename = url.rsplit('/', 1)[1]
        filename = f'../images/{filename}'
        print(i, url, filename)
        r = requests.get(url, allow_redirects=True)
        # TODO: use context manager
        open(filename, 'wb').write(r.content)
    

if __name__ == '__main__':
    main()
