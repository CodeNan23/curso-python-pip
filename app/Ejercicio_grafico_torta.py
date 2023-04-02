import utils
import read_csv
import charts
import matplotlib.pyplot as plt #PLT ES UN ALIAS O SINONIMO DE PYPLOT

#obtenemois la data
def run():
    data = read_csv.read_csv('./app/data.csv')#le digo donde esta el csv que tiene que leer
    #Agrego un FILTRO para solo usar Sudamerica.
    data = list(filter(lambda item: item ['Continent'] == 'South America', data))
     #Selecciono columna de pais
    countries= list(map(lambda x: x['Country/Territory'], data))
#Selecciono columna de datos %
    percentages= list(map(lambda x: x['World Population Percentage'], data))
#este es el resultado:
    charts.generate_pie_chart(countries, percentages)

if __name__ == '__main__':
    run()


