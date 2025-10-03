import tkinter as tk
from tkinter import ttk
import threading
import pygetwindow as gw
import time
import pyautogui
import os
from time import sleep

# ---------------------------
# Função de alerta personalizada
# ---------------------------

# Caminho da imagem que você quer procurar
IMAGEM_ALVO = "telainicial.PNG"


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
            print("❌ Imagem não encontrada. Atualizando página...")
            pyautogui.press("f5")
            time.sleep(13)  # espera a página recarregar
            tentativas += 1

    print("🚫 Imagem não localizada após várias tentativas.")
    return False

def meu_alert(msg, titulo="Alerta", botao="OK"):
    """
    Mostra um alerta modal com botão OK.
    Retorna True se clicou OK, False se clicou X.
    """
    resposta = {"ok": False}

    def on_ok():
        resposta["ok"] = True
        win.destroy()

    def on_close():
        resposta["ok"] = False
        win.destroy()

    root = tk.Tk()
    root.withdraw()  # esconde janela principal
    win = tk.Toplevel(root)
    win.title(titulo)
    win.geometry("300x120")
    win.resizable(False, False)
    win.grab_set()  # bloqueia interação com outras janelas
    win.protocol("WM_DELETE_WINDOW", on_close)

    tk.Label(win, text=msg, padx=10, pady=10).pack()
    tk.Button(win, text=botao, width=10, command=on_ok).pack(pady=10)

    root.wait_window(win)  # espera apenas essa janela fechar
    root.destroy()
    return resposta["ok"]

# ---------------------------
# Funções do WMS
# ---------------------------


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
    executar_comando("LS123")


def verificar_empdoc():
    executar_comando("AK400")


def coletor():
    executar_comando("RF200")


def reconferir_uz():
    executar_comando("WE150")


def etiqueta_uz():
    executar_comando("SF110")


def etiqueta_variadas():
    executar_comando("SD181")


def Associar():
    executar_comando("gt100")
    time.sleep(2)
    if not meu_alert('Clic "OK" para avançar!'):
        return
    time.sleep(0.3)
    executar_comando("AF200")


def reservar():
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
    executar_comando("gt800")


def Liberar_EMP():
    executar_comando("SD380")
    sleep(1)
    pyautogui.hotkey('f11')
    sleep(1)
    pyautogui.hotkey('ctrl', 'f11')


def Expedição():
    executar_comando("AF510")
    time.sleep(2)
    if not meu_alert('Clic "OK" para avançar!'):
        return
    executar_comando("AF540")
    time.sleep(2)
    if not meu_alert('Clic "OK" para avançar!'):
        return
    executar_comando("AK100")
    if not meu_alert('Clic "OK" para avançar!'):
        return
    os.system(r'"C:\Program Files\Google\Chrome\Application\chrome.exe"')
    sleep(0.3)
    pyautogui.click(533, 518)
    sleep(0.3)
    pyautogui.hotkey('ctrl', 't')
    sleep(0.3)
    pyautogui.typewrite(
        'https://pwa.alcis.com.br/INTERLOG/conteudo/principal.aspx')
    pyautogui.press('enter')


def recebimento():
    executar_comando("GT100")
    time.sleep(2)
    if not meu_alert('Clic "OK" para avançar!'):
        return
    executar_comando("WF100")
    time.sleep(2)
    if not meu_alert('Clic "OK" para avançar!'):
        return
    executar_comando("WF230")
    if not meu_alert('Clic "OK" para avançar!'):
        return
    executar_comando("WE100")
    sleep(2)
    if not meu_alert('Clic "OK" para avançar!'):
        return
    os.system(r'"C:\Program Files\Google\Chrome\Application\chrome.exe"')
    sleep(0.3)
    pyautogui.click(533, 518)
    sleep(0.3)
    pyautogui.hotkey('ctrl', 't')
    sleep(0.3)
    pyautogui.typewrite(
        'https://pwa.alcis.com.br/INTERLOG/conteudo/principal.aspx')
    pyautogui.press('enter')


def finalizar_recebimento():
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


def Cancelamento_Pedido():
    executar_comando("AK100")
    time.sleep(2)
    if not meu_alert('Clic "OK" para avançar!'):
        return
    executar_comando("AF550")
    time.sleep(2)


def verificar_BLOK_AVA():
    executar_comando("LS200")


# ---------------------------
# Interface Tkinter com Paginação
# ---------------------------


def criar_interface():
    root = tk.Tk()
    root.title("Automação WMS")
    root.geometry("400x650")

    # Frame principal para paginação
    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=True)

    # Dicionário de funções (agora dividido em páginas)
    paginas_funcoes = [
        # Página 1
        {
            "Verificar EMPDOC ❔": verificar_empdoc,
            "Verificar UZ Faltando ❔": verificar_uz_faltando,
            "Associar 📈": Associar,
            "Cadastro Motorista 🚚": Cadastro_Motorista,
            "Reservar 📦": reservar,
            "Coletor 📟": coletor,
            "Reconferir UZ ↪️": reconferir_uz,
            "Etiqueta UZ 🏷️": etiqueta_uz,
            "Etiqueta Variadas 🏷️": etiqueta_variadas,
            "Liberar EMP ✅": Liberar_EMP,
            "Expedição ⭐": Expedição,
            "recebimento ⭐": recebimento,
            "Finalizar Recebimento ▶️": finalizar_recebimento,
            "Finalizar Expedicao ▶️": finalizar_expedicao,
            "Cancelamento Pedido ❌": Cancelamento_Pedido,

        },
        # Página 2
        {
            "Verificar Blokc AVA ❔": verificar_BLOK_AVA,
            

        }
    ]

    # Variável para controlar a página atual
    pagina_atual = tk.IntVar(value=0)

    # Função para atualizar a página
    def atualizar_pagina():
        # Limpa frame atual
        for widget in botoes_frame.winfo_children():
            widget.destroy()

        # Adiciona botões da página atual
        funcoes = paginas_funcoes[pagina_atual.get()]
        for nome, func in funcoes.items():
            btn = ttk.Button(botoes_frame, text=nome, width=30,
                             command=lambda f=func: threading.Thread(target=f).start())
            btn.pack(pady=5)

        # Atualiza indicador de página
        pagina_label.config(
            text=f"Página {pagina_atual.get() + 1}/{len(paginas_funcoes)}")

        # Configura estado dos botões de navegação
        if pagina_atual.get() == 0:
            btn_anterior.config(state=tk.DISABLED)
        else:
            btn_anterior.config(state=tk.NORMAL)

        if pagina_atual.get() == len(paginas_funcoes) - 1:
            btn_proximo.config(state=tk.DISABLED)
        else:
            btn_proximo.config(state=tk.NORMAL)

    # Frame para os botões de função
    botoes_frame = tk.Frame(main_frame)
    botoes_frame.pack(pady=20)

    # Frame para navegação
    navegacao_frame = tk.Frame(main_frame)
    navegacao_frame.pack(side=tk.BOTTOM, pady=10)

    # Botão página anterior
    btn_anterior = ttk.Button(navegacao_frame, text="←", width=5,
                              command=lambda: [pagina_atual.set(pagina_atual.get() - 1), atualizar_pagina()])
    btn_anterior.pack(side=tk.LEFT, padx=10)

    # Indicador de página
    pagina_label = tk.Label(navegacao_frame, text="", font=("Arial", 10))
    pagina_label.pack(side=tk.LEFT, padx=10)

    # Botão próxima página
    btn_proximo = ttk.Button(navegacao_frame, text="→", width=5,
                             command=lambda: [pagina_atual.set(pagina_atual.get() + 1), atualizar_pagina()])
    btn_proximo.pack(side=tk.LEFT, padx=10)

    # Label de título
    label = tk.Label(main_frame, text="Selecione a função:",
                     font=("Arial", 14, "bold"))
    label.pack(pady=10)

    # Inicializa primeira página
    atualizar_pagina()

    root.mainloop()


if __name__ == "__main__":
    criar_interface()
