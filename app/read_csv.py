import csv

def read_csv(path):
    with open(path, 'r') as csvfile: #csvfile es el tipo de archivo con el que trabajamos (csv)
        reader = csv.reader(csvfile, delimiter=',')
        header= next(reader)
            #Vamos a crear un lector del csv, 
#csv es un módulo de python, y tiene la función reader que lee las líneas del csvfile proporcionado.
#delimiter es la forma en la que vienen separados los datos del archivo, en este caso son comas
        data=[]
        for row in reader:  #row es la cantidad de filas que tiene el documento
            iterable = zip(header, row) #zip es un iterador que intercala los elementos de dos interables y los devulve como tuplas.
            country_dict = {key:value for key, value in iterable}
            data.append(country_dict)
        return data
if __name__ == '__main__':
    data = read_csv('./app/data.csv')
    print(data[0])
