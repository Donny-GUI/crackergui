import os
import PySimpleGUI as sg
import shutil

def gui():
    layout = [
        [sg.StatusBar("\t\t\t\t",key='STATUS'),sg.FileBrowse(size=(100,100),key='FILE'), sg.Submit()], 
        [sg.Exit()]]
    window = sg.Window('get file', layout)
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Submit':
            window.close()
            print(values['FILE'])
            dirs = f"{os.getcwd()}/target"
            shutil.copy(src=str(window['STATUS']), dst=dirs)
            return values['FILE']
        if event == 'FILE':
            event, values = window.read()
            window['STATUS'].update(values['FILE'])

gui()
exit()

def get_target_pdf():
    file = sg.FileBrowse()
    location = f"{os.getcwd()}/target"
    shutil.copy(src=file, dst=location)
    return f'{os.getcwd()}/target'

def remove_text_objects(target):
    with open(target, 'r') as readfile:
        lines = [x.strip("\n") for x in readfile.readlines()]
        newlines = [x for x in lines if x[0:2] not in ['<<', 'XO', '00', '>>', 'en', 'st', '']]
        print(newlines)
    
tar = get_target_pdf()
