import PySimpleGUI as sg

def tema():
    sg.theme('darkblue')

class PrimeiraJanela:
    tema()
    layout1 = [
        [sg.Text('Usuário'), sg.Input(size=(41), key='usuario', focus=True)],
        [sg.Text('Senha'), sg.Input(size=(40), key='senha', password_char='*')],
        [sg.Button('Entrar'), sg.Button('Sair'), sg.Button('Se registre'), sg.Text(text_color='red', key='alerta')]
    ]

    #Criando a janela
    window = sg.Window('Sistema de Login', layout1, resizable=True)

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
                    [sg.Input(size=(40), key='user')],
                    [sg.Text('Senha')],
                    [sg.Input(size=(40), key='senha', password_char='*')],
                    [sg.Button('Salvar'), sg.Button('Sair'), sg.Text(text_color='red', key='alerta')]
                ]
            
                window = sg.Window('Registro', layout)

                while True:
                    event, values = window.read()

                    if event == sg.WINDOW_CLOSED or event == 'Sair':
                        break
                    
                    if values['user'] == '' or values['senha'] == '':
                        window['alerta'].update('Preencha todos os campos')

                    if event == 'Salvar':
                        with open ('cadastros.txt', 'a') as f:
                            f.write(values['user'] + '|' + values['senha'] + '\n')
                            window['alerta'].update('Usuário registrado com sucesso', text_color='green')

                window.close()

        if event == 'Entrar':         
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
                        window['alerta'].update('Usuário/Senha inválido!')   
                
            finally:
                f.close()

        if values['usuario'] == '' or values['senha'] == '':
            window['alerta'].update('Preencha todos os campos!')
    #Fechando a janela
    window.close()
