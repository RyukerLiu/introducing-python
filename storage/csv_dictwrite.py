import csv
villains = [{'first': 'Doctor', 'last': 'No'} , {'first': 'Rosa', 'last' : 'Klebb'}]
with open('villians', 'wt', newline='') as fout:
    csvout = csv.DictWriter(fout, ['first', 'last'])
    csvout.writeheader()
    csvout.writerows(villains)
