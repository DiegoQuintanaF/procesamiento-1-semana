import matplotlib.pyplot as plt
import pandas as pd


paracaidista1 = {
    'masa_persona': 70,
    'arrastre': 12,
    'intervalo_tiempo': 0.2,
    'tiempo_final': 50,
    'identificador': 'paracaidista-1'
}

paracaidista2 = {
    'masa_persona': 75,
    'arrastre': 15,
    'intervalo_tiempo': 0.2,
    'tiempo_final': 50,
    'identificador': 'paracaidista-2'
}


def velocidad_paraicaidista(arrastre: float, masa_persona: float,
                            intervalo_tiempo: float, identificador: str, tiempo_final: float = 60) -> None:

    global velocidad_anterior
    global velocidad_actual

    data = open(f'{identificador}.csv', 'w')
    data.write('Tiempo;Velocidad;\n')

    lista_velocidades = [0.0]
    lista_tiempo = [0.0]

    velocidad_anterior = 0.0
    velocidad_actual = 0.0

    tiempo_actual = intervalo_tiempo
    while (tiempo_actual <= tiempo_final):
        velocidad_actual = round(
            velocidad_anterior + (9.8 - (arrastre/masa_persona)*velocidad_anterior)*intervalo_tiempo, 3)

        lista_velocidades.append(velocidad_actual)
        lista_tiempo.append(tiempo_actual)

        data.write(f'{tiempo_actual};{velocidad_actual};\n')

        velocidad_anterior = velocidad_actual
        tiempo_actual = round(tiempo_actual + intervalo_tiempo, 1)

    data.close()
    pd.read_csv(f'{identificador}.csv', sep=';')
    plt.plot(lista_tiempo, lista_velocidades)
    plt.xlabel('Tiempo')
    plt.ylabel('Velocidad')
    plt.title(f'Velocidad vs tiempo - {identificador}')
    plt.show()


velocidad_paraicaidista(**paracaidista1)
velocidad_paraicaidista(**paracaidista2)

