import csv

def read_csv(path, columna_name):
  columna_values = []
  
  with open(path, 'r') as csvfile:
    reader = csv.DictReader(csvfile,)
    
    for row in reader:
      columna_values.append(row[columna_name])
  return columna_values


    
      

if __name__ == '__main__':
  data = read_csv('./app/data.csv', 'World Population Percentage')
  print(data)
