import PySimpleGUI as sg

sg.theme("DarkTeal")

def crearVentanaPrincipal():
    lista_vacunas = [
        "Pfizer",
        "Moderna",
        "AstraZeneca",
        "Sputnik",
        "Cansino"
        ]
    lista_recomendacion = [
        "Muy recomendado",
        "Recomendado",
        "Nada recomndado"
        ]
    layout = [
        # Text
        [sg.Text("Mi primera ventana",
                 font = "Arial 30",
                 text_color = "blue",
                 background_color = "white")],
        # Button
        [sg.Button("Soy un botón",
                   key = "botón 1",
                   image_filename = "panda.png"),
         sg.Button("Otro botón",
                   key = "botón 2")],
        # Input
        [sg.Text("Email"),
         sg.Input(key = "input email")],
        [sg.Text("Contraseña"),
         sg.Input(key = "input contraseña",
                  password_char="*")],
        # Radio
        [sg.Text("¿Te aplicaste la vacuna?"),
         sg.Radio("Sí",
                  key = "radio sí",
                  group_id = "grupo vacuna",
                  enable_events = True),
         sg.Radio("No",
                  key = "radio no",
                  group_id = "grupo vacuna",
                  default = True,
                  enable_events = True)],
        # Combo
        [sg.Text("Marca de la vacuna"),
         sg.Combo(lista_vacunas,
                  key = "combo vacunas",
                  default_value = "Pfizer",
                  disabled = True)],
        # Checkbox
        [sg.Text("Síntomas"),
         sg.Checkbox("Fiebre",
                     key = "checkbox fiebre"),
         sg.Checkbox("Dolor de cabeza",
                     key = "checkbox dolor de cabeza"),
         sg.Checkbox("Tos",
                     key = "checkbox tos")],
        # Slider
        [sg.Text("Nivel se satisfacción"),
         sg.Slider(range=(1,5),
                   key = "slider satisfacción",
                   orientation = "horizontal",
                   default_value = 3)],
        # Spin
        [sg.Text("¿Recomendarías esta aplicación?"),
         sg.Spin(lista_recomendacion,
                 key = "spin recomendación",
                 initial_value = "Recomendado")],
        # Image
        [sg.Image("panda.png")]
        ]
    return sg.Window("Mi primer título", layout, finalize=True)

ventanaPrincipal = crearVentanaPrincipal()

while True:
    window, event, values = sg.read_all_windows()
    if event == sg.WINDOW_CLOSED:
        window.close()
        break
    elif event == "botón 1":
        print("Di click en mi primer botón.")
        email = values["input email"]
        contraseña = values["input contraseña"]
        print(f"Email: {email} - Password: {contraseña}")
        print(f"Vacuna sí: {values['radio sí']}")
        print(f"Vacuna no: {values['radio no']}")
        print(f"Marca de la vacuna: {values['combo vacunas']}")
        print(f"Fiebre: {values['checkbox fiebre']}")
        print(f"Dolor de cabeza: {values['checkbox dolor de cabeza']}")
        print(f"Tos: {values['checkbox tos']}")
        if values["checkbox fiebre"]:
            print("Tiene fiebre")
        print(f"Nivel de satisfacción: {values['slider satisfacción']}")
        print(f"Recomendación: {values['spin recomendación']}")
    elif event == "botón 2":
        sg.Popup("Ejemplo de popup", title="Título")
    elif event == "radio sí":
        window["combo vacunas"].update(disabled = False)
    elif event == "radio no":
        window["combo vacunas"].update(disabled = True)