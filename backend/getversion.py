import urllib.request


def getlatestversion():
    try:
        url = "https://www.x3collective.com/LU/SWLU/version.txt"
        request = urllib.request.Request(url, headers={'User-Agent' : "SWLU Updater"})
        response = urllib.request.urlopen(request)
        data = response.read()
        return data.decode('utf-8')
    except urllib.request.HTTPError as e:
        return "Cannot get version info."