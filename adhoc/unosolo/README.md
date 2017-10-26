# UnoSolo

## Description (spanish)

### Juego "Uno Solo"
Existe un juego llamado "Uno Solo", en el que existe un tablero 
con forma de cruz, con la siguiente disposición.

```
    O O O    
    O O O    
O O O O O O O
O O O X O O O
O O O O O O O
    O O O    
    O O O    
```

En donde cada `O` es un casillero con una ficha, 
y la `X` del centro es un casillero vacío. 
El objetivo del juego es "comer" las fichas entre sí, 
de forma tal que al terminar queden todos los casilleros
vacíos, excepto el central, que debe quedar con una ficha.

```
    X X X    
    X X X    
X X X X X X X 
X X X O X X X 
X X X X X X X 
    X X X    
    X X X    
```

La forma de comer fichas es la siguiente: una ficha puede comer
a otra ficha que tenga a su lado (es decir, a la izquierda, la derecha,
arriba o abajo), siempre y cuando el siguiente casillero en esa misma
dirección esté vacío. Al comer una ficha, la ficha comida se saca del
tablero, y la otra se mueve a la posición siguiente en la misma dirección
en que se comió la ficha. 

```
    O O O    
    O O O    
O O O O O O O
O O O X 2 1 O
O O O O O O O
    O O O    
    O O O    
```

En el tablero de ejemplo (tablero inicial), se marca con 
un `1` a la ficha que come, y con un `2` a la ficha que es comida.

```
    O O O    
    O O O    
O O O O O O O
O O O 1 X X O
O O O O O O O
    O O O    
    O O O    
```

Luego, el tablero pasa a tener libres las posiciones donde
estaban las fichas `1` y `2`, y la ficha `1` pasa a estar
en la posición central.

### Problema

El problema está basado en la forma de comer de este juego,
pero se parte de un tablero infinito, y vacío. Se define
una fila N, y sólo se pueden poner fichas en cualquier fila M
tal que M>=N. El objetivo es encontrar la mínima cantidad de
fichas que hay que poner en el tablero, para que luego de
alguna sucesión de operaciones de "comer ficha", termine
habiendo una ficha en la fila N-K, para K entre 1 y 5.


#### Ejemplo de tablero inicial:

```
 .
 .
 .
N-3   X X X X X X X ...
N-2   X X X X X X X ...
N-1   X X X X X X X ...
  N   X X X X X X X ...
N+1   X X X X X X X ...
N+2   X X X X X X X ...
N+3   X X X X X X X ...
N+4   X X X X X X X ...
 .
 .
 .
```

#### Ejemplo de solución para K=1

```
.
.
.
N-3 X X X X X X X ...
N-2 X X X X X X X ...
N-1 X X X X X X X ...
N   X X X 2 X X X ...
N+1 X X X 1 X X X ...
N+2 X X X X X X X ...
N+3 X X X X X X X ...
N+4 X X X X X X X ...
.
.
.
```

**Ficha 1 come a 2.**

```
.
.
.
N-3 X X X X X X X ...
N-2 X X X X X X X ...
N-1 X X X 1 X X X ...
N   X X X X X X X ...
N+1 X X X X X X X ...
N+2 X X X X X X X ...
N+3 X X X X X X X ...
N+4 X X X X X X X ...
.
.
.
```

**Fin.**

**Respuesta: 2**

#### Ejemplo de solución para K=2

```
.
.
.
N-3 X X X X X X X ...
N-2 X X X X X X X ...
N-1 X X X X X X X ...
N   X X X 2 X X X ...
N+1 X X X 1 4 3 X ...
N+2 X X X X 6 5 X ...
N+3 X X X X X X X ...
N+4 X X X X X X X ...
.
.
.
```

**Ficha 1 come a 2.**

```
.
.
.
N-3 X X X X X X X ...
N-2 X X X X X X X ...
N-1 X X X 1 X X X ...
N   X X X X X X X ...
N+1 X X X X 3 4 X ...
N+2 X X X X 6 5 X ...
N+3 X X X X X X X ...
N+4 X X X X X X X ...
.
.
.
```

**Ficha 3 come a 4.**

**Ficha 5 come a 6.**

```
.
.
.
N-3 X X X X X X X ...
N-2 X X X X X X X ...
N-1 X X X 1 X X X ...
N   X X X X X X X ...
N+1 X X X 6 X X X ...
N+2 X X X 4 X X X ...
N+3 X X X X X X X ...
N+4 X X X X X X X ...
.
.
.
```

**La ficha 4 come a 6.**

```
.
.
.
N-3 X X X X X X X ...
N-2 X X X X X X X ...
N-1 X X X 1 X X X ...
N   X X X 4 X X X ...
N+1 X X X X X X X ...
N+2 X X X X X X X ...
N+3 X X X X X X X ...
N+4 X X X X X X X ...
.
.
.
```

**La ficha 4 come a 1.**

```
.
.
.
N-3 X X X X X X X ...
N-2 X X X 4 X X X ...
N-1 X X X X X X X ...
N   X X X X X X X ...
N+1 X X X X X X X ...
N+2 X X X X X X X ...
N+3 X X X X X X X ...
N+4 X X X X X X X ...
.
.
.
```

**Fin.**

**Respuesta: 6**

### Input
El input es un K tal que `1 <= K <= 5`.

### Output
El output es un R tal que R es la cantidad **mínima** de fichas 
necesarias para que, acorde a la descripción del problema,
se pueda llegar hasta la fila N-K a través de una sucesioń de
comidas de fichas.

### Ejemplo de Input
```
1
```

### Ejemplo de Output
```
2
```


## Solución

La idea sería poder simular de algún modo el progreso del juego, 
para encontrar el tablero inicial mínimo tal que se pueda llegar
al estado deseado.

Lo ideal sería poder encontrar un algoritmo greedy, que restringido
a un determinado set de reglas y movimientos, pueda generar un
tablero inicial mínimo, dado un determinado tablero resultado.

Ejemplo, para K=1,
```
.
.
.
N-3 X X X X X X X ...
N-2 X X X X X X X ...
N-1 X X X 1 X X X ...
N   X X X X X X X ...
N+1 X X X X X X X ...
N+2 X X X X X X X ...
N+3 X X X X X X X ...
N+4 X X X X X X X ...
.
.
.
```

Dado el tablero final, el algoritmo podría ir "extendiéndolo",
hasta encontrar un tablero inicial que cumpla con que no exista
ninguna ficha en una fila que esté arriba de N. En este caso,
la extensión buscada sería reemplazar la ficha 1, por dos fichas
1 y 2, que se encuentren debajo de 1.

```
.
.
.
N-3 X X X X X X X ...
N-2 X X X X X X X ...
N-1 X X X X X X X ...
N   X X X 2 X X X ...
N+1 X X X 1 X X X ...
N+2 X X X X X X X ...
N+3 X X X X X X X ...
N+4 X X X X X X X ...
.
.
.
```

En líneas generales, una ficha 1 puede haber provenido de los siguientes
estados.

### Comer Arriba

Estado anterior
```
X X X
X 2 X
X 1 X
```

Luego de comer
```
X 1 X
X X X
X X X
```

### Comer Izquierda

Estado anterior
```
X X X X X
X X 2 1 X
X X X X X
```

Luego de comer
```
X X X X X
X 1 X X X
X X X X X
```

### Comer Derecha

Estado anterior
```
X X X X X
X 1 2 X X
X X X X X
```

Luego de comer
```
X X X X X
X X X 1 X
X X X X X
```

### Comer Abajo

Estado anterior
```
X 1 X
X 2 X
X X X
```

Luego de comer
```
X X X
X X X
X 1 X
```

En este caso, no interesa ninguno de los tableros que ya tenían
una ficha en una fila que esté arriba de la deseada, ya que 
para llegar a esa fila, necesariamente pasaron por la fila deseada.
Es decir, que **no** interesa analizar el movimiento ```COMER ABAJO```.

Entonces, dado un tablero, el mismo pudo provenir de tres tableros 
posibles. Aquel surgido de una operación 
de {comer arriba, comer izquierda, comer derecha}. Para mayor comodidad,
llamemos a estas operaciones A, I, D.

El primer intento que se puede hacer, entonces, es un algoritmo
por fuerza bruta, que vaya analizando el conjunto de soluciones,
iterando sobre el tablero final, mediante aplicaciones 
del inverso de las 3 operaciones permitidas. Para evitar confusiones,
el nombre de las operaciones lo haremos de forma espejada. Es decir,
Reverso(A) = RD. Reverso(I) = RD. Reverso(D) = RI.

### RD (reemplazar una ficha por dos debajo)

Estado anterior
```
O
X
X
```

Luego de comer
```
X
O
O
```

### RI (reemplazar una ficha por dos a la izquierda)

Estado anterior
```
X X O
```

Luego de comer
```
O O X
```

### RD (reemplazar una ficha por dos a la derecha)

Estado anterior
```
O X X
```

Luego de comer
```
X O O
```

Es claro que en cada iteración, la cantidad de posibles 
soluciones analizadas se multiplica por 3. La complejidad de
resolver el problema de este modo es, entonces, exponencial O(n^3).