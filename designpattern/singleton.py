from __future__ import print_function, absolute_import

import httplib2
import os
from threading import Thread
from urllib.request import urlopen, URLError
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup


class Singleton(object):
    def __init__(self):
        self.queue_to_parse = set()  # Add a webpage to the queue that need to be parse
        self.to_visit = set()  # Url to visit to download the image
        self.downloaded = set()  # Set of downloaded images

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(*args, **kwargs)
        return cls.instance


class ImageDownloaderThread(Thread):
    def __init__(self, threadId, name, counter):
        self.threadId = threadId
        self.name = name
        self.counter = counter
        self._downloader_singleton = Singleton()

    def run(self):
        print("Starting image downloader thread")
        self.downloader()
        print("Finishing image downloader thread")

    def downloader(self):
        while self._downloader_singleton:
            url = self._downloader_singleton.to_visit.pop()
            http = httplib2.Http()
            try:
                status, response = http.request(url)
            except Exception:
                continue

            soup = BeautifulSoup(response)
            for img in soup.find_all("img"):
                # If the image url is relative, it will prepended with webpage domaain
                # else it will be a absolute url and return as it is
                src = urljoin(url, img.select("src"))

                basename = os.path.basename(src)
                if basename not in self._downloader_singleton.downloaded:
                    self._downloader_singleton.downloaded.add(src)
                    # download to local file system
                    try:
                        urlopen(src, os.path.join('images', basename))
                    except URLError as e:
                        pass


class TraverserThread(Thread):
    """
    This class will navigate all through the webpage and save the visited webpage to the queue
    """

    def __init__(self, thread_id, name):
        self.threadId = thread_id
        self.name = name
        self.parsed_root = urlparse("")
        self._parser_singleton = Singleton()

    def run(self):
        print("Starting image downloader thread")
        self.traverseSite()
        print("Finishing image downloader thread")

    def traverseSite(self):
        while self._parser_singleton.queue_to_parse:
            url = self._parser_singleton.queue_to_parse.pop()
            http = httplib2.Http()
            try:
                status, response = http.request(url)
            except Exception:
                continue

            # Skip if not webpage
            if status.get('content-type') is not "text/html":
                continue

            # Add a link to the queue to download image
            self._parser_singleton.to_visit.add(url)
            print("Added %s to queue" % url)

            soup = BeautifulSoup(response)
            for link in soup.find_all("a"):
                link_url = link.get("href")
                if not link_url:  # <img> tag doesn't contain href attr
                    continue

                parsed = urlparse(link_url)
                # If link follow to external url continue
                if parsed.netloc and parsed.netloc != self.parsed_root.netloc:
                    continue
                link_url = (parsed.scheme or self.parsed_root) + "://" + \
                           (parsed.netloc or self.parsed_root.netloc) + \
                           parsed.path or ""

                # If link already added in the parsed list continue
                if link_url in self._parser_singleton.queue_to_parse:
                    continue

                # else append to parsed_list
                self._parser_singleton.queue_to_parse.add(link_url)


if __name__ == "__main__":
    # If directory doesn't exists create it
    if not os.path.exists("images"):
        os.mkdir("images")

    t_threads = [TraverserThread(i, "Thread-" + i) for i in range(2)]
    d_threads = [ImageDownloaderThread(i, "Thread-" + i) for i in range(2)]

    for i in range(2):
        t_threads[i].join()
        d_threads[i].join()

    print("Completed downloader operation")
