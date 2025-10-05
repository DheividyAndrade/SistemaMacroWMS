import os
import sys
import tkinter as tk
from datetime import datetime
from google.oauth2 import service_account
from googleapiclient.discovery import build
from PIL import Image, ImageTk
import pyautogui
import time
# ========== CONFIGURAÇÕES ==========

IMAGEM_ALVO = os.path.join("image", "logo.jpg")


ARQUIVO_CREDENCIAIS = 'soy-surge-397101-970c2a316ba9.json'
ID_PLANILHA = '1M-VbVx94Y86uNnBUXDjPoEk1VB4kF6YyIQ8n9nkad2k'
NOME_ABA = 'Página1'
ARQUIVO_CHAVE_SALVA = 'chave_acesso.txt'


# ========== SPLASH SCREEN ==========
def executar_api():
    os.system('python api/api.py')

def mostrar_splash():
    splash = tk.Tk()
    splash.overrideredirect(True)
    splash.geometry("400x300+500+300")  # Centraliza
    splash.configure(bg="black")

    try:
        imagem = Image.open(IMAGEM_ALVO)
        imagem = imagem.resize((100, 100))
        imagem_tk = ImageTk.PhotoImage(imagem)
        label_img = tk.Label(splash, image=imagem_tk, bg="black")
        label_img.image = imagem_tk
        label_img.pack(pady=(30, 10))
    except Exception as e:
        print("Erro ao carregar imagem:", e)

    tk.Label(splash, text="DH Scripts", font=(
        "Helvetica", 24, "bold"), fg="white", bg="black").pack()
    tk.Label(splash, text="Iniciando...", font=("Helvetica", 12),
             fg="gray", bg="black").pack(pady=(10, 0))
    # Contato no canto inferior direito
    contato_label = tk.Label(splash, text="Cel. (82) 99121-7317",
                             font=("Helvetica", 10),
                             fg="white", bg="black")
    contato_label.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)

    def fechar():
        splash.destroy()

    splash.after(5000, fechar)
    splash.mainloop()


# ========== INÍCIO DO PROGRAMA ==========
mostrar_splash()

# ========== FUNÇÕES AUXILIARES ==========


def carregar_credenciais():
    if not os.path.exists(ARQUIVO_CREDENCIAIS):
        pyautogui.alert(
            f"Arquivo de credenciais '{ARQUIVO_CREDENCIAIS}' não encontrado.")
        return None
    try:
        creds = service_account.Credentials.from_service_account_file(
            ARQUIVO_CREDENCIAIS)
        service = build('sheets', 'v4', credentials=creds)
        return service
    except Exception as e:
        pyautogui.alert(f"Erro ao carregar as credenciais do Google:\n{e}")
        return None


def verificar_chave(chave_usuario):
    service = carregar_credenciais()
    if not service:
        return False
    try:
        sheet = service.spreadsheets()
        resultado = sheet.values().get(spreadsheetId=ID_PLANILHA,
                                       range=f"{NOME_ABA}!A2:C").execute()
        valores = resultado.get('values', [])

        for linha in valores:
            if len(linha) >= 3:
                chave, status, data_expiracao = linha[0].strip(
                ), linha[1].strip().lower(), linha[2].strip()
                if chave_usuario.strip() == chave and status == 'sim':
                    try:
                        data_exp = datetime.strptime(
                            data_expiracao, "%Y-%m-%d").date()
                        hoje = datetime.now().date()
                        if hoje <= data_exp:
                            return True
                        else:
                            pyautogui.alert("❌ Chave expirada.")
                            return False
                    except ValueError:
                        pyautogui.alert(
                            f"⚠️ Data inválida para a chave '{chave}'.")
                        return False
        return False
    except Exception as e:
        pyautogui.alert(f"Erro ao acessar a planilha:\n{e}")
        return False


def salvar_chave_local(chave):
    with open(ARQUIVO_CHAVE_SALVA, 'w') as f:
        f.write(chave)

# ========== VERIFICAÇÃO DA CHAVE ==========


chave_digitada = pyautogui.prompt("🔐 Digite sua chave de acesso:")

if not chave_digitada:
    pyautogui.alert("❌ Nenhuma chave foi digitada. Encerrando.")
    sys.exit()

if verificar_chave(chave_digitada):
    salvar_chave_local(chave_digitada)
    pyautogui.alert("✅ Chave válida! Bot liberado!")
else:
    pyautogui.alert("❌ Chave inválida, inativa ou expirada. Bot bloqueado.")
    sys.exit()

time.sleep(1)  # Pequena pausa antes de iniciar o bot