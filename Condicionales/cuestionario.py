respuestas_si = 0

print("Para las siguientes preguntas, responde sí o no.")

# strip() -> Quita los espacios vacíos al inicio y al final de mi string
# "      sí   " -> "sí"
# lower() -> Convierte el contenido del string a minúsculas
pregunta = input("¿Actúas ética e irreprochablemente en tu trabajo?: ").strip().lower()

#if pregunta == "sí" or pregunta == "si":
if pregunta in ["sí", "si"]:
    #respuestas_si = respuestas_si + 1
    respuestas_si += 1
    
print("Para las siguientes preguntas responda 1 para sí y 2 para no")
pregunta = int(input("¿Actúas ética e irreprochablemente en tu trabajo?: "))

if pregunta == 1:
    #respuestas_si = respuestas_si + 1
    respuestas_si += 1

print(f"Respondió sí: {respuestas_si} veces.")