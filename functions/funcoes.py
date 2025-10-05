import pyautogui
import pygetwindow as gw
import time
import os
from alerts.alerta import meu_alert
from time import sleep
# Funções do WMS
# ---------------------------


IMAGEM_ALVO = os.path.join("image", "telainicial.PNG")


def executar_comando(codigo):
    nome_janela = "WMS Alcis -"
    janelas = [win for win in gw.getWindowsWithTitle(
        '') if nome_janela.lower() in win.title.lower()]
    if janelas:
        janela = janelas[0]
        if janela.isMinimized:
            janela.restore()
        time.sleep(0.5)
        janela.activate()
        time.sleep(1)
        pyautogui.typewrite(codigo)
        pyautogui.press('enter')
        print(
            f"✅ Janela '{janela.title}' foi trazida para frente e '{codigo}' foi enviado.")
    else:
        print("❌ Nenhuma janela encontrada com esse nome.")


def verificar_uz_faltando():
    procurar_e_clicar()
    executar_comando("LS123")


def verificar_empdoc():
    procurar_e_clicar()
    executar_comando("AK400")


def coletor():
    procurar_e_clicar()
    executar_comando("RF200")


def reconferir_uz():
    procurar_e_clicar()
    executar_comando("WE150")


def Desbloquear_UZ():
    procurar_e_clicar()
    executar_comando("QK100")


def etiqueta_uz():
    procurar_e_clicar()
    executar_comando("SF110")


def etiqueta_variadas():
    procurar_e_clicar()
    executar_comando("SD181")


def Associar():
    procurar_e_clicar()
    executar_comando("gt100")
    time.sleep(2)
    if not meu_alert('Clic "OK" para avançar!'):
        return
    time.sleep(0.3)
    executar_comando("AF200")


def reservar():
    procurar_e_clicar()
    executar_comando("SD280")
    time.sleep(2)
    if not meu_alert('Clic "OK" para avançar!'):
        return
    executar_comando("AK300")
    time.sleep(2)
    if not meu_alert('Clic "OK" para avançar!'):
        return
    pyautogui.click(707, 587)


def Cadastro_Motorista():
    procurar_e_clicar()
    executar_comando("gt800")


def Liberar_EMP():
    procurar_e_clicar()
    executar_comando("SD380")
    sleep(1)
    pyautogui.hotkey('f11')
    sleep(1)
    pyautogui.hotkey('ctrl', 'f11')


def Expedição():
    procurar_e_clicar()
    executar_comando("AF510")
    time.sleep(2)
    if not meu_alert('Clic "OK" para avançar!'):
        return
    time.sleep(0.3)
    executar_comando("AF540")
    time.sleep(2)
    if not meu_alert('Clic "OK" para avançar!'):
        return
    time.sleep(0.3)
    executar_comando("AK100")
    if not meu_alert('Clic "OK" para avançar!'):
        return
    os.system(r'""')
    sleep(0.3)
    pyautogui.click(533, 518)
    sleep(0.3)
    pyautogui.hotkey('ctrl', 't')
    sleep(0.3)
    pyautogui.typewrite(
        '')
    pyautogui.press('enter')


def recebimento():
    procurar_e_clicar()
    executar_comando("GT100")
    time.sleep(2)
    if not meu_alert('Clic "OK" para avançar!'):
        return
    time.sleep(0.3)
    executar_comando("WF100")
    time.sleep(2)
    if not meu_alert('Clic "OK" para avançar!'):
        return
    time.sleep(0.3)
    executar_comando("WF230")
    time.sleep(2)
    if not meu_alert('Clic "OK" para avançar!'):
        return
    executar_comando("WE100")
    sleep(2)
    if not meu_alert('Clic "OK" para avançar!'):
        return
    os.system(r'"')
    sleep(0.3)
    pyautogui.click(533, 518)
    sleep(0.3)
    pyautogui.hotkey('ctrl', 't')
    sleep(0.3)
    pyautogui.typewrite(
        '')
    pyautogui.press('enter')


def finalizar_recebimento():
    procurar_e_clicar()
    executar_comando("WE150")
    time.sleep(2)
    if not meu_alert('Clic "OK" para avançar!'):
        return
    time.sleep(0.3)
    executar_comando("WF200")
    time.sleep(2)
    if not meu_alert('Clic "OK" para avançar!'):
        return
    executar_comando("GT100")


def finalizar_expedicao():
    procurar_e_clicar()
    executar_comando("LS123")
    time.sleep(2)
    if not meu_alert('Clic "OK" para avançar!'):
        return
    time.sleep(0.3)
    executar_comando("GT100")
    time.sleep(2)
    if not meu_alert('Clic "OK" para avançar!'):
        return
    executar_comando("AK100")


def finalizar_faturamento():
    procurar_e_clicar()
    executar_comando("AF570")


def Cancelamento_Pedido():
    procurar_e_clicar()
    executar_comando("AK100")
    time.sleep(2)
    if not meu_alert('Clic "OK" para avançar!'):
        return
    executar_comando("AF550")
    time.sleep(2)


def verificar_BLOK_AVA():
    procurar_e_clicar()
    executar_comando("QK100")


def Erro_Motorista():
    procurar_e_clicar()
    executar_comando("gt600")


def faturar_stine():
    executar_comando("AF100")
    sleep(1)
    if not meu_alert('Clic "OK" para avançar!'):
        return
    executar_comando("AF560")
    sleep(1)


def login_porta_admim():
    # portaria
    os.system(r'""')
    sleep(3)
    pyautogui.typewrite(')
    sleep(1)
    pyautogui.press('enter')
    sleep(3)
    pyautogui.hotkey('tab')
    sleep(0.3)
    pyautogui.hotkey('tab')
    sleep(0.3)
    pyautogui.typewrite('')
    sleep(0.3)
    pyautogui.hotkey('tab')
    sleep(0.3)
    pyautogui.typewrite('')
    sleep(1)
    if not meu_alert('Resolva o Calculo e Clic "OK"'):
        return
    pyautogui.press('enter')
    sleep(1)
    # ADM
    pyautogui.hotkey('ctrl', 'shift', 'n')
    sleep(1)
    pyautogui.typewrite('')
    pyautogui.press('enter')
    sleep(3)
    pyautogui.hotkey('tab')
    sleep(0.3)
    pyautogui.hotkey('tab')
    sleep(0.3)
    pyautogui.typewrite('')
    sleep(0.3)
    pyautogui.hotkey('tab')
    sleep(0.3)
    pyautogui.typewrite('')
    if not meu_alert('Resolva o Calculo e Clic "OK"'):
        return
    pyautogui.press('enter')
    sleep(1)


def procurar_e_clicar(IMAGEM_ALVO=IMAGEM_ALVO, max_tentativas=5):
    """
    Procura uma imagem na tela e clica nela.
    - IMAGEM_ALVO: caminho da imagem
    - max_tentativas: número de vezes que vai tentar
    """
    tentativas = 0

    while tentativas < max_tentativas:
        print("🔎 Procurando imagem...")

        try:
            pos = pyautogui.locateCenterOnScreen(IMAGEM_ALVO, confidence=0.8)
        except Exception as e:
            print(f"⚠️ Erro ao procurar imagem: {e}")
            pos = None

        if pos:
            print("✅ Imagem encontrada!")
            return True
        else:
            meu_alert("Feche as abas abertas. Volte a tela principal.")
            tentativas += 1

    print("🚫 Imagem não localizada após várias tentativas.")
    return False
