from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pathlib
import time
import ctypes
from datetime import datetime

def Mbox(title, text, style):
        return ctypes.windll.user32.MessageBoxW(0, text, title, style)

def verifyHour():
    verificaHora()

def tryRegister():
    registrar()

def verificaHora():
    now = datetime.now()
    horaAtual = now.strftime("%H:%M")
    hora = []
    with open('horas.txt', 'r') as arch:
        for line in arch:
            hora.append(str(line))
        arch.close()
    for h in hora:
        if horaAtual == h:
            tryRegister()
            return 0
    for h in hora:
        if horaAtual < h:
            t2 = datetime.strptime(h, "%H:%M")
            break
    t1 = datetime.strptime(horaAtual, "%H:%M")
    tempoEspera = int((t2 - t1).total_seconds())
    time.sleep(tempoEspera)
    tryRegister()

def registrar():
    test = Mbox('Registro de ponto', 'Deseja registrar o ponto agora?', 3)
    if test == 2:
        print("Fechou")
        return -1
    else:
        if test == 6:
            caminho = pathlib.Path().absolute()
            data = []
            with open('senhas.txt', 'r') as arch:
                for line in arch:
                    data.append(str(line))
                arch.close()
            if len(data) == 2:
                caminho_driver = "" + str(caminho) + "\\chromedriver.exe"
                driver = webdriver.Chrome(executable_path=caminho_driver)
                driver.get("http://webponto.salux.com.br:90/pcponto/webponto/registro.asp")
                assert "WebPonto" in driver.title
                login = driver.find_element_by_name("txtCodigo")
                login.clear()
                login.send_keys(data[0])
                senha = driver.find_element_by_name("txtSenha")
                senha.clear()
                senha.send_keys(data[1])
                registrar = driver.find_element_by_name("cmdRegistrar")
                registrar.click()
                time.sleep(1)

                resp = driver.find_element_by_id("mensagem").text        

                driver.close()
                if resp == "Login ou senha incorretos!":
                    Mbox('Erro', 'Login ou senha incorretos! Verifique o arquivo de senhas e execute novamente o programa.', 0)
                    return -1

                if resp == "Código recém computado!":                    
                    Mbox('Erro', 'Código recém computado!', 0)
                    verifyHour()  

                if "Entrada" in resp or "Saída" in resp:        
                    Mbox('Sucesso', 'Registro concluido com sucesso!', 0)
                    verifyHour()  
                    
            else:                
                Mbox('Erro', 'Não foi localizado o arquivo de senhas! Verifique o arquivo de senhas e execute novamente o programa.', 0)
                return -1
            return 0
        else:
            time.sleep(300)
            return tryRegister()

if __name__ == "__main__":
    verificaHora()
