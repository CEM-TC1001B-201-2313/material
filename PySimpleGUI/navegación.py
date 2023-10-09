import PySimpleGUI as sg
import pandas as pd

def crearVentanaLogin():
    col1 = sg.Column([
        [sg.Text("Email")],
        [sg.Text("Contraseña")],
        [sg.Button("Ingresar", key="botón ingresar")]
        ])
    col2 = sg.Column([
        [sg.Input(key="input email")],
        [sg.Input(key="input password", password_char="*")],
        [sg.Button("Registro", key="botón registrar")]
        ])
    layout = [
        [col1, col2]
        ]
    return sg.Window("Inicio de sesión", layout, finalize=True)

def crearVentanaRegistro():
    col1 = sg.Column([
        [sg.Text("Nombre")],
        [sg.Text("Apellido paterno")],
        [sg.Text("Apellido materno")],
        [sg.Text("Email")],
        [sg.Text("Contraseña")],
        [sg.Text("Repetir contraseña")],
        [sg.Text("Recibir notificaciones")]
        ])
    col2 = sg.Column([
        [sg.Input(key="input nombre")],
        [sg.Input(key="input apellido paterno")],
        [sg.Input(key="input apellido materno")],
        [sg.Input(key="input email")],
        [sg.Input(key="input contraseña")],
        [sg.Input(key="input repetir contraseña")],
        [sg.Radio("Sí",
                  key="radio sí",
                  default=True,
                  group_id="radio notificaciones"),
         sg.Radio("No",
                  key="radio no",
                  group_id="radio notificaciones")]
        ])
    layout = [
        [col1, col2],
        [sg.Button("Volver", key="botón volver"),
         sg.Button("Registrar", key="botón registrar")]
        ]
    return sg.Window("Registro de usuario", layout, finalize=True)

def crearVentanaMenuPrincipal():
    layout = [
        [sg.Image("panda.png")],
        [sg.Button("Salir", key="botón salir")]
        ]
    return sg.Window("Menú principal", layout, finalize=True)
    
ventanaLogin = crearVentanaLogin()
ventanaRegistro = None
ventanaMenuPrincipal = None

while True:
    window, event, values = sg.read_all_windows()
    if event == sg.WINDOW_CLOSED:
        window.close()
        break
    # Para ir a otra ventana, preguntamos:
    # ¿En qué ventana estamos?
    # ¿Qué botón se oprimió?
    # ¿La ventana a la que vamos está cerrada (None)?
    # Entonces hacer:
    # Cerrar la ventana actual.
    # Igualar la ventana actual a None
    # Abrir la nueva ventana usando su función
    
    # ventanaLogin ("botón ingresar") -> ventanaMenuPrincipal
    elif window == ventanaLogin and \
         event == "botón ingresar" and \
         ventanaMenuPrincipal is None:
        window.close()
        ventanaLogin = None
        ventanaMenuPrincipal = crearVentanaMenuPrincipal()
    # ventanaLogin ("botón registrar") -> ventanaRegistro
    elif window == ventanaLogin and \
         event == "botón registrar" and \
         ventanaRegistro is None:
        window.close()
        ventanaLogin = None
        ventanaRegistro = crearVentanaRegistro()
    # ventanaRegistro ("botón volver") -> ventanaLogin
    elif window == ventanaRegistro and \
         event == "botón volver" and \
         ventanaLogin is None:
        window.close()
        ventanaRegistro = None
        ventanaLogin = crearVentanaLogin()
    # ventanaRegistro ("botón registrar") -> ventanaMenuPrincipal
    elif window == ventanaRegistro and \
         event == "botón registrar" and \
         ventanaMenuPrincipal is None:
        window.close()
        ventanaRegistro = None
        ventanaMenuPrincipal = crearVentanaMenuPrincipal()
        