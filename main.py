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
    
    def __gt__(self, other):
        if self.division_index > other.division_index:
            return True
        elif self.division_index == other.division_index:
            return self.conference_index > other.conference_index
        else:
            return False



patriots = Team("Patriots", "AFC", "East")
cowboys = Team("Cowboys", "NFC", "East")  
dolphins = Team("Dolphins", "AFC", "East")  
broncos = Team("Broncos", "AFC", "West")  

print(f"DEBUG: Patriots greater than Dolphins = {patriots > dolphins}")
print(f"DEBUG: Broncos greater than Patriots = {broncos > patriots}")
print(f"DEBUG: Cowboys greater than Patriots = {cowboys > patriots}")
print(f"DEBUG: Patriots greater than Cowboys = {patriots > cowboys}")
