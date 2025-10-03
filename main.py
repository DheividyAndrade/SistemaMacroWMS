# main.py
import customtkinter as ctk
import tkinter as tk
import threading
import os
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
)




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
            "Cancelamento Pedido ❌": Cancelamento_Pedido,
        },
        # Página 2
        {
            "Verificar Blokc AVA ❔": verificar_BLOK_AVA,
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
