import requests

def getAbilities(agent):
    agentResponse = requests.get(f"https://valorant-api.com/v1/agents/")
    data = agentResponse.json()
    for i in data["data"]:
        if agent == i["displayName"]:
            for ability in i["abilities"]:
                print(ability["displayName"])
def getAgentList():
    agentResponse = requests.get(f"https://valorant-api.com/v1/agents/")
    data = agentResponse.json()
    for i in data["data"]:
        #if i["isPlayableCharacter"] == True:
            print(i["displayName"])

wantToRun = True
while wantToRun == True:
     agentSelect = input("What agent do you want to learn more about?")

getAgentList()
getAbilities("Gekko")