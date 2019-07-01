import re
import csv


with open("phonebook_raw.csv", encoding='utf8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    count = 0
    for line in contacts_list:
        if count == 0:
            pass
            count += 1
        else:
            line_raw = line[0] + ' ' + line[1] +  ' ' + line[2] +  ' ' + line[3] +  ' ' + line[4] +  ' ' + line[5] +  ' ' + line[6]
            print(line_raw)
            pattern = '[А-Я][а-я]+([,]|\s)[А-я][а-я]+(\s|)([А-Я][а-я]+|)[,]*[^,]?[,]([^,]+|[,])[,]?(\+7|8)?\s?[(]?\d{0,3}[)]?\s?[-]?\d{0,3}[-]?\d{0,2}[-]?\d{0,2}[,].+'
            mask = re.findall(line_raw, pattern)
            
            print(mask)





