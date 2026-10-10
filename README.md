# Repo para EIEC - DevOps - UNIR

Este repositorio nos servirá para demostrar el uso de Git en la asignatura de EIEC y muchas cosas mas.

---

Los comandos del Makefile funcionarán en Linux y MacOS. En caso de usar Windows, necesitarás adaptarlos o ejecutarlos en una máquina virtual Linux.

## Ejecución

python3 main.py <filename> <dup> <order>
  filename: **ruta** al fichero que contiene la lista de palabras, una por línea
  dup: **yes|no**, yes para eliminar palabras duplicadas, no para mantener la lista

### Ejemplo de ejecución

Con un fichero `words.txt` que contiene:

```text
pear
apple
pear
```

Ejecuta la aplicación manteniendo las palabras duplicadas:

```console
$ python3 main.py words.txt no
Se leerán las palabras del fichero words.txt
['apple', 'pear', 'pear']
```

Para eliminar los duplicados, usa `yes` como segundo argumento:

```console
$ python3 main.py words.txt yes
Se leerán las palabras del fichero words.txt
['apple', 'pear']
```
