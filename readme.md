 Simulador de Mi Vida (Trabajo y el SENA)
 Descripción
Esta aplicación es un simulador interactivo en consola basado en mi rutina diaria. Representa mi vida como trabajadora cuidando a un adulto mayor y estudiante del SENA.

El programa permite tomar decisiones durante el día (mañana, tarde y noche), las cuales afectan variables como energía, estrés, conocimiento, responsabilidad y dinero.

El objetivo es completar varios días manteniendo un equilibrio entre el trabajo, el estudio y el bienestar personal.

 Objetivo
Simular la toma de decisiones en la vida real y mostrar cómo influyen en el rendimiento académico, el trabajo y el estado físico y emocional.


 Instrucciones de ejecución

1. Tener Python instalado.
2. Descargar o clonar este repositorio.
3. Abrir una terminal en la carpeta del proyecto.
4. Ejecutar:

```bash
python aplicacion.py

Estructuras de datos utilizadas

Diccionario
para almacenar el estado del usuario:
energía
estrés
dinero
responsabilidad
conocimiento
día



Lista
 para guardar el historial de acciones realizadas durante cada día.


Tupla
para definir opciones fijas del programa.

Set 
para almacenar logros únicos.
Los sets evitan que se repitan los mismos logros.
 Estructuras de control
Ciclo while
Controla la ejecución del programa mientras:

haya energía
el estrés no sea demasiado alto
no se hayan terminado los días

Ciclo for
 para recorrer:
El estado del usuario
El historial de acciones
Los logros obtenidos

 Funcionalidades
Simulación de rutina diaria real
Toma de decisiones
Eventos aleatorios (finca, citas médicas)
Sistema de logros
Historial de acciones
Condiciones de victoria y derrota