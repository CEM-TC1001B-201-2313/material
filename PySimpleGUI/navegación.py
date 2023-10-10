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
        [sg.Input(key="input contraseña",
                  password_char="*")],
        [sg.Input(key="input repetir contraseña",
                  password_char="*")],
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
    if event == sg.WINDOW_CLOSED or event == "botón salir":
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
        df = pd.read_csv("usuarios.csv")
        usuario = df[(df["Email"] == values["input email"]) &
                     (df["Contraseña"] == values["input password"])]
        if len(usuario) > 0:
            window.close()
            ventanaLogin = None
            ventanaMenuPrincipal = crearVentanaMenuPrincipal()
        else:
            sg.Popup("El usuario o contraseña son incorrectos",
                     title="Error de inicio de sesión")
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
        
        if len(values["input email"]) == 0 or \
           values["input contraseña"] != values["input repetir contraseña"]:
            sg.Popup("Error en el registro. Compruebe sus datos.",
                     title = "Error en registro")
        else:
        
            if values["radio sí"]:
                notificaciones = "sí"
            else:
                notificaciones = "no"
            usuario = pd.DataFrame({
                "Nombre": [values["input nombre"]],
                "Apellido Paterno": [values["input apellido paterno"]],
                "Apellido Materno": [values["input apellido materno"]],
                "Email": [values["input email"]],
                "Contraseña": [values["input contraseña"]],
                "Recibir Notificaciones": [notificaciones]
                })
            
            df = pd.read_csv("usuarios.csv")
            df = pd.concat([df, usuario], ignore_index=True)
            df.to_csv("usuarios.csv", index=False)
            
            sg.Popup("¡Usuario creado exitosamente!",
                     title = "Registro correcto.")
            
            window.close()
            ventanaRegistro = None
            ventanaMenuPrincipal = crearVentanaMenuPrincipal()
        
