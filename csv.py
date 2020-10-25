
import csv

with open('files.csv', 'w') as w:
        writer = csv.writer(w)
        writer.writerow(column_names)
        writer.writerows(result)