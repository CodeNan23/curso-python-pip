import utils

data = [
{
'Country':'Colombia',
'Population': 500
},

{
'Country': 'Bolivia',
'Population': 300
}
]

def run ():
    pais, valor= utils.get_population()
    print(pais, valor)

    print (utils.A)

    country = input ('Type  Country ==>')

    result= utils.populations_by_country(data, 'Colombia')
    print (result)

# Este IF le dice al archivo "main.py" que si:
    #- Lo ejecuta desde la terminal lo ejecutas por el metodo run()!
    #- Pero si es ejecutado desde otro archivo, esto no se ejecutara
if __name__=='__main__':
    run()