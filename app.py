import requests

def getAbilities(agent):
    response = requests.get(f"https://valorant-api.com/v1/agents/")
    data = response.json()
    for i in data["data"]:
        if agent == i["displayName"]:
            for ability in i["abilities"]:
                print(ability["displayName"])
    
    

getAbilities("Gekko")