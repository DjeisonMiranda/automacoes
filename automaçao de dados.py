import pyautogui
import time
#pyautogui.click -> clicar em alguma coisa
#pyautogui.press -> apertar 1 tecla
#pyautogui.write -> escrever um texto 
#pyautogui.hotkey -> para apertar uma combinaçao de teclas ex:(ctrl + c) >> pyautogui.hotkey('ctrl', 'c')
#pyautogui.PAUSE = VALOR EM SEGUNDOS QUE VAI PAUSAR 

#passo 1: entra no sistema da empresa - https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbGpuc3RtSnZjYlliYVZoN3ZNWklhS1o3c1M5UXxBQ3Jtc0tsT01nc3pXOEdpdFg4OGptOVZiZ0pMeHhMWWpwWExsSWtpZjE4VUxlbWZGa18zVThFdHFXY3dOU05nRjNzU243aVkxLU9ESm1hZFZUckFSZFVmeWZXcV9hWDZoMFNPdHZtekNpRU5QbW9kZExVSWkxaw&q=https%3A%2F%2Fdlp.hashtagtreinamentos.com%2Fpython%2Fintensivao%2Flogin&v=RqTDtsITYSM
# passo 2: fazer login
# passo 3: importar a base de dados
# passo 4: cadastrar um produto
# passo 5: repetir para todos os produtos

pyautogui.PAUSE = 0.5
 #passo 1: entra no sistema da empresa
    #abrir o chrome
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
    #digitar o site 
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
     # passo 2: fazer login 
time.sleep(3)
pyautogui.click(x=885, y=367)
pyautogui.write('djeisonmiranda38@gmail.com')
pyautogui.press('enter')
time.sleep(1)
pyautogui.press('tab')
pyautogui.write('1234')
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(3)

    # passo 3: importar a base de dados
import pandas

tabela = pandas.read_csv('produtos.csv')

    # passo 4: cadastrar um produtos
for linha in tabela.index:

    codigo = tabela.loc[linha, 'codigo']
    marca = tabela.loc[linha, 'marca']
    tipo = tabela.loc[linha, 'tipo']
    categoria = str(tabela.loc[linha, 'categoria'])
    preco_unitario = str(tabela.loc[linha, 'preco_unitario'])
    custo = str(tabela.loc[linha, 'custo'])
    obs = str(tabela.loc[linha, 'obs'])

    pyautogui.press('tab')
    pyautogui.write(codigo)
    pyautogui.press('tab')
    pyautogui.write(marca)
    pyautogui.press('tab')
    pyautogui.write(tipo)
    pyautogui.press('tab')
    pyautogui.write(categoria)
    pyautogui.press('tab')
    pyautogui.write(preco_unitario)
    pyautogui.press('tab')
    pyautogui.write(custo)
    pyautogui.press('tab')
    if obs != 'nan':
        pyautogui.write(obs)
    pyautogui.press('tab')
    pyautogui.press('enter')

    pyautogui.scroll(10000)#pode ser usado .press('home') para voltar ao inicio da pagina.
