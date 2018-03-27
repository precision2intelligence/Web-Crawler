import urllib.request
# import requests 强大的新库
class Downloader(object):
    def download_url(self,url):
        if url is None:
            return None
        response = urllib.request.urlopen(url)

        if response.getcode() != 200:
            return None
        return response.read()