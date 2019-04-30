import csv

def getID(argument):
    switcher = {
        "Refugio Orrantia": 1,
        "Melita Scarpaci": 2,
        "Ramiro Gault": 3,
        "Augusta Sharp": 4,
        "May Burton": 5,
        "Alex Hall": 6,
        "Lizbeth Jindra": 7,
        "Jose Ringwald": 8,
        "Kerstin Belveal": 9,
        "Richard Fox": 10,
        "Tobi Gatlin": 11,
        "Patrick Lane": 12,
        "Dylan Ballard": 13,
        "Lindsy Henion": 14,
        "Glen Grant": 15,
        "Sara Ballard": 16,
        "1663285": 16,
        "Meryl Pastuch": 17,
        "Rosalia Larroque": 18,
        "Julie Tierno": 19,
        "Jenice Savaria": 20
    }
    return switcher.get(argument, "nothing")

with open('./sus_activity_with_names.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            source = getID(row[0])
            target = getID(row[2])
            print(f'{{ "source": {source}, "target": {target} }},')
            line_count += 1
    print(f'Processed {line_count} lines.')