import json
import utilities

with open("social_network.json", "r") as file:
    graph = json.load(file)

_,p=utilities.bfs(graph,"Emma")
connect = utilities.is_connected(graph)
print(connect)