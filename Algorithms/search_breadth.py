from collections import deque

graph = {}
graph["oli"] = ["horst", "uschi", "anne", "max"]
graph["anne"] = ["oli", "friedel", "martin", "max"]
graph["martin"] = ["anne","friedel", "sonja", "michi", "marlene"]
graph["max"] = ["anne", "oli"]
graph["horst"] = ["uschi", "oli"]
graph["uschi"] = ["horst", "oli", "anni"]
graph["friedel"] = ["anne", "martin", "hans"]
graph["hans"] = ["friedel"]
graph["sonja"] = ["michi", "marlene"]
graph["michi"] = ["martin", "sonja", "marlene"]
graph["marlene"] = ["martin", "sonja", "michi"]
graph["anni"] = []

def search_bf(startname, endname):
    """Breitensuche für einen gegebenen gerichteten Graphen"""
    search_queue = deque()
    search_queue += graph[startname]
    searched = []
    #hops = 1
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person == endname:
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

start = "oli"
ziel = "anni"

if search_bf(start, ziel):
    print("Von", start, "nach", ziel, "ist möglich.")
else:
    print("Dieser Weg ist nicht möglich.")