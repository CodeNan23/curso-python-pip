import matplotlib.pyplot as plt #PLT ES UN ALIAS O SINONIMO DE PYPLOT


def generate_bar_chart(labels, values):
    fig, ax = plt.subplots() #FIG (FIGURA, AX SON LAS COORDENADAS) SUBPLOTSes un metodo 
    ax.bar(labels, values) # utilizadno ax digo que el grafico es BAR (barras) Aqui le indico los valores
    plt.show()

def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis ('equal') #estoy indicando que sea centrado.
    plt.show()
if __name__ == '__main__':
    labels= ["a","b","c"]
    values= [50,500,300]
    generate_bar_chart(labels, values)
    generate_pie_chart(labels, values)
    