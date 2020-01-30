import requests
import json
import os


os.chdir('~/survival')
def responseList(version):
    url = 'https://papermc.io/api/v1/paper/' + version
    response = requests.get(url)
    return response.json()

latestMCVersion = responseList('')['versions'][0]
print(latestMCVersion)

latestPaperVersion = responseList(latestMCVersion)['builds']['latest']
print(latestPaperVersion)

url = 'https://papermc.io/api/v1/paper/' + latestMCVersion + '/latest/download'

with open('paper-' + latestPaperVersion + '.jar', 'wb') as code:
    code.write(requests.get(url).content)