import requests, json, os, subprocess, time


def responseList(version):
    url = 'https://papermc.io/api/v1/paper/' + version
    response = requests.get(url)
    return response.json()

def download():
    print('Downloading new jar-file. MC-version: ' + latestMCVersion + ' Paper version: ' + latestPaperVersion)
    url = 'https://papermc.io/api/v1/paper/' + latestMCVersion + '/latest/download'

    with open('paper-' + latestPaperVersion + '.jar', 'wb') as code:
        code.write(requests.get(url).content)
    print('Download complete')

latestMCVersion = responseList('')['versions'][0]

latestPaperVersion = responseList(latestMCVersion)['builds']['latest']

currentMCVersion = ''
currentPaperVersion = ''
with open('serverVersion.json') as versionFile:
    data = json.load(versionFile)
    currentMCVersion = data['MCVersion']
    currentPaperVersion = data['PaperVersion']

if ((latestMCVersion != currentMCVersion) or (latestPaperVersion != currentPaperVersion)):
    print("New server version available!")
    download()
    print("Waiting for MC-server to stop...")
    while True:
        try:
            subprocess.check_output(["pidof", "-s" ,"java"])
            time.sleep(1)
        except subprocess.CalledProcessError:
            print('Process stopped')
            break
    subprocess.check_output(['tmux', 'kill-session', '-t', 'minecraft-server'])
    print("tmux session killed")
    with open('launch.sh', 'r') as launch:
        oldFile = launch.read()
        newFile = oldFile.replace('paper-' + currentPaperVersion + '.jar', 'paper-' + latestPaperVersion + '.jar')
    with open('launch.sh' , 'wt') as launch:
        print(newFile)
        launch.write(newFile)
        print("launch.sh updated")
    with open('serverVersion.json', 'w') as jsonfile:
        versionData = {"MCVersion": latestMCVersion, "PaperVersion": latestPaperVersion}
        json.dump(versionData, jsonfile)
        print("serverVersion.json updated")
    subprocess.check_output(['rm', 'paper-' + currentPaperVersion + '.jar'])
    print("Old .jar removed")
    os.system('./start.sh')
    print("New server started")
else:
    print("Server has the latest version")