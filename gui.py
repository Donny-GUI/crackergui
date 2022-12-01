import PySimpleGUI as sg
import os

#############################################
######[]    CHARACTERSET DECLARE    []#######
#############################################
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
character_sets = list(base_character_set.values())


def main():
    
    #|######################################|#
    #|          ALL GUI ELEMENTS            |#
    #|                                      |# 
    #| Individual items from the top to the |# 
    #|  bottom, left to right for each line |# 
    #|  of the gui, as they appear.         |#
    #|######################################|#
    
    top_label_password_list_maker = sg.T(
        " \n\tPassword List Maker\t\n ", 
        font='ubuntu 20', 
        text_color='green',
        background_color='black', 
        pad=(20,20), 
        relief='raised'
    )
    frame1_characters_label = sg.T(
        "Characters", 
        font='ubuntu 10', 
        tooltip='The set of letters symbols and numbers\n to start out with when creating a\n password list'
    )
    frame1_characterset_combo_box = sg.Combo( 
        character_set_names, 
        expand_y=True, 
        default_value=character_set_names[0], 
        enable_events=True, 
        key='SETNAME', 
        font='ubuntu 10', 
        pad=(10,10)
    )
    frame1_hidden_entry_box = sg.I( 
        "", 
        key="HIDDENCHARSET", 
        enable_events=True, 
        visible=False, 
        pad=(10,10),
        tooltip='Enter a custom set of letters, numbers, symbols here'
    )
    frame1_characterset_status_bar = sg.StatusBar(
        ASCII,size=(90,1), 
        key='STATUSSET',
        font='ubuntu 10',
        background_color='black',
        text_color='green',
        justification='center',
        enable_events=True, pad=(10,10)
    )
    
    frame2_exceptions_label = sg.T(
        "Exceptions", 
        font='ubuntu 10'
    ),
    
    frame2_exceptions_entry_box = sg.I(
        "", 
        expand_y=True,  
        enable_events=True, 
        key='EXCEPTIONS', 
        font='ubuntu 10'
    )
    
    frame2_exceptions_status_bar = sg.StatusBar(
        "",
        size=(90,1), 
        key='STATUSEXCEPTIONS',
        font='ubuntu 10',
        background_color='black',
        text_color='green'
    )
    frame3_outfile_label = sg.T(
        "Outfile:",
        font='ubuntu 10'
    ), 
    frame3_outfile_entry_box = sg.I(
        f"{os.getcwd()}/outfile.txt", 
        enable_events=True, 
        key="OUTFILEENTRY"
    ),
    frame3_file_browse_button = sg.FileBrowse(
        key='OUTFILE', 
        font='ubuntu 10'
    )
    ########################################
    ######[     FRAME 1 LAYOUT      ]#######
    ########################################
    first_frame = sg.Frame(
        'Base Character Set', 
        [
            [
                frame1_characters_label, frame1_characterset_combo_box, frame1_hidden_entry_box
            ],
            [ 
                frame1_characterset_status_bar
            ]
        ],
        relief='sunken', pad=(20,20)
    )
    #######################################
    ######[]   FRAME 2 LAYOUT      []######
    #######################################
    second_frame = sg.Frame(
        'Character Exceptions', 
        [
            [
                frame2_exceptions_label, 
                frame2_exceptions_entry_box
            ],
            [
                frame2_exceptions_status_bar
            ]
        ]
    )
    ##################################|
    ######[]   MAIN LAYOUT    []######|
    ##################################|
    layout = [
        [
            top_label_password_list_maker
        ],
        [
            first_frame
        ],
        [
            sg.HorizontalSeparator()
        ],
        [
            second_frame
        ],
        [
            frame3_outfile_label, frame3_outfile_entry_box, frame3_file_browse_button
        ],
    ]
        
    #######################################|
    ######[] MAIN WINDOW SETTINGS []#######|
    #######################################|
    
    window = sg.Window("Cracker", layout, finalize=True)
    
    while True:
        event, values = window.read()
        event = str(event)
        
        ###############################
        #####[]    EVENTS      []######
        ###############################
        
        ##  ON CLOSE OR EXIT
        
        if event.startswith(str(sg.WINDOW_CLOSED)) or event.startswith(str('Exit')):
            window.close()
            break
        
        ## ON COMBO CHOSEN CHARACTERSET
        
        if event.startswith("SETNAME") == True:
            key = values['SETNAME']
            myval = base_character_set[key]
            window['STATUSSET'].update(myval)
            window.refresh()
            is_custom = values['SETNAME']
            
            ##  UPDATE IF CUSTOM IS SET
            if is_custom == "custom":
                window['HIDDENCHARSET'].update(visible = True)
                window.refresh()
            else:
                ##  RETURN TO INVISIBLE WHEN CUSTOM IS NOT
                window['HIDDENCHARSET'].update(visible=False)
                window.refresh()
        
        ## HIDDEN CUSTOM CHARACTERS
        
        if event.startswith("HIDDENCHARSET"):
            window['STATUSSET'].update(values['HIDDENCHARSET'])
        
        ## FILE BROWSE AND ENTRY BOX
        
        if event == 'Browse':
            event, values = window.read()
            window.refresh()
            window['OUTFILEENTRY'].update(values['Browse'])
            len(values['OUTFILEENTRY'])
        
        ## EXCEPTIONS STATUS BAR AND ENTRY BOX
        
        if event == 'EXCEPTIONS':
            currently_typed = values['EXCEPTIONS']
            window['STATUSEXCEPTIONS'].update(currently_typed)
            window.refresh()
        
        
        
main()