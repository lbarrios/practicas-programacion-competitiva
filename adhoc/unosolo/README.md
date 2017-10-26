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
N   X X X 2 4 3 X ...
N+1 X X X 1 6 5 X ...
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

## Input
El input es un K tal que `1 <= K <= 5`.

## Output
El output es un R tal que R es la cantidad **mínima** de fichas 
necesarias para que, acorde a la descripción del problema,
se pueda llegar hasta la fila N-K a través de una sucesioń de
comidas de fichas.

## Ejemplo de Input
```
1
```

## Ejemplo de Output
```
2
```