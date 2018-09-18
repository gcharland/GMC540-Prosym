import csv
from provider import Provider
from company import Company

def read_csv(filename):
    output_array = []
    with open(filename + '.csv', 'r') as csvfile:
      reader = csv.reader(csvfile, delimiter=",", quotechar='"')
      for row in reader:
          output_array.append(row)

    return output_array

data_small = read_csv('petits_formats')
data_big = read_csv('grands_formats')

prix_A = read_csv('prix_A')
prix_B = read_csv('prix_B')
prix_C = read_csv('prix_C')

max_A = 80000
max_B = 150000
max_C = 0

delais_A = [[1, 2]]
delais_B = [[0.4, 1], [0.4, 2], [0.2, 3]]
delais_C = [[1, 1]]

cout_base_A = 0
cout_base_B = 1000
cout_base_C = 800

probabilite_A = [[0.2, 0.96], [0.3, 0.97], [0.3, 0.98], [0.2, 0.99]]
probabilite_B = [[0.5, 0.97], [0.5, 0.98]]
probabilite_C = [[1, 1]]

fournisseur_A = Provider(max_A, delais_A, cout_base_A, prix_A, probabilite_A)
fournisseur_B = Provider(max_B, delais_B, cout_base_B, prix_B, probabilite_B)
fournisseur_C = Provider(max_C, delais_C, cout_base_C, prix_C, probabilite_C)

compagnie = Company(1000, 0, 1000, 3)

compagnie.buy(fournisseur_A, 10000)


#for attr in dir(fournisseur_A):
#       if hasattr( fournisseur_A, attr ):
#           print( "obj.%s = %s" % (attr, getattr(fournisseur_A, attr)))
