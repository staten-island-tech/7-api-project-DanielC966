import requests
agentResponse = requests.get(f"https://valorant-api.com/v1/agents/")
data = agentResponse.json()

def getAbilities(agent):
    for i in data["data"]:
        if agent == i["displayName"]:
            for ability in i["abilities"]:
                print(ability["displayName"])
def getAgentDescript(agent):
    for i in data["data"]:
        if agent == i["displayName"]:
            print(i["description"])
def getAgentRole(agent):
    for i in data["data"]:
        if agent == i["displayName"]:
            print(i["role"]["displayName"])
def getAgentList():
    for i in data["data"]:
        #if i["isPlayableCharacter"] == True:
            print(i["displayName"])

wantToRun = True
while wantToRun == True:
    agentSelect = input("What agent do you want to learn more about? *Stop with 'n'\n")
    if agentSelect == "n":
        break
    for i in data["data"]:
         if agentSelect == i["displayName"]:
            print(f"Info on {agentSelect.upper()}")
            print("[0] Abilities")
            print("[1] Agent Description")
            print("[2] Role")
            specifiedReq = input("Which part of the agent would you want to learn about?:")

            if specifiedReq == "0":
                print("- \nABILITIES:")
                getAbilities(agentSelect)
                print("-")
            elif specifiedReq == "1":
                print("- \nDESCRIPTION:")
                getAgentDescript(agentSelect)
                print("-")
            elif specifiedReq == "2":
                print("- \nROLE")
                getAgentRole(agentSelect)
                print("-")


