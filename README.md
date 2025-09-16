# 🎮 Cuatro en Raya — Juego en consola con Python

Este proyecto es una implementación del clásico juego *Cuatro en Raya* (Connect 4) en consola, desarrollado en Python. El objetivo es que dos jugadores alternen turnos para insertar fichas en un tablero, tratando de formar una línea de cuatro fichas consecutivas en horizontal, vertical o diagonal.

---

## 🧠 ¿Qué hace esta aplicación?

- Permite al usuario definir el tamaño del tablero (filas y columnas).
- Alterna turnos entre dos jugadores (X y Y).
- Inserta fichas en la columna elegida, simulando la caída desde la parte superior.
- Verifica condiciones de victoria por fila, columna y diagonales.
- Detecta empate si se llena el tablero sin que nadie gane.
- Limpia la pantalla en cada turno para mejorar la experiencia visual (solo en terminales reales).

---

## 🧪 Conceptos técnicos aplicados

Este proyecto utiliza varios fundamentos de programación:

- **Listas anidadas** para representar el tablero como una matriz.
- **Ciclos `for` y `while`** para recorrer el tablero y controlar el flujo del juego.
- **Condicionales `if`, `elif`, `else`** para validar jugadas, detectar errores y alternar turnos.
- **Funciones modulares** como `crear_tablero`, `introducir_fichas`, `revisar_ganador`, que permiten mantener el código organizado y reutilizable.
- **Iteraciones controladas** para revisar patrones de 4 fichas consecutivas en distintas direcciones.
- **Control de errores** para evitar inserciones fuera de rango o en columnas llenas.

---

## 🛠️ Proceso de desarrollo y depuración

Durante el desarrollo se enfrentaron varios retos técnicos:

- **Validación de columnas fuera de rango**: se corrigió el error que ocurría al intentar insertar en una columna inválida.
- **Evitar sobrescribir el tablero con `None`**: se ajustó el flujo para que solo se actualice el tablero si la jugada fue válida.
- **Separación de condiciones de victoria y empate**: se reorganizó la lógica para evitar que se imprimiera “empate” incluso cuando había un ganador.
- **Limpieza de pantalla**: se agregó una función que usa `os.system` para limpiar la consola en cada turno (no funciona en IDLE, pero sí en terminales reales).

Cada mejora fue pensada para hacer el código más robusto, legible y profesional.

---

## 🚀 Cómo ejecutar el juego

1. Asegúrate de tener Python instalado.
2. Ejecuta el archivo en una terminal (no en IDLE si quieres ver la limpieza de pantalla).
3. Sigue las instrucciones en consola para definir el tablero y jugar.

```bash
python cuatro_en_raya.py

