import requests
import urllib3
from datetime import datetime
import os
import sys
import time
from rich import print
from getpass import getpass
import base64

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

ano: datetime = datetime.now().year
mes: datetime = datetime.now().strftime("%m")
dia: datetime = datetime.now().strftime("%d")
momento: datetime = datetime.now().strftime("%H%M%S")

count: int = 0

def GeraLog(LogMensage: str) -> None:
    """
    Docstring for GeraLog
    
    :param LogMensage: Description
    :type LogMensage: str
    """
    LogPathNow: str = str(os.getcwd()) + "/logs/" + str(ano) + "/" + str(mes) + "/" + str(dia)
    if not os.path.exists(LogPathNow):
        os.makedirs(LogPathNow)
    with open (f"{LogPathNow}/pyHttpPing_{momento}.log","a",encoding='utf-8') as log:
        log.writelines(str(LogMensage) + '\n')
    print(LogMensage)

    #: Teste de comentário.

def GeraCsv(LogMensage: str) -> None:
    """
    Função para manipulação simples de dados que serão gravados em um arquivo de texto com extensão .csv

    :param LogMensage: str: 

    :return: None
    """
    LogPathNow: str = str(os.getcwd()) + "/data/" + str(ano) + "/" + str(mes) + "/" + str(dia)
    if not os.path.exists(LogPathNow):
        os.makedirs(LogPathNow)
    with open (f"{LogPathNow}/pyHttpPing_{momento}.csv","a",encoding='utf-8') as log:
        log.writelines(LogMensage + "\n")

def TestaUrl(url: str, pcred: str) -> None:
    """
    Função que recebe a URL e a credencial para a realização de teste.

    O teste de conectividade com a URL é realizada usando a lib requests, onde fazemos um simples GET na URL e verificamos os dados de retorno.
    
    :param url: str: 
    :param pcred: str: 

    :return: None

    """
    try:
        headers: dict[str,str] = {
        'Content-Type': 'application/json',
        'Authorization': f'Basic {pcred}'
        }
        GeraLog(f'{datetime.now()} - INFO - Realizando teste na url {url}')
        response = requests.get(url, headers=headers, verify=False, timeout=10)
        color: str = "green" if response.status_code == 200 else "red"
        GeraLog(f'{datetime.now()} - INFO - {url=}, [bold {color}]{response.status_code=}[/bold {color}]')
        GeraCsv(f'{datetime.now()};{url};{response.status_code}')
    except requests.ConnectionError:
        GeraLog(f'{datetime.now()} - ERROR - Falha de conexão com a {url=}')
        GeraCsv(f'{datetime.now()};{url};FALHA DE CONEXÃO')
    except requests.Timeout:
        GeraLog(f'{datetime.now()} - ERROR - Timeout na {url=}')
        GeraCsv(f'{datetime.now()};{url};TIMEOUT')
    except Exception as eError:
        #: Teste de comentário
        GeraLog(f"{datetime.now()} - ERROR - Um erro ocorreu com a requisição {url=}.")
        GeraLog(f'{datetime.now()} - ERROR - Exception on function: {TestaUrl.__name__}')
        GeraLog(f'{datetime.now()} - ERROR - Exception Message: {eError}')
        GeraLog(f'{datetime.now()} - ERROR - Exception Type: {type(eError)}')
        GeraLog(f'{datetime.now()} - ERROR - Exception Doc: {eError.__doc__}')
        GeraLog(f'{datetime.now()} - ERROR - sys.exc_info Details: {sys.exc_info}')

def main(urls: list[str], pcred: str) -> None:
    """
    Função main que cria um loop para ficar realizando o teste da url desejada.
    
    :param urls: list[str]: 
    :param pcred: str: 

    """
    global count
    # Teste de comentário 2
    try:
        while True:
            for url in urls:
                TestaUrl(str(url), pcred)
            count += 1
            time.sleep(10)
    except KeyboardInterrupt:
        GeraLog(f'{datetime.now()} - INFO - Saindo do teste.')

if __name__ == "__main__":
    InicioExecucao: datetime = datetime.now()
    GeraCsv('DATE;URL;STATUS_CODE')
    print('Por favor, insira seu usuário e senha do WebRIS Enterprise.')
    UserName: str = input('Usuário: ')
    Password: str = getpass('Senha: ')

    credentials: str = f'{UserName}:{Password}'
    fCredentials: str = base64.b64encode(credentials.encode()).decode()

    with open ("urls.dat","r") as unidades:
        UrlList: list[str]= unidades.read().splitlines()

    main(UrlList,fCredentials)
    TerminoExecucao: datetime = datetime.now()
    TempoExecucao: datetime = TerminoExecucao - InicioExecucao
    GeraLog(f'{datetime.now()} - INFO - O tempo de execução foi de {TempoExecucao} com um total de {count} iterações.')

    # TODO: Teste de todo para aparecer na documentação.