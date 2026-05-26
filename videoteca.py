# --- PROGRAMA VIDEOTECA Y CIA ---
# Nombre del estudiante: Leonardo Ortiz Hurtado
#Grupo:213022_95
#Codigo Fuente: Autoria Propia

def contar_titulos_destacados(matriz_videoteca, año_minimo, calificacion_minima):
    # Cuenta la cantidad de títulos en la videoteca que cumplen con los criterios
    # de año de lanzamiento y calificación mínima (reciente y popular).
    #
    # Argumentos:
    #     matriz_videoteca (list): Matriz con los datos [Título, Año, Calificación, Género].
    #     año_minimo (int): Año a partir del cual se considera "reciente".
    #     calificacion_minima (float): Puntuación a partir de la cual se considera "popular".
    #
    # Retorno:
    #     int: Cantidad de títulos que cumplen los criterios.
    contador = 0
    # A continuación comienza el bucle que recorre cada material de la videoteca
    for material in matriz_videoteca:
        titulo = material[0]
        año = material[1]
        calificacion = material[2]
        genero = material[3]
        
        if año >= año_minimo and calificacion >= calificacion_minima:
            contador += 1
            print(f"- Encontrado: '{titulo}' ({año}) | Calificación: {calificacion} | Género: {genero}")
            
    return contador

#Matrix que representa la videoteca digital, con títulos, año de lanzamiento, calificación y género.
if __name__ == "__main__":
    videoteca = [
        ["Dune: Parte Dos", 2024, 8.8, "Ciencia Ficción"],
        ["Oppenheimer", 2023, 8.4, "Drama"],
        ["El Padrino", 1972, 9.2, "Crimen"],
        ["Madame Web", 2024, 3.8, "Acción"],
        ["Pobres Criaturas", 2023, 8.0, "Comedia"],
        ["Interestelar", 2014, 8.6, "Ciencia Ficción"],
        ["Super mario bros: La pelicula", 2023, 8.6, "Animación"],
        ["The Matrix", 1999, 8.7, "Acción"],
        ["Avatar: El Camino del Agua", 2022, 7.6, "Ciencia Ficción"],
        ["Todo en Todas Partes al Mismo Tiempo", 2022, 8.1, "Aventura"]
    ]
# Fin de la definición de la lista de películas de la videoteca
    AÑO_CRITERIO = 2022
    CALIFICACION_CRITERIO = 8.0

    print("=== Análisis de Videoteca Digital ===")
    print(f"Buscando material reciente (>= {AÑO_CRITERIO}) y popular (>= {CALIFICACION_CRITERIO})...\n")

    total_encontrados = contar_titulos_destacados(videoteca, AÑO_CRITERIO, CALIFICACION_CRITERIO)

    print(f"\nTotal de títulos que satisfacen los criterios: {total_encontrados}")
