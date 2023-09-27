import requests, sys, os, io

class insertserver:
    def downloadAsset(id):
        url = 'https://assetdelivery.roblox.com/v1/asset/?id='+str(id)
        REQUEST = requests.get(url)
        if (REQUEST.status_code<400):
            rawData = REQUEST.content
            asset = open('assets/v1/rbxm/'+str(id)+".rbxm", "w")
            asset.write(str(rawData))
            return asset
        else:
            print('REQUEST_ERROR: '+str(REQUEST.status_code))
            return {'STATUS_CODE':REQUEST.status_code,'ERROR_MESSAGE':'REQUEST_ERROR: '+str(REQUEST.status_code)}
        ##endif
    ##end
    def downloadImage(id):
        url = 'https://assetdelivery.roblox.com/v1/asset/?id='+str(id)
        REQUEST = requests.get(url)
        if (REQUEST.status_code<400):
            rawData = REQUEST.content
            asset = open('assets/v1/png/'+str(id)+".png", "w")
            asset.write(str(rawData))
            return asset
        else:
            print('REQUEST_ERROR: '+str(REQUEST.status_code))
            return {'STATUS_CODE':REQUEST.status_code,'ERROR_MESSAGE':'REQUEST_ERROR: '+str(REQUEST.status_code)}
        ##endif
    ##end
    def downloadAudio(id):
        url = 'https://api.hyra.io/audio/'+str(id)
        REQUEST = requests.get(url)
        if (REQUEST.status_code<400):
            rawData = REQUEST.content
            asset = open('assets/v1/mp3/'+str(id)+".mp3", "w")
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
myQuery = os.eviron.get('QUERY_STRING')
print(str(myURLSelf)+str(myQuery))
