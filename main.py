import PySimpleGUI as sg

ASCII = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
SUPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïð "
DIGITS = "0123456789"
LCHARS = 'abcdefghijklmnopqrstuvwxyz'
UCHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LUCHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
COMMON_SYMBOLS = "!@#$%&+_-.?"
symbol_sets = ['Upper Lower Alphabet', 'Upper Lower Alphabet and Digits 0-9', 'Lower Alphabet digits 0-9', 'Upper Alphabet digits 0-9', 'All Ascii Characters']
digits_and_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
digits_and_lower = "0123456789abcdefghijklmnopqrstuvwxyz"
digits_upper_and_lower = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
base_character_set = {
    'ascii': ASCII, 
    'lower characters': LCHARS, 
    'upper characters':UCHARS, 
    'upper and lower alphabet':LUCHARS,
    'digits and upper':digits_and_upper,
    'digits and lower':digits_and_lower,
    'digits with upper and lower': digits_upper_and_lower,
    'custom': 'CUSTOM'}
character_set_names = list(base_character_set.keys())
character_sets = [list(base_character_set.values())]


def main():
    
    layout = [
        [
            sg.T("  Character Set  ", font='helvetica 20', text_color='light green',pad=(0,0), relief="raised")    
        ],
        [
            sg.HorizontalSeparator()
        ],
        [
            sg.T(
                "Base Character Set", 
                 font='ubuntu 10'),
            
            sg.Combo(
                character_set_names, 
                default_value=character_set_names[0], 
                enable_events=True, 
                key='SETNAME', 
                font='ubuntu 10'), 
            sg.StatusBar(
                ASCII,
                size=(90,1), 
                key='STATUSSET',
                font='ubuntu 10',
                background_color='black',
                text_color='green',
                justification='center')
        ],
        [
            sg.HorizontalSeparator()
        ],
        [
            sg.T("Remove the Following From base set:", font='ubuntu 10'), 
            sg.I("", key="REMOVECHARS")
        ],
        [
            sg.T("Outfile:",font='ubuntu 10'), 
            sg.FileBrowse(key='OUTFILE', font='ubuntu 10')
        ],
        ]
    window = sg.Window("Cracker", layout)
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Exit':
            window.close()
            break
        if event == 'SETNAME':
            key = values['SETNAME']
            myval = base_character_set[key]
            window['STATUSSET'].update(myval)
            window.refresh()
        
main()