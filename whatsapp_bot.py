import pywhatkit
from datetime import datetime
import PySimpleGUI as sg

def aviso():
    tema = sg.theme('Reddit')
    layout = [
        [sg.Text('Para o programa funcionar corretamente pareie o whatsapp')],[sg.Text('com o seu celular e abra o web whatsapp em uma aba no')],[sg.Text('seu navegador padrão')],
        [sg.Image(filename='emoji1.png')]

    ]
    janela = sg.Window('Aviso',layout,size=(400,200))
    while True:
        e,v = janela.Read()
        if e == sg.WIN_CLOSED or e == 'Cancel':
            break
    janela.Close()


tema = sg.theme('Reddit')
layout = [
    [sg.Text('Número',font='Roboto')],[sg.Input(key='int',font='Roboto')],[sg.Text('Mensagem',font='Roboto')],[sg.Input(key='intt',font='Roboto')],[sg.Button('Confirmar',key='btn',font='Roboto')],[sg.Image(filename='emoji2.png')]
]
janela = sg.Window('bot',layout,size=(250,250))
while True:
    aviso()
    e,v = janela.Read()
    if e == sg.WIN_CLOSED or e == 'Cancel':
        break
    if e == 'btn':
        ina = v['int']
        ino = v['intt']
        print(f'o número do contato é:{ina} e a mensagem:{ino}')
        pywhatkit.sendwhatmsg(ina,ino,datetime.now().hour,datetime.now().minute+1)
   

