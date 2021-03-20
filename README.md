# Proyecto 1 - Diseno de lenguajes
El objetivo del proyecto es la implementacion de 5 diferentes algoritmos para la creacion y simulacion de un automata.
1. Algoritmo de thompson: permite la creacion de un automata finito no determinista.
2. Construccion de subconjuntos: con el resultado de transicionde del automata finito no determinista, construye un automa finito determinista.
3. Creacion directa: dado una expresion regular, se genera su arbol sintactico y a traves de el se genera un automata finito determinista.
4. Simulacion de afn: ingresando una expresion a evaluar nos dice si es valida o no la expresion dentro del afn.
5. Simulacion de afd: ingresando una expresion a evaluar nos dice si es valida o no la expresion dentro del afd.


## Instalacion
Usar el manejador de paquetes [pip](https://pip.pypa.io/en/stable/) para instalar graphviz, libreria que se utiliza para graficar los automatas.

```bash
pip install graphviz
```

## Uso
Para utilizar el proyecto se necesita clonarlo y dirijirse a la direccion en donde se clono. Estando ahi se debera de correr el menu principal que permite la seleccion del algoritmo a utilizar.

```bash
python main.py
```

