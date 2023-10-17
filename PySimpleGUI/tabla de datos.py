import pandas as pd
import PySimpleGUI as sg

def crearVentanaTabla():
    df = pd.read_csv("datos.csv")
    encabezado = df.columns.tolist()
    contenido = df.head(10).values.tolist()
    promedio = df["Enero"].mean()
    layout = [
        [sg.Text("Ejemplo de ventana de datos")],
        [sg.Table(headings=encabezado,
                 values=contenido)],
        [sg.Text(f"El promedio del mes de enero fue de: {promedio:,.2f}")]
        ]
    return sg.Window("Tabla de datos", layout, finalize=True)

ventanaTabla = crearVentanaTabla()

while True:
    window, event, values = sg.read_all_windows()
    if event == sg.WINDOW_CLOSED:
        window.close()
        break