import csv
data=[{'Name':'Amrutha','Roll No':13},
      {'Name':'Aswathy','Roll No':20},
      {'Name':'Karthika','Roll No':33}
    ]
with open('data_dict1.csv','w') as file:
    fieldnames=['Name','Roll No']
    writer=csv.DictWriter(file,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)
print('Dictionary data has been written to the csv file ')
    
