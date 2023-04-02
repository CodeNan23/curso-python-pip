import utils
import read_csv
import charts
import matplotlib.pyplot as plt #PLT ES UN ALIAS O SINONIMO DE PYPLOT

#obtenemois la data
def run():
    data = read_csv.read_csv('./app/data.csv')#le digo donde esta el csv que tiene que leer
    country= input ("Ingrese el pais==>:  ")
#este es el resultado:
    result= utils.populations_by_country(data, country)
#este if trabaja sobre el resultado devuelto
    if len(result) > 0:
        country = result [0]
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(labels, values)

if __name__ == '__main__':
    run()


