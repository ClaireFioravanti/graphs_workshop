import json

social_network = { "Liam": ["Emma", "Raj", "Sofia"], 
                "Emma": ["Liam", "Raj", "Chen"], 
                "Raj": ["Liam", "Emma", "Priya", "Sofia"], 
                "Sofia": ["Liam", "Raj", "Priya"], 
                "Chen": ["Emma", "Aiko", "Noah"], 
                "Priya": ["Raj", "Sofia", "Arjun"], 
                "Aiko": ["Chen", "Yuki", "Noah"], 
                "Noah": ["Chen", "Aiko", "Maya"], 
                "Yuki": ["Aiko", "Maya"], 
                "Maya": ["Noah", "Yuki", "Ethan"], 
                "Arjun": ["Priya", "Ethan", "Fatima"], 
                "Ethan": ["Maya", "Arjun", "Olivia"], 
                "Fatima": ["Arjun", "Olivia"], 
                "Olivia": ["Ethan", "Fatima", "Isabella"], 
                "Isabella":["Olivia"] 
}

with open("social_network.json", "w") as file:
    json.dump(social_network, file, indent=4)

