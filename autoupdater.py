import requests
import json
import os


os.chdir('~/survival')
def responseList(version):
    url = 'https://papermc.io/api/v1/paper/' + version
    response = requests.get(url)
    return response.json()

def download():
    url = 'https://papermc.io/api/v1/paper/' + latestMCVersion + '/latest/download'

    with open('paper-' + latestPaperVersion + '.jar', 'wb') as code:
        code.write(requests.get(url).content)

    versionData = {"MCVersion": latestMCVersion, "PaperVersion": latestPaperVersion}
    with open('serverVersion.json', 'w') as jsonfile:
        json.dump(versionData, jsonfile)


latestMCVersion = responseList('')['versions'][0]

latestPaperVersion = responseList(latestMCVersion)['builds']['latest']

currentMCVersion = ''
currentPaperVersion = ''
with open('serverVersion.json') as versionFile:
    data = json.load(versionFile)
    currentMCVersion = data['MCVersion']
    currentPaperVersion = data['PaperVersion']

if ((latestMCVersion != currentMCVersion) or (latestPaperVersion != currentPaperVersion)):
    download()

