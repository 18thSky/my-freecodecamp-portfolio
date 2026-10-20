import re

def extract_attributes(element):
    matches = re.findall(r'([\w-]+)="([^"]*)"', element)
    return [f"{attr}, {val}" for attr,val in matches]