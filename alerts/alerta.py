# alerts/alerta.py
import customtkinter as ctk
import tkinter as tk

def meu_alert(msg, titulo="Alerta", botao="OK"):
    """
    Mostra um alerta modal com botão OK no canto superior direito.
    Retorna True se clicou OK, False se clicou X.
    """
    resposta = {"ok": False}

    def on_ok():
        resposta["ok"] = True
        win.destroy()

    def on_close():
        resposta["ok"] = False
        win.destroy()

    root = ctk.CTk()
    root.withdraw()  # esconde janela principal
    
    win = ctk.CTkToplevel(root)
    win.title(titulo)
    win.geometry("300x120")
    win.resizable(False, False)
    
    # POSICIONAMENTO NO CANTO SUPERIOR DIREITO
    # Obtém as dimensões da tela
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    
    # Calcula a posição (canto superior direito)
    x_position = screen_width - 320  # 300 (largura) + 20 (margem)
    y_position = 50  # 50 pixels do topo
    
    # Define a posição da janela
    win.geometry(f"300x120+{x_position}+{y_position}")
    
    win.grab_set()  # bloqueia interação com outras janelas
    win.protocol("WM_DELETE_WINDOW", on_close)

    # Conteúdo do alerta
    ctk.CTkLabel(win, text=msg, padx=10, pady=10).pack(expand=True)
    ctk.CTkButton(win, text=botao, width=100, command=on_ok).pack(pady=10)

    # Traz a janela para frente
    win.lift()
    win.focus_force()
    
    root.wait_window(win)  # espera apenas essa janela fechar
    root.destroy()
    return resposta["ok"]