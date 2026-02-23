DIVISIONS = ["AFC", "NFC"]
CONFERENCES = ["East", "North", "South", "West"]

class Team:
    def __init__(self, name, division, conference):
        self.name = name
        self.division = division
        self.conference = conference
        self.division_index = DIVISIONS.index(self.division)
        self.conference_index = CONFERENCES.index(self.conference)

    def __eq__(self, other):
        return self.division_index == other.division_index and self.conference_index == other.conference_index



patriots = Team("Patriots", "AFC", "East")
cowboys = Team("Cowboys", "NFC", "East")  
dolphins = Team("Dolphins", "AFC", "East")  
broncos = Team("Broncos", "AFC", "West")  

print(f"DEBUG: Patriots same as Dolphins = {patriots == dolphins}")
print(f"DEBUG: Patriots same as Cowboys = {patriots == cowboys}")
print(f"DEBUG: Patriots same as Broncos = {patriots == broncos}")