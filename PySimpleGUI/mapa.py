import PySimpleGUI as sg
import webbrowser

def crearVentanaMapa():
    layout = [
        [sg.Button("Mapa", key="botón mapa")],
        [sg.Button("Video", key="botón video")]
        ]
    return sg.Window("Ejemplo actividad", layout, finalize=True)

ventanaMapa = crearVentanaMapa()

while True:
    window, event, values = sg.read_all_windows()
    if event == sg.WINDOW_CLOSED:
        window.close()
        break
    elif event == "botón mapa":
        webbrowser.open("https://www.google.com/maps/d/edit?mid=1kd16HOIgg_1Cwe1Z2hsEV7HXAjg8S-w&usp=sharing")
    elif event == "botón video":
        webbrowser.open("")