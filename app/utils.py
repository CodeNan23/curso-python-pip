#def get_population():
 #   keys= ['col', 'bol']
  #  values = [300, 400]
   # return keys, values

#A = "Hola Gato"


# Creamos una formula para recibir los datos de toda una fila detallando las columnas que deseamos.
def get_population(country_dic):
    populations_dic={
        '2022':int(country_dic['2022 Population']),}
    # Opc 1
    labels = populations_dic.keys ()
    values = populations_dic.values()
    return labels, values
    #Opc 2
    #return populations_dic.keys (), populations_dic.values(),

def populations_by_country (data, country):
    result = list(filter(lambda item: item ['Country/Territory'] == country,  data ))
    return result

def get_row(country_dic):
    populations_dic={
        '2022':int(country_dic['2022 Population']),
        '2020':int(country_dic['2020 Population']),
        '2015':int(country_dic['2015 Population']),
        '2010':int(country_dic['2010 Population']),
        '2000':int(country_dic['2000 Population']),
        '1990':int(country_dic['1990 Population']),
        '1980':int(country_dic['1980 Population']),
        '1980':int(country_dic['1970 Population']),
    }
    # Opc 1
    labels = populations_dic.keys ()
    values = populations_dic.values()
    return labels, values
    #Opc 2
    #return populations_dic.keys (), populations_dic.values(),

def populations_by_country (data, country):
    result = list(filter(lambda item: item ['Country/Territory'] == country,  data ))
    return result

