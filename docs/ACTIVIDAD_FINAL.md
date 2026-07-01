# Actividad final: rescate en un mapa con obstáculos

## Situación
Una persona debe llegar desde un punto de inicio `S` hasta una zona segura `G`. El mapa contiene obstáculos representados con `#`. Cada equipo debe diseñar un mapa y probar BFS, DFS y A*.

## Tarea

1. Crear un mapa de al menos 8 filas por 8 columnas.
2. Incluir mínimo 10 obstáculos.
3. Ejecutar BFS, DFS y A*.
4. Comparar los caminos encontrados.
5. Activar modo `debug=True` en al menos un algoritmo.
6. Explicar qué algoritmo fue más conveniente y por qué.

## Producto esperado
El repositorio debe incluir:

- Archivo `.txt` con el mapa.
- Código Python funcional.
- Captura o salida de consola.
- Tabla comparativa.

## Tabla comparativa

| Algoritmo | ¿Encontró camino? | Longitud del camino | Observación |
|---|---|---:|---|
| BFS |  |  |  |
| DFS |  |  |  |
| A* |  |  |  |

## Reflexión final
Escribe un párrafo de 150 a 250 palabras respondiendo:

- ¿Cuál fue el error más difícil de depurar?
- ¿Qué aprendiste sobre frontera, visitados y padres?
- ¿Por qué A* puede ser más eficiente que BFS?

## Ejemplo de reflexión
Durante el taller, el error más difícil de depurar fue comprender por qué el algoritmo volvía a visitar posiciones que ya habían sido revisadas. Al principio parecía que el mapa estaba mal, pero el problema real estaba en el manejo de los visitados. Aprendí que la frontera representa los nodos pendientes de explorar, mientras que los visitados sirven para evitar ciclos y repeticiones innecesarias. También entendí que el diccionario de padres es esencial porque permite reconstruir el camino final desde la meta hasta el inicio. Sin padres, el algoritmo puede encontrar la meta, pero no puede explicar cómo llegó hasta ella. Al comparar BFS, DFS y A*, observé que BFS encuentra caminos cortos cuando todos los movimientos tienen el mismo costo, pero puede explorar muchas posiciones. DFS puede encontrar una solución, aunque no siempre la mejor. A* puede ser más eficiente porque usa una heurística, como la distancia Manhattan, para acercarse a la meta con mayor intención y explorar menos zonas irrelevantes del mapa.
