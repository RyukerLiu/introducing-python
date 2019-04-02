import csv
villains = [['Doctor', 'No'], ['Rosa', 'Klebb']]
with open('villians', 'wt', newline='') as fout:
    csvout = csv.writer(fout)
    csvout.writerows(villains)
