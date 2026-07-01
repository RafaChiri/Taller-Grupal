# Taller BFS, DFS y A*

## Objetivo
Implementar y depurar algoritmos de búsqueda usando grafos y mapas de cuadrícula.

## Parte 1: Búsqueda en grafos
Un grafo puede representarse con un diccionario donde cada clave es un nodo y su valor es una lista de vecinos.

Ejemplo:

```python
graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E"],
    "D": ["G"],
    "E": ["G"],
    "G": []
}
```

Tareas:

1. Ejecutar BFS desde `A` hasta `G`.
2. Ejecutar DFS desde `A` hasta `G`.
3. Comparar los caminos encontrados.
4. Activar `debug=True` para observar la frontera y los visitados.

## Parte 2: Búsqueda en mapas
Un mapa se representa como texto:

- `S`: inicio.
- `G`: meta.
- `#`: obstáculo.
- `.`: camino libre.

Ejemplo:

```text
S.......
.###....
...#....
...#..G.
........
```

Tareas:

1. Cargar un mapa desde la carpeta `data`.
2. Ejecutar BFS, DFS y A*.
3. Dibujar el camino encontrado.
4. Validar que el camino no atraviese obstáculos.

## Parte 3: Depuración incremental
Antes de ejecutar todo el algoritmo completo, revisa:

1. Si el mapa carga correctamente.
2. Si encuentra `S` y `G`.
3. Si los vecinos generados son válidos.
4. Si la frontera cambia correctamente.
5. Si los padres permiten reconstruir el camino.

## Entrega
El estudiante debe entregar:

- Código funcional.
- Mapa propio de al menos 8x8.
- Mínimo 10 obstáculos.
- Salida de consola o captura.
- Tabla comparativa de BFS, DFS y A*.
- Reflexión final de 150 a 250 palabras.
