DIVISIONS = ["AFC", "NFC"]
CONFERENCES = ["East", "North", "South", "West"]
class Team:
    def __init__(self, name, division, conference):
        self.name = name
        self.division = division
        self.conference = conference
        self.division_index = DIVISIONS.index(self.division)
        self.conference_index = CONFERENCES.index(self.conference)



patriots = Team("Patriots", "AFC", "East")
cowboys = Team("Cowboys", "NFC", "East")  

print(f"DEBUG: Division index (Patriots) = {patriots.division_index}")
print(f"DEBUG: Conference index (Patriots) = {patriots.conference_index}")

print(f"DEBUG: Division index (Cowboys) = {cowboys.division_index}")
print(f"DEBUG: Conference index (Cowboys) = {cowboys.conference_index}")
