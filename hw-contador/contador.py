import PySimpleGUI as sg
import keyboard as kb

# Version 1.0

sg.theme('Black')
click=0
money=0.0

cm=sg.popup_get_text('Qual o preço por mil tarefas? (Caso seja centavos, utilize o .)', 'Escolha', no_titlebar = True)
if (cm == None) or (cm == ''):
    quit()
applayout = [
    [sg.Text(click,size=(5),font=('minecraft 50'), justification=('right'),key='click')],
    [sg.Text('$'+str(money),size=(12),font=('minecraft 20'), justification=('right'),key='money')]
]


window = sg.Window('Contador', layout = applayout, no_titlebar = True, keep_on_top = True, grab_anywhere= True, margins=(0,0))

while True:
    event, values = window.read(timeout=1)
    
    if event == sg.WINDOW_CLOSED:
        break
    
    if kb.is_pressed('/') == True:
        click += 1
        money += (float(cm) / 1000)
        window['money'].update(value='$'+str(round(money, 2)))
        window['click'].update(value=click)
        kb.wait('/',suppress = True, trigger_on_release = True)

    if kb.is_pressed('esc') == True:
        exit()
        
window.close()