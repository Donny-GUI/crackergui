import PySimpleGUI as sg
import os

from attributes import (
    TITLE_PADX,
    TITLE_PADY,
    TITLE_FONT,

    FRAME1_PADX,
    FRAME1_PADY,
    FRAME1_FONT,
    FRAME1_LABEL_TOOLTIP,
    FRAME1_COMBO_BOX_KEY,
    FRAME1_COMBO_BOX_EXPAND_Y,
    FRAME1_HIDDEN_ENTRY_BOX_KEY,
    FRAME1_CHARACTERSET_STATUS_BAR_SIZE_X,
    FRAME1_CHARACTERSET_STATUS_BAR_SIZE_Y,
    FRAME1_CHARACTERSET_STATUS_BAR_KEY,
    FRAME1_CHARACTERSET_STATUS_BAR_FONT,
    FRAME1_CHARACTERSET_STATUS_BAR_JUSTIFICATION,
    FRAME2_EXCEPTIONS_ENTRY_BOX_KEY,
    FRAME2_EXCEPTIONS_STATUS_BAR_SIZE_X,
    FRAME2_EXCEPTIONS_STATUS_BAR_SIZE_Y,
    FRAME2_EXCEPTIONS_STATUS_BAR_KEY,
    FRAME2_EXCEPTIONS_STATUS_BAR_FONT,
    FRAME1_LABEL_TEXT,
    FRAME2_FONT,
    FRAME3_OUTFILE_LABEL_TEXT,
    FRAME3_OUTFILE_ENTRY_BOX_KEY,
    FRAME3_FILEBROWSE_KEY,
    FRAME3_FILEBROWSE_FONT,
    FRAME3_ELEMENT_JUSTIFICATION,
    FRAME3_FONT,

)
from lib import (
    ASCII, 
    base_character_set,
    character_set_names
    )


def main():
    sg.theme('dark amber')
    #|######################################|#
    #|          ALL GUI ELEMENTS            |#
    #|                                      |# 
    #| Individual items from the top to the |# 
    #|  bottom, left to right for each line |# 
    #|  of the gui, as they appear.         |#
    #|######################################|#
    
    top_label_password_list_maker = sg.T(
        " \n\tPassword List Maker\t\n ", 
        font                =   TITLE_FONT, 
        #text_color          =   TITLE_TEXT_COLOR,
        #background_color    =   TITLE_BACKGROUND_COLOR, 
        pad                 =   (TITLE_PADX, TITLE_PADY), 
        relief              =   "ridge",
        expand_y            =   True,
        justification       =   'Center'
        )
    
    frame1_characters_label = sg.T(
        FRAME1_LABEL_TEXT,
        #text_color       =   FRAME1_CHARACTERSET_STATUS_BAR_FG_COLOR,
        #background_color =   FRAME1_BG_COLOR, 
        font             =   FRAME1_FONT, 
        tooltip          =   FRAME1_LABEL_TOOLTIP
        )
    
    frame1_characterset_combo_box = sg.Combo( 
        character_set_names, 
        expand_y        = FRAME1_COMBO_BOX_EXPAND_Y, 
        default_value   = character_set_names[0], 
        enable_events   = True, 
        key             = FRAME1_COMBO_BOX_KEY, 
        font            = FRAME1_CHARACTERSET_STATUS_BAR_FONT, 
        pad             = (FRAME1_PADX,FRAME1_PADY),
        text_color      = 'cyan',
        button_arrow_color= 'yellow',
        button_background_color='blue',
        #background_color= FRAME1_BG_COLOR
        )
    
    frame1_hidden_entry_box = sg.I( 
        "", 
        key             = FRAME1_HIDDEN_ENTRY_BOX_KEY,
        #text_color      = 'cyan',
        #background_color= FRAME1_CHARACTERSET_STATUS_BAR_BG_COLOR,
        enable_events   = True, 
        visible         = False,
        font            = 'ubuntu 10',
        pad             = (10, 5),
        tooltip         = 'Enter a custom set of letters, numbers, symbols here')
    
    frame1_characterset_status_bar = sg.StatusBar(
        ASCII,
        size            =(FRAME1_CHARACTERSET_STATUS_BAR_SIZE_X,FRAME1_CHARACTERSET_STATUS_BAR_SIZE_Y), 
        key             = FRAME1_CHARACTERSET_STATUS_BAR_KEY,
        font            = 'ubuntu 10',
        background_color= 'black',
        #text_color      = FRAME1_CHARACTERSET_STATUS_BAR_FG_COLOR,
        justification   = FRAME1_CHARACTERSET_STATUS_BAR_JUSTIFICATION,
        enable_events   =True, 
        pad             = (20,5),
        )
    
    frame2_exceptions_label = sg.T(
        "Exceptions",
        font                = 'ubuntu 12',
        pad                 = (10, 20),
        #background_color    = FRAME2_EXCEPTIONS_STATUS_BAR_BG_COLOR,
        #text_color          = FRAME2_EXCEPTIONS_STATUS_BAR_FG_COLOR
        )
    
    frame2_exceptions_hidden_message = sg.T(
        "Do not include  delimiters in your string, just the characters to exclude",
        enable_events=True,
        key="HIDDENEXCEPTIONSWARNING",
        font='ubuntu 12',
        text_color='red',
        visible=False,
        background_color='black')
    
    hidden_switch = sg.Radio(
        group_id="RadioButtons",
        text="Exclude Spaces",
        visible=False,
        key="EXCLUDESPACES"
        )
        
    
    frame2_exceptions_entry_box = sg.I(
        "click to add character exceptions", 
        expand_y        =   True,  
        enable_events   =   True,
        key             =   FRAME2_EXCEPTIONS_ENTRY_BOX_KEY, 
        font            =   FRAME2_FONT,
        pad             =   (20, 20),   
        )
    
    frame2_exceptions_status_bar = sg.StatusBar(
        "",
        size                =   (FRAME2_EXCEPTIONS_STATUS_BAR_SIZE_X,FRAME2_EXCEPTIONS_STATUS_BAR_SIZE_Y), 
        key                 =   FRAME2_EXCEPTIONS_STATUS_BAR_KEY,
        font                =   FRAME2_EXCEPTIONS_STATUS_BAR_FONT,
        pad                 =   (20, 20),
        justification       =   'center',
        #background_color    =   FRAME2_EXCEPTIONS_STATUS_BAR_BG_COLOR,
        #text_color          =   FRAME2_EXCEPTIONS_STATUS_BAR_FG_COLOR
        )
    frame3_outfile_label = sg.T(
        FRAME3_OUTFILE_LABEL_TEXT,
        font                =   FRAME3_FONT,
        pad                 =   (20, 20),)
    frame3_outfile_entry_box = sg.I(
        f"{os.getcwd()}/outfile.txt", 
        enable_events       =   True, 
        key                 =   FRAME3_OUTFILE_ENTRY_BOX_KEY,
        pad                 =   (20, 20),
        )
    frame3_file_browse_button = sg.FileBrowse(
        key                 =   FRAME3_FILEBROWSE_KEY,
        font                =   FRAME3_FILEBROWSE_FONT,
        pad                 =   (20, 20),
    )
    first_frame = sg.Frame(
        ' Base Character Set ', 
        [
            [frame1_characterset_combo_box, frame1_hidden_entry_box],
            [frame1_characterset_status_bar]
        ],
        relief              =   'sunken',
        #background_color    =   FRAME1_BG_COLOR,
        title_color         =   'gray',
        font                =   "ubuntu 16",
        expand_x            =   True,         
        pad                 =   (20, 20)
        )
    second_frame = sg.Frame(
        " Exceptions ", 
        [
            [frame2_exceptions_entry_box, hidden_switch],
            [frame2_exceptions_hidden_message],
            [frame2_exceptions_status_bar]
        ],
        relief          =   'sunken',
        font            =   'ubuntu 16',
        pad             =   (20, 20),
        title_color     =   'gray',
        )
    
    third_frame = sg.Frame(
        "Outfile",
        [
            [frame3_outfile_entry_box, frame3_file_browse_button]
        ],
        title_color             =   'gray',
        relief                  =   'sunken',
        font                    =   'ubuntu 16',
        pad                     =   (20, 20),
        expand_y                =   True,
        element_justification   =   FRAME3_ELEMENT_JUSTIFICATION
        )
    mincombo = [1,2,3]
    pdf_combo = [1.4,1.5,1.6,1.7]
    fourth_frame_row_1 = [
        [
            sg.Radio(group_id="EXCLUDESPACES", text ="Exclude Spaces\t\t", key="ESPACES",font='ubuntu 10'), sg.Push(),
            sg.T("\t  Minimum Repeats", font='ubuntu 10'),sg.Push(),sg.Combo(mincombo, key="MINIMUMREPEATS")
        ]
    ]
    maxcombo = [2,3,4,5]
    
    fourth_frame_row_2 = [
        [
            sg.Radio(group_id="TRYHARD",font='ubuntu 10', text ="TryHard Substitution", key='THARD'),sg.Push(),
            sg.T("\tMaximum Character Repeats",font='ubuntu 10'),sg.Push(),sg.Combo(maxcombo, key='MAXIMUMREPEATS',font='ubuntu 10'),
        ]
    ]
    fourth_frame_row_3 = [
        [
            sg.Radio(group_id="RANDOMORDER", text ="Randomize Order\t", key='RORDER'),sg.Push(),

            sg.T("\t\tMaximize for pdf version"),sg.Push(),

            sg.Combo(pdf_combo, key="PDFVERSION"),
        ],
    ]
    fourthframe_layout = [fourth_frame_row_1, fourth_frame_row_2, fourth_frame_row_3]
    
    layout = [
        [top_label_password_list_maker],
        [first_frame],
        [second_frame],
        [third_frame],
        [sg.Frame("Special Rules",[
        [sg.Frame("", fourth_frame_row_1, relief='flat')],
        [sg.Frame("", fourth_frame_row_2, relief='flat')], 
        [sg.Frame("", fourth_frame_row_3, relief='flat')]],
        element_justification='left')]
    ]
    window = sg.Window(
        "Cracker", 
        layout, 
        #background_color    =   WINDOW_BG_COLOR, 
        #sbar_frame_color    =   'green',
        finalize=True
        )
    is_clicked = False
    was_seen = False
    has_spaces = False
    while True:
        event, values = window.read()
        print(event)
        print(values)
        ##  ON CLOSE OR EXIT
        if event == sg.WINDOW_CLOSED or event =='Exit':
            window.close()
            break
        ## ON COMBO CHOSEN CHARACTERSET
        if event == "SETNAME":
            key = values['SETNAME']
            myval = base_character_set[key]
            window['STATUSSET'].update(myval)
            window.refresh()
            is_custom = values['SETNAME']
            #  UPDATE IF CUSTOM IS SET
            if is_custom == "custom":
                window['HIDDENCHARSET'].update(visible = True)
                window.refresh()
            else:
                ##  RETURN TO INVISIBLE WHEN CUSTOM IS NOT
                window['HIDDENCHARSET'].update(visible=False)
                window.refresh()
        
        ## HIDDEN CUSTOM CHARACTERS
        
        if event == "HIDDENCHARSET":
            window['STATUSSET'].update(values['HIDDENCHARSET'])
        
        ## FILE BROWSE AND ENTRY BOX
        
        if event == 'Browse':
            event, values = window.read()
            window.refresh()
            window['OUTFILEENTRY'].update(values['Browse'])
            len(values['OUTFILEENTRY'])
        
        ## EXCEPTIONS STATUS BAR AND ENTRY BOX
        
        if event == 'EXCEPTIONS':
            if not is_clicked:
                ## IF THE BOX HASNT BEEN CLICKED YET
                window["EXCEPTIONS"].update("")
                window['STATUSEXCEPTIONS'].update('')
                is_clicked = True
                window.refresh()
            else:
                ## REMOVE THE DUPLICATE CHARACTERS
                window['STATUSEXCEPTIONS'].update(values['EXCEPTIONS'])
                window.refresh()
                chars = ""
                for char in values['EXCEPTIONS']:
                    if char not in chars:
                        chars+=char
                    ## SHOW WARNING
                    else:window['HIDDENEXCEPTIONSWARNING'].update(visible=True)
                ## UPDATE JOINED SET AS CHARS        
                window['EXCEPTIONS'].update(chars)
                window['STATUSEXCEPTIONS'].update(chars)
                window.refresh()
main()