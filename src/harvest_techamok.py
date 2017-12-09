# Harvests the Techamok Best Pics of the month sub-website
# Date create: 08 December 2017
# Author: Rudolph Lombaard (prlombaard@gmail.com)



# DONE: refactor, move file getter into its own function
# DONE: stop iteration if "end of range" of images reached.

# TODO: make multithreaded / multiprocess to download more images at once
# TODO: Automatically determine range of images to harvest
# TODO: use logging module, NOT prints!!!


import requests
import threading
import inspect


def get_file_from_url(base_url=f'http://www.techamok.com/pics', year=17, month_index=11, start_index=1, stop_index=300):
    print('Hello from get_file_from_url')
    frame = inspect.currentframe()
    args, _, _, values = inspect.getargvalues(frame)
    print('function name "%s"' % inspect.getframeinfo(frame)[2])
    for i in args:
        print("    %s = %s" % (i, values[i]))
    # return
    # return [(i, values[i]) for i in args]
    # year = 17
    # base_url = f'http://www.techamok.com/pics'
    # base_url = f'http://www.techamok.com/pics//17/dec/best'
    months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    # month_index = -1
    # start_index = 1
    # stop_index = 275
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
            # DONE: use context manager
            with open(filename, 'wb') as f:
                f.write(r.content)
            print(f'Written {url} to disk at {filename}')
        else:
            print(f'Skipping {url}, REASON = content from server not an image')
            break  # Break out of loop, assuming that end of range have been reached


def main():
    # Main function
    print('Techamok Harvester')
    # get_file_from_url(start_index=104)

    workers = [threading.Thread(target=get_file_from_url, kwargs={'month_index': x+8}) for x in range(4)]

    for worker in workers:
        worker.start()
    for worker in workers:
        worker.join()


if __name__ == '__main__':
    main()
