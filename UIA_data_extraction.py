# UIA REF NUMBER	CONSULTATIVE STATUS	IGO RELATIONS	NGO RELATIONS
import re
def reg(string):
    return re.findall('[A-Z][0-9]{4}', string)

import csv

with open('2005_data_new.csv', 'w',  newline='') as csvfile:
    fieldnames = ['UIA REF NUMBER', 'ID', 'SOURCE']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    fopen = open('data_2017.txt')
    for line in fopen:
        try:
            l = line.split('\t')
            id = l[0]
            consultative_status = reg(l[1]) if len(l) >= 2 else []
            igo = reg(l[2]) if len(l) >= 3 else []
            ngo = reg(l[3]) if len(l) == 4 else []
            for con in consultative_status:
                writer.writerow({'UIA REF NUMBER': id, 'ID': con, 'SOURCE' : 'CONSULTATIVE STATUS'})
            for i in igo:
                writer.writerow({'UIA REF NUMBER': id, 'ID': i, 'SOURCE': 'IGO'})
            for n in ngo:
                writer.writerow({'UIA REF NUMBER': id, 'ID': n, 'SOURCE' : 'NGO'})
        except Exception as e:
            print(e)
            print(id)
