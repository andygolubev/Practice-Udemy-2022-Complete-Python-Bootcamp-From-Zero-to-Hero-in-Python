from modules import functions
import PySimpleGUI
import tkinter

label = PySimpleGUI.Text("Type in ToDo:")
input_text = PySimpleGUI.InputText(tooltip="Enter ToDo")

window = PySimpleGUI.Window('My simple GUI', layout=[[label, input_text]])
window.read()
window.close()