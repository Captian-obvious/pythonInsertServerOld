import requests
import sys
import io
import os

my_webpage = """
<!DOCTYPE html>
<html>
    <head>
        <title>Asset Downloader</title>
    </head>
    <body>
        <h1>Download Asset Request Recieved.</h1>
    </body>
</html>
"""
def hello_world():
    return my_webpage
##end

def test_placeholder():
    pass
##end

class insertserver:
    def downloadAsset(assetid):
        url = 'https://assetdelivery.roblox.com/v1/asset/?id='+str(assetid)
        REQUEST = requests.get(url)
        if (REQUEST.status_code<400):
            rawData = REQUEST.content
            asset = open('../assets/v1/rbxm/'+str(assetid)+".rbxm", "w")
            asset.write(str(rawData))
            return asset
        else:
            print('REQUEST_ERROR: '+str(REQUEST.status_code))
            return {'STATUS_CODE':REQUEST.status_code,'ERROR_MESSAGE':'REQUEST_ERROR: '+str(REQUEST.status_code)}
        ##endif
    ##end
    def downloadImage(assetid):
        url = 'https://assetdelivery.roblox.com/v1/asset/?id='+str(assetid)
        REQUEST = requests.get(url)
        if (REQUEST.status_code<400):
            rawData = REQUEST.content
            asset = open('../assets/v1/png/'+str(assetid)+".png", "w")
            asset.write(str(rawData))
            return asset
        else:
            print('REQUEST_ERROR: '+str(REQUEST.status_code))
            return {'STATUS_CODE':REQUEST.status_code,'ERROR_MESSAGE':'REQUEST_ERROR: '+str(REQUEST.status_code)}
        ##endif
    ##end
    def downloadAudio(assetid):
        url = 'https://api.hyra.io/audio/'+str(assetid)
        REQUEST = requests.get(url)
        if (REQUEST.status_code<400):
            rawData = REQUEST.content
            asset = open('../assets/v1/mp3/'+str(assetid)+".mp3", "w")
            asset.write(str(rawData))
            return asset
        else:
            print('REQUEST_ERROR: '+str(REQUEST.status_code))
            return {'STATUS_CODE':REQUEST.status_code,'ERROR_MESSAGE':'REQUEST_ERROR: '+str(REQUEST.status_code)}
        ##endif
    ##end
##end

myDomainSelf = os.environ.get('SERVER_NAME')
myPathSelf = os.environ.get('PATH_INFO')
myURLSelf = myDomainSelf+myPathSelf
myQuery = os.environ.get('QUERY_STRING')
if (myQuery is not None) and (myQuery.find('id')):
    theid = int(myQuery[myQuery.find('id'):])
    if (theid is not None):
        insertserver.downloadAsset(theid)
    ##endif
##endif
