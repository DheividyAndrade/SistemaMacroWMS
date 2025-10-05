# main.py
import customtkinter as ctk
import tkinter as tk
import threading
import os
import sys
import pyautogui
import time
from datetime import datetime
from google.oauth2 import service_account
from googleapiclient.discovery import build
from PIL import Image, ImageTk



# from imagesearch import telainicial  # Removido devido a erro de importação

# Importando funções do WMS

from functions.funcoes import (
    verificar_empdoc,
    verificar_uz_faltando,
    coletor,
    reconferir_uz,
    etiqueta_uz,
    etiqueta_variadas,
    Associar,
    Cadastro_Motorista,
    reservar,
    Liberar_EMP,
    Expedição,
    recebimento,
    finalizar_recebimento,
    finalizar_expedicao,
    Cancelamento_Pedido,
    verificar_BLOK_AVA,
    finalizar_faturamento,
    Erro_Motorista,
    Desbloquear_UZ,
    login_porta_admim,
    faturar_stine,
)

IMAGEM_ALVO = os.path.join("image", "logo.jpg")




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


# Configurar CustomTkinter
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


def criar_interface():
    root = ctk.CTk()
    root.title("Automação WMS")
    root.geometry("450x650")

    # Frame principal
    main_frame = ctk.CTkFrame(root)
    main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

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
            "Finalizar Faturamento ▶️": finalizar_faturamento,

        },
        # Página 2
        {
            "Desbloquear UZ 🔓": Desbloquear_UZ,
            "Verificar Blokc AVA ❔": verificar_BLOK_AVA,
            "Erro Motorista ❗": Erro_Motorista,
            "Cancelamento Pedido ❌": Cancelamento_Pedido,
            "Faturar Stine 💲": faturar_stine,
            "Login Porta Admin 🔑": login_porta_admim,
        }
    ]

    # Variável para controlar a página atual
    pagina_atual = ctk.IntVar(value=0)

    # Label de título
    label = ctk.CTkLabel(main_frame, text="Selecione a função:",
                         font=ctk.CTkFont(size=16, weight="bold"))
    label.pack(pady=10)

    # Container para a área scrollável (com altura fixa)
    container_scroll = ctk.CTkFrame(main_frame)
    container_scroll.pack(fill=tk.BOTH, expand=True, pady=10)
    # Impede que o container redimensione
    container_scroll.pack_propagate(False)

    # Configurar altura do container scrollável
    container_scroll.configure(height=450)

    # Canvas para scrolling
    canvas = tk.Canvas(container_scroll, highlightthickness=0, bg='#2b2b2b')
    scrollbar = ctk.CTkScrollbar(
        container_scroll, orientation="vertical", command=canvas.yview)

    # Frame scrollável que vai dentro do canvas
    scrollable_frame = ctk.CTkFrame(canvas)

    # Configurar o sistema de scroll
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    # Colocar o frame scrollável no canvas
    canvas.create_window((0, 0), window=scrollable_frame,
                         anchor="nw", width=canvas.winfo_reqwidth())
    canvas.configure(yscrollcommand=scrollbar.set)

    # Frame para os botões
    botoes_frame = ctk.CTkFrame(scrollable_frame)
    botoes_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Empacotar canvas e scrollbar
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Função para scroll com mouse
    def on_mousewheel(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    # Vincular evento de scroll apenas ao canvas
    canvas.bind("<MouseWheel>", on_mousewheel)

    # Frame para navegação (FORA do container scrollável)
    navegacao_frame = ctk.CTkFrame(main_frame)
    navegacao_frame.pack(side=tk.BOTTOM, pady=10, fill=tk.X)

    # Botão página anterior
    btn_anterior = ctk.CTkButton(navegacao_frame, text="←", width=40,
                                 command=lambda: [pagina_atual.set(pagina_atual.get() - 1), atualizar_pagina()])
    btn_anterior.pack(side=tk.LEFT, padx=10)

    # Indicador de página
    pagina_label = ctk.CTkLabel(
        navegacao_frame, text="", font=ctk.CTkFont(size=12))
    pagina_label.pack(side=tk.LEFT, padx=10)

    # Botão próxima página
    btn_proximo = ctk.CTkButton(navegacao_frame, text="→", width=40,
                                command=lambda: [pagina_atual.set(pagina_atual.get() + 1), atualizar_pagina()])
    btn_proximo.pack(side=tk.LEFT, padx=10)

    # Função para atualizar a página
    def atualizar_pagina():
        # Limpa frame atual
        for widget in botoes_frame.winfo_children():
            widget.destroy()

        # Adiciona botões da página atual
        funcoes = paginas_funcoes[pagina_atual.get()]
        for nome, func in funcoes.items():
            btn = ctk.CTkButton(botoes_frame, text=nome, width=300,
                                height=35, command=lambda f=func: threading.Thread(target=f).start())
            btn.pack(pady=8)

        # Atualiza indicador de página
        pagina_label.configure(
            text=f"Página {pagina_atual.get() + 1}/{len(paginas_funcoes)}")

        # Configura estado dos botões de navegação
        if pagina_atual.get() == 0:
            btn_anterior.configure(state="disabled")
        else:
            btn_anterior.configure(state="normal")

        if pagina_atual.get() == len(paginas_funcoes) - 1:
            btn_proximo.configure(state="disabled")
        else:
            btn_proximo.configure(state="normal")

        # Atualizar o scroll após adicionar os botões
        root.update_idletasks()
        canvas.configure(scrollregion=canvas.bbox("all"))

    # Ajustar largura do canvas quando o container for redimensionado
    def ajustar_largura_canvas(event):
        canvas.itemconfig("all", width=event.width)
        canvas.configure(width=event.width)

    scrollable_frame.bind("<Configure>", ajustar_largura_canvas)

    # Inicializa primeira página
    atualizar_pagina()

    root.mainloop()


if __name__ == "__main__":
    criar_interface()
