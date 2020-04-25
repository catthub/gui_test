import PySimpleGUI as sg

sg.theme("BluePurple")

layout = [
   [sg.Text("Your typed chars appear here:"), sg.Text(size=(15, 1), key="-OUTPUT-")],
   [sg.Input(key="-IN-")],
   [sg.Button("Show"), sg.Button("Exit")],
]

window = sg.Window("Pattern 2B", layout)

while True:  # Event Loop
   event, values = window.read()
   print(event, values)
   if event in (None, "Exit"):
       break
   if event == "Show":
       # "-OUTPUT-" 要素を "-IN-" 要素の値に更新
       window["-OUTPUT-"].update(values["-IN-"])

window.close()
