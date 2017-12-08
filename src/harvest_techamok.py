# Harvests the Techamok Best Pics of the month sub-website
# Date create: 08 December 2017
# Author: Rudolph Lombaard (prlombaard@gmail.com)



# DONE: stop iteration if "end of range" of images reached.

# TODO: make multithreaded / multiprocess to download more images at once
# TODO: Automatically determine range of images to harvest
# TODO: use logging module, NOT prints!!!


import requests


def main():
    # Main function
    print('Techamok Harvester')
    year = 17
    base_url = f'http://www.techamok.com/pics'
    # base_url = f'http://www.techamok.com/pics//17/dec/best'
    months = ['jan', 'feb', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov','dec']
    month_index = -1
    start_index = 1
    stop_index = 275
    for i in range(start_index, stop_index):
        url = f'{base_url}//{year}/{months[month_index]}/best/best{i:03}.jpg'
        filename = url.rsplit('/', 1)[1]
        # TODO: Check if output folder exists before writing there, if it does not exist create one
        filename = f'../images/{year}/{months[month_index]}/{filename}'
        print(f'Trying to download content at URL {url}')
        r = requests.get(url, allow_redirects=True)
        # print(r.content[0:10])
        # print(r.headers['Content-Type'])
        if r.headers['Content-Type'] == 'image/jpeg':
            # File found on server, continue to save the file to disk
            # TODO: use context manager
            open(filename, 'wb').write(r.content)
            print(f'Written {url} to disk at {filename}')
        else:
            print(f'Skipping {url}, REASON = content from server not an image')
            break   # Break out of loop, assuming that end of range have been reached
    

if __name__ == '__main__':
    main()
