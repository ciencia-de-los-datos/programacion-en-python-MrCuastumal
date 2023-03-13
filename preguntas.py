"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

datos = open("data.csv", "r").readlines()
datos = [z.replace("\t", " ") for z in datos]
datos = [z.replace("\n", "") for z in datos]
datos = [z.split(" ") for z in datos]

def pregunta_01():
    colum_dos= ([z[1] for z in datos[0:]])
    colum_dos_int = ([int(x) for x in colum_dos])
    suma_de_notas = 0
    for nota in colum_dos_int:
        suma_de_notas  += nota
    return suma_de_notas


def pregunta_02():
    colum_uno= [z[0] for z in datos[0:]]
    duplicados=sorted(set(colum_uno))
    listatuplas= [(j,colum_uno.count(j))for j in duplicados]
    return listatuplas


def pregunta_03():
    suma_por_letra = {}
    for fila in datos:
        letra = fila[0]
        valor = int(fila[1])
        suma_por_letra[letra] = suma_por_letra.get(letra, 0) + valor
    resultado = sorted([(letra, suma) for letra, suma in suma_por_letra.items()])
    return resultado


def pregunta_04():
    colum_tres= [z[2] for z in datos[0:]]
    fechas = []
    for linea in colum_tres:
        fecha = linea.strip().split(',')[0]
        fechas.append(fecha)
    registros_por_mes = {}
    for fecha in fechas:
        año, mes, dia = fecha.split('-')
        if mes in registros_por_mes:
            registros_por_mes[mes] += 1
        else:
            registros_por_mes[mes] = 1
    tuplas_por_mes = [(mes, registros_por_mes[mes]) for mes in registros_por_mes]     
    tuplas_por_mes_ordenadas =sorted(tuplas_por_mes, key=lambda tupla: tupla[0])

    return tuplas_por_mes_ordenadas


def pregunta_05():
    x = {}
    for row in datos:
        letra = row[0]
        value = float(row[1])
        if letra not in x:
            x[letra] = (value, value)
        else:
            maximo, minimo = x[letra]
            if value > maximo:
                x[letra] = (value, minimo)
            elif value < minimo:
                x[letra] = (maximo, value)

    tupla = [(letra, int(valor[0]), int(valor[1])) for letra, valor in x.items()]
    tuplas_ordenadas =sorted(tupla, key=lambda tupla: tupla[0])
    
    return tuplas_ordenadas


def pregunta_06():
    colum_cinco= [z[4] for z in datos[0:]]
    diccionario= {"aaa": [float('inf'), float('-inf')],
            "bbb": [float('inf'), float('-inf')],
            "ccc": [float('inf'), float('-inf')],
            "ddd": [float('inf'), float('-inf')],
            "eee": [float('inf'), float('-inf')],
            "fff": [float('inf'), float('-inf')],
            "ggg": [float('inf'), float('-inf')],
            "hhh": [float('inf'), float('-inf')],
            "iii": [float('inf'), float('-inf')],
            "jjj": [float('inf'), float('-inf')]}

    for columna in colum_cinco:
        items = columna.split(',')
        for item in items:
            key, valor = item.split(':')
            valor = int(valor)
            if valor < diccionario[key][0]:
                diccionario[key][0] = valor
            if valor > diccionario[key][1]:
                diccionario[key][1] = valor
    result_list = sorted([(key, diccionario[key][0], diccionario[key][1]) for key in diccionario])

    return result_list


def pregunta_07():
    colum_uno= [z[0] for z in datos[0:]]
    colum_dos= ([z[1] for z in datos[0:]])
    diccionario = {}
    for valor, letra in zip(colum_dos, colum_uno):
        if valor not in diccionario:
            diccionario[valor] = [letra]
        else:
            diccionario[valor].append(letra)

    lista_tuplas = sorted([(int(x), y) for x, y in diccionario.items()])
    return lista_tuplas


def pregunta_08():
    colum_uno= [z[0] for z in datos[0:]]
    colum_dos= ([z[1] for z in datos[0:]])
    diccionario = {}
    for valor, letra in zip(colum_dos, colum_uno):
        if valor not in diccionario:
            diccionario[valor] = [letra]
        else:
            diccionario[valor].append(letra)

    lista_tuplas = sorted([(int(x), sorted(set(y))) for x, y in diccionario.items()])
    return lista_tuplas


def pregunta_09():
    colum_cinco= [z[4] for z in datos[0:]]
    resultados = {}
    for linea in colum_cinco:
        subcadenas = linea.split(",")
        for subcadena in subcadenas:
            clave, valor = subcadena.split(":")
            if clave in resultados:
                resultados[clave] += 1
            else:
                resultados[clave] = 1

    tupla = sorted({(clave, resultados[clave]) for clave in resultados})
    diccionarios = {key: value for key, value in tupla}
    
    return diccionarios


def pregunta_10():
    colum1= [z[0] for z in datos[0:]]
    colum4= [z[3] for z in datos[0:]]
    colum5= [z[4] for z in datos[0:]]
    result = []
    for i in range(len(colum1)):
        letra = colum1[i]
        elementos_col4 = colum4[i].split(',')
        cantidad_col5 = len(colum5[i].split(','))
        tupla = (letra, len(elementos_col4), cantidad_col5)
        result.append(tupla)

    return result


def pregunta_11():
    colum2= [z[1] for z in datos[0:]]
    colum4= [z[3] for z in datos[0:]]
    suma_por_letra = {}
    for letra, numero in zip(colum4, colum2):
        numeros = [int(x) for x in numero.split(",")]
        for letra in letra.split(","):
            if letra in suma_por_letra:
                suma_por_letra[letra] += sum(numeros)
            else:
                suma_por_letra[letra] = sum(numeros)

    suma_por_letra_ordenada = dict(sorted(suma_por_letra.items()))
    
    return suma_por_letra_ordenada


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    return
