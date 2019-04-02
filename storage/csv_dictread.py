import csv
with open('villians', 'rt', newline='') as fin:
    cin = csv.DictReader(fin, fieldnames = ['first', 'last'])
    villains = [row for row in cin]

print(villains)
