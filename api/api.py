import os
import sys
from datetime import datetime
from google.oauth2 import service_account
from googleapiclient.discovery import build
from PIL import Image
import pyautogui
import time
import customtkinter as ctk

# ========== CONFIGURAÇÕES ==========
ctk.set_appearance_mode("Dark")  # Modos: "System", "Dark", "Light"
ctk.set_default_color_theme("blue")  # Temas: "blue", "green", "dark-blue"

IMAGEM_ALVO = os.path.join("image", "logo.jpg")
ARQUIVO_CREDENCIAIS = 'soy-surge-397101-970c2a316ba9.json'
ID_PLANILHA = '1M-VbVx94Y86uNnBUXDjPoEk1VB4kF6YyIQ8n9nkad2k'
NOME_ABA = 'Página1'
ARQUIVO_CHAVE_SALVA = 'chave_acesso.txt'

# ========== SPLASH SCREEN ==========
def executar_api():
    os.system('python api/api.py')

def mostrar_splash():
    splash = ctk.CTk()
    splash.overrideredirect(True)
    
    # Centralizar na tela
    largura = 400
    altura = 300
    x = (splash.winfo_screenwidth() - largura) // 2
    y = (splash.winfo_screenheight() - altura) // 2
    splash.geometry(f"{largura}x{altura}+{x}+{y}")
    
    splash.configure(fg_color="black")

    try:
        imagem = Image.open(IMAGEM_ALVO)
        imagem = imagem.resize((100, 100))
        label_img = ctk.CTkLabel(splash, image=ctk.CTkImage(light_image=imagem, dark_image=imagem, size=(100, 100)), text="")
        label_img.pack(pady=(30, 10))
    except Exception as e:
        print("Erro ao carregar imagem:", e)

    ctk.CTkLabel(splash, text="DH Scripts", font=("Helvetica", 24, "bold"), 
                text_color="white", fg_color="black").pack()
    ctk.CTkLabel(splash, text="Iniciando...", font=("Helvetica", 12),
                text_color="gray", fg_color="black").pack(pady=(10, 0))
    
    # Contato no canto inferior direito
    contato_label = ctk.CTkLabel(splash, text="Cel. (82) 99121-7317",
                                font=("Helvetica", 10),
                                text_color="white", fg_color="black")
    contato_label.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)

    def fechar():
        splash.destroy()

    splash.after(5000, fechar)
    splash.mainloop()

# ========== FUNÇÕES AUXILIARES ==========
def carregar_credenciais():
    if not os.path.exists(ARQUIVO_CREDENCIAIS):
        mostrar_alerta("Erro", f"Arquivo de credenciais '{ARQUIVO_CREDENCIAIS}' não encontrado.")
        return None
    try:
        creds = service_account.Credentials.from_service_account_file(ARQUIVO_CREDENCIAIS)
        service = build('sheets', 'v4', credentials=creds)
        return service
    except Exception as e:
        mostrar_alerta("Erro", f"Erro ao carregar as credenciais do Google:\n{e}")
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
                chave, status, data_expiracao = linha[0].strip(), linha[1].strip().lower(), linha[2].strip()
                if chave_usuario.strip() == chave and status == 'sim':
                    try:
                        data_exp = datetime.strptime(data_expiracao, "%Y-%m-%d").date()
                        hoje = datetime.now().date()
                        if hoje <= data_exp:
                            return True
                        else:
                            mostrar_alerta("Aviso", "❌ Chave expirada.")
                            return False
                    except ValueError:
                        mostrar_alerta("Aviso", f"⚠️ Data inválida para a chave '{chave}'.")
                        return False
        return False
    except Exception as e:
        mostrar_alerta("Erro", f"Erro ao acessar a planilha:\n{e}")
        return False

def salvar_chave_local(chave):
    with open(ARQUIVO_CHAVE_SALVA, 'w') as f:
        f.write(chave)

# ========== DIALOGOS PERSONALIZADOS ==========
def mostrar_alerta(titulo, mensagem):
    """Substitui pyautogui.alert com CustomTkinter"""
    alerta = ctk.CTkToplevel()
    alerta.title(titulo)
    alerta.geometry("300x150")
    alerta.resizable(False, False)
    alerta.transient()
    alerta.grab_set()
    
    # Centralizar
    alerta.update_idletasks()
    x = (alerta.winfo_screenwidth() - 300) // 2
    y = (alerta.winfo_screenheight() - 150) // 2
    alerta.geometry(f"300x150+{x}+{y}")
    
    ctk.CTkLabel(alerta, text=mensagem, wraplength=280).pack(pady=20)
    ctk.CTkButton(alerta, text="OK", command=alerta.destroy).pack(pady=10)

def pedir_chave():
    """Substitui pyautogui.prompt com CustomTkinter"""
    dialog = ctk.CTkToplevel()
    dialog.title("Acesso ao Sistema")
    dialog.geometry("400x200")
    dialog.resizable(False, False)
    dialog.transient()
    dialog.grab_set()
    
    # Centralizar
    dialog.update_idletasks()
    x = (dialog.winfo_screenwidth() - 400) // 2
    y = (dialog.winfo_screenheight() - 200) // 2
    dialog.geometry(f"400x200+{x}+{y}")
    
    resultado = {"chave": ""}
    
    def confirmar():
        resultado["chave"] = entrada.get()
        dialog.destroy()
    
    def cancelar():
        dialog.destroy()
    
    ctk.CTkLabel(dialog, text="🔐 Digite sua chave de acesso:", 
                font=("Helvetica", 14)).pack(pady=20)
    
    entrada = ctk.CTkEntry(dialog, width=300, placeholder_text="Chave de acesso...")
    entrada.pack(pady=10)
    entrada.bind("<Return>", lambda e: confirmar())
    
    frame_botoes = ctk.CTkFrame(dialog, fg_color="transparent")
    frame_botoes.pack(pady=20)
    
    ctk.CTkButton(frame_botoes, text="Confirmar", command=confirmar).pack(side="left", padx=10)
    ctk.CTkButton(frame_botoes, text="Cancelar", command=cancelar, fg_color="gray").pack(side="left", padx=10)
    
    entrada.focus()
    dialog.wait_window()
    
    return resultado["chave"]

# ========== INÍCIO DO PROGRAMA ==========
mostrar_splash()

# ========== VERIFICAÇÃO DA CHAVE ==========
chave_digitada = pedir_chave()

if not chave_digitada:
    mostrar_alerta("Erro", "❌ Nenhuma chave foi digitada. Encerrando.")
    sys.exit()

if verificar_chave(chave_digitada):
    salvar_chave_local(chave_digitada)
    mostrar_alerta("Sucesso", "✅ Chave válida! Bot liberado!")
else:
    mostrar_alerta("Erro", "❌ Chave inválida, inativa ou expirada. Bot bloqueado.")
    sys.exit()

time.sleep(1)  # Pequena pausa antes de iniciar o bot