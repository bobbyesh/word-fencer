import csv

with open('thai.csv') as f:
    out = open('thai.txt', 'w')
    reader = csv.reader(f, delimiter='\t', quotechar='|')
    for line in reader:
        token = line[0]
        out.write(token + '\n')

out.close()
