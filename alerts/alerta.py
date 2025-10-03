# alerts/alerta.py
import customtkinter as ctk
import tkinter as tk
import threading

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

    root = ctk.CTk()
    root.withdraw()  # esconde janela principal
    win = ctk.CTkToplevel(root)
    win.title(titulo)
    win.geometry("300x120")
    win.resizable(False, False)
    win.grab_set()  # bloqueia interação com outras janelas
    win.protocol("WM_DELETE_WINDOW", on_close)

    ctk.CTkLabel(win, text=msg, padx=10, pady=10).pack()
    ctk.CTkButton(win, text=botao, width=10, command=on_ok).pack(pady=10)

    root.wait_window(win)  # espera apenas essa janela fechar
    root.destroy()
    return resposta["ok"]