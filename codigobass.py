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






# ---------------------------


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
