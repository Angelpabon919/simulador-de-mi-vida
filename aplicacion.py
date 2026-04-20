import random
estado = {
    "energia": 70,
    "estres": 20,
    "dinero": 50,
    "responsabilidad": 50,
    "conocimiento": 0,
    "dia": 1
}
historial = []
logros = set()
opciones = ("1", "2", "3")

print("SIMULADOR DE MI VIDA (TRABAJO y  SENA)")
print("soy una joven de 18 años que trabaja cuidando a un abuelo y asiste al SENA por las noches. y tengo  5 días para equilibrar mi energía, estrés, dinero, responsabilidad y conocimiento")
while estado["energia"] > 0 and estado["estres"] < 100 and estado["dia"] <= 5:

    print(f"DÍA {estado['dia']}")
    print("Te levantas a las 5:30 a.m")

    print("¿Cómo empiezas el día?")
    print("1. Con buena actitud")
    print("2. con dolor de cabeza")
    opciones = input("Elige: ")

    if opciones == "1":
        estado["energia"] -= 5
        estado["responsabilidad"] += 10
        historial.append(f"Día {estado['dia']}: empezó el día con buena actitud")
    else:
        estado["energia"] -= 15
        estado["estres"] += 10
        historial.append(f"Día {estado['dia']}: empezó con dolor de cabeza")

    print("\nMañana: trabajo cuidando al abuelo")
    estado["energia"] -= 10
    estado["responsabilidad"] += 5

    evento = random.choice(["normal", "finca", "cita"])

    if evento == "finca":
        print("Hoy fueron a la finca ")
        estado["energia"] -= 15
        estado["estres"] += 5
        historial.append(f"Día {estado['dia']}: fue a la finca")
    elif evento == "cita":
        print("Acompañaste a una cita médica ")
        estado["estres"] += 10
        historial.append(f"Día {estado['dia']}: cita médica")
    else:
        historial.append(f"Día {estado['dia']}: día normal de trabajo")

    print("Tarde:")
    print("1. Hacer tareas ")
    print("2. Descansar ")
    print("3. Usar el celular ")

    op = input("Elige: ")

    if op == "1":
        estado["conocimiento"] += 15
        estado["estres"] += 5
        historial.append(f"Día {estado['dia']}: hizo tareas")
    elif op == "2":
        estado["energia"] += 10
        estado["estres"] -= 5
        historial.append(f"Día {estado['dia']}: descansó")
    else:
        estado["energia"] -= 5
        estado["conocimiento"] += 2
        historial.append(f"Día {estado['dia']}: usó el celular")

    print("Noche: ir al SENA (7:00 pm)")
    print("1. Ir al SENA ")
    print("2. No ir")

    opciones= input("Elige: ")

    if opciones == "1":
        estado["conocimiento"] += 20
        estado["energia"] -= 15
        estado["responsabilidad"] += 10
        historial.append(f"Día {estado['dia']}: fue al SENA")
    else:
        estado["estres"] += 10
        estado["responsabilidad"] -= 5
        historial.append(f"Día {estado['dia']}: no fue al SENA")

    if estado["conocimiento"] >= 50:
        logros.add("Avanzó en el SENA")

    if estado["responsabilidad"] >= 80:
        logros.add("Muy responsable")

    print("Estado actual:")
    for clave, valor in estado.items():  
        print(f"{clave}: {valor}")

    estado["dia"] += 1

print("RESULTADO FINAL")

if estado["energia"] <= 0:
    print("Te quedaste sin energía ")
elif estado["estres"] >= 100:
    print("El estrés fue demasiado ")
else:
    print("Lograste completar la semana ")

print("Historial:")
for h in historial:
    print("-", h)

print("Logros:")
for l in logros:
    print("-", l)