import csv
fields=[['Name','Place']]
rows=[['Amrutha','Piravom'],
      ['Aswathy','Muvattupuzha'],
      ['Karthika','Thodupuzha']]
with open('data.csv','w') as file:
    writer=csv.writer(file)
    writer.writerows(fields)
    writer.writerows(rows)
print("CSV file has been created ")
