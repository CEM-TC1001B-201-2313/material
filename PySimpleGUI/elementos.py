import PySimpleGUI as sg

def crearVentanaPrincipal():
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
                  password_char="*")]
        # Radio
        # Combo
        # Checkbox
        # Slider
        # Spin
        # Image
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
    elif event == "botón 2":
        sg.Popup("Ejemplo de popup", title="Título")