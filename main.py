from tracemalloc import stop
import PySimpleGUI as sg
import os

def tema():
    sg.theme('darkamber')

class PrimeiraJanela:
    tema()
    layout1 = [
        [sg.Text('Usuário'), sg.Input(size=(41), key='usuario', focus=True)],
        [sg.Text('Senha'), sg.Input(size=(40), key='senha', password_char='*')],
        [sg.Button('Entrar'), sg.Button('Sair'), sg.Button('Se registre'), sg.Text(text_color='red', key='alerta')]
    ]

    #Criando a janela
    window = sg.Window('Sistema de Login', layout1)

    #mostrando e interagindo com a janela
    while True:      
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Sair':
            break
        
        #Criando um novo usuário e registrando no cadastros.txt
        if event == 'Se registre':           
            class registro:
                tema()
                layout = [
                    [sg.Text('Cadastro', size=(40), justification='c')],
                    [sg.Text('Usuário')],
                    [sg.Input(size=(50), key='user')],
                    [sg.Text('Senha')],
                    [sg.Input(size=(50), key='senha', password_char='*')],
                    [sg.Button('Salvar'), sg.Button('Sair'), sg.Text(text_color='red', key='alerta')]
                ]
            
                window = sg.Window('Registro', layout)

                while True:
                    event, values = window.read()

                    if event == sg.WINDOW_CLOSED or event == 'Sair':
                        break

                    if event == 'Salvar':
                        doc = open('cadastros.txt')
                        filesize = os.path.getsize('cadastros.txt')
                        if filesize == 0:
                            if values['user'] == '' or values['senha'] == '':
                                window['alerta'].update('Preencha todos os campos!')
                            
                            else:
                                with open ('cadastros.txt', 'a') as f:
                                    f.write(values['user'] + '|' + values['senha'] + '\n')
                                    window['alerta'].update('Usuário registrado com sucesso', text_color='green')

                        else:
                            if values['user'] == '' or values['senha'] == '':
                                window['alerta'].update('Preencha todos os campos!')
                            
                            else:
                                for linha in doc:
                                    dados = linha.split('|')
                                    dados[1] = dados[1].replace('\n', '')

                                if values['user'] == dados[0] and values['senha'] == dados[1]:
                                    window['alerta'].update('Este login já existe, volte e entre.')
                
                                else:
                                    if values['user'] == dados[0] and values['senha'] != dados[1]:
                                        window['alerta'].update('Este usuário já existe.')

                                    else:
                                        with open ('cadastros.txt', 'a') as f:
                                            f.write(values['user'] + '|' + values['senha'] + '\n')
                                            window['alerta'].update('Usuário registrado com sucesso', text_color='green')

                            
                window.close()

        if event == 'Entrar':         
            filesize = os.path.getsize('cadastros.txt')

            if filesize == 0:
                window['alerta'].update('Usuário não cadastrado')

            else:
                try:
                    f = open('cadastros.txt', 'rt')

                except:
                    window['alerta'].update('Erro no armazenamento!')

                else:
                    #Verificando se o user e a senha já estão cadastrados
                    for linha in f:
                        dados = linha.split('|')
                        dados[1] = dados[1].replace('\n', '')
                        
                        if dados[0] == values['usuario'] and values['senha'] == dados[1]:
                                window.close()
                                class dentroDoSistema:
                                    tema()
                                    layout = [
                                        [sg.Text('Bem vindo!')],
                                        [sg.Button('Sair')]
                                    ]

                                    window = sg.Window('Sistema', layout)

                                    while True:
                                        event, values = window.read()

                                        if event == sg.WINDOW_CLOSED or event == 'Sair':
                                            break
                                    
                                    window.close()    

                        else:
                            if dados[0] == values['usuario'] and values ['senha'] != dados[1]:
                                window['alerta'].update('Senha incorreta')

                            elif dados[1] != values['usuario'] and values['senha'] == dados[1]:
                                window['alerta'].update('Usuário incorreto')

                            else:
                                window['alerta'].update('Este login não existe.')
                finally:
                    f.close()

        if values['usuario'] == '' or values['senha'] == '':
            window['alerta'].update('Preencha todos os campos!')

    #Fechando a janela
    window.close()
