import PySimpleGUI as sg
import sys
import os
import shutil

def get_file():
    if len(sys.argv) == 1:
        event, values = sg.Window('Get Document',
                        [[sg.Text('Document to open')],
                        [sg.In(key='FILE'), sg.FileBrowse()],
                        [sg.Open(), sg.Cancel()]]).read()
        file = values['FILE']
        fname = values['FILE']
    else:
        fname = sys.argv[1]

    if not fname:
        exit()
    else:
        print(fname)
        path = f'{os.getcwd()}/target'
        shutil.copy(src=fname, dst=path)
        return str(fname)


get_file()