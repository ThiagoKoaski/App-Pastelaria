import customtkinter as ctk
ctk.set_appearance_mode("dark")
lista_pedidos = None
def enviar_pedido_para_cozinha(mesa, sabores):
    
    global lista_pedidos

    # Se a cozinha ainda não estiver aberta, abre a janela
    if lista_pedidos is None or not lista_pedidos.winfo_exists():
        janela_secundaria_cozinha()

    # Habilita a caixa de texto, insere o pedido e bloqueia novamente
    lista_pedidos.configure(state="normal")
    lista_pedidos.insert("end", f"{mesa}: {', '.join(sabores)}\n")
    lista_pedidos.configure(state="disabled")
    
#Comando para o botão de escolha entre cozinha e balcão funcionar
def janela_secundaria_cozinha():
    global lista_pedidos
    nova_janela = ctk.CTkToplevel(app)
    nova_janela.title("Cozinha")
    nova_janela.geometry("1024x768")
    
    #Força janela abrir em primeiro plano
    nova_janela.after(50, lambda: (
        nova_janela.lift(),
        nova_janela.focus_force(),
    ))
    titulo_cozinha = ctk.CTkLabel(nova_janela, text="LISTA DE ESPERA", font=ctk.CTkFont(family="Arial", size=30, weight="bold" ))
    titulo_cozinha.pack(pady=(15,50))
    
    lista_pedidos = ctk.CTkTextbox(nova_janela, width=800, height=600, font=ctk.CTkFont(family="Arial", size=18))
    lista_pedidos.pack(pady=10)

def janela_secundaria_balcao():
    global lista_pedidos
    nova_janela = ctk.CTkToplevel(app)
    nova_janela.title("Balcão")
    nova_janela.geometry("1024x768")
    
    #Força janela abrir em primeiro plano, o 50 significa os ms para abrir a aba
    nova_janela.after(50, lambda: (
        nova_janela.lift(),
        nova_janela.focus_force(),
    ))
    
    titulo = ctk.CTkLabel(nova_janela, text="SABORES", font=ctk.CTkFont(family="Arial", size=30, weight="bold"))
    titulo.pack(pady=(15, 50)) 
    
    
    #Sabores dos pasteis diponiveis com caixas de seleção, e seleção de mesa com lista suspensa 
    mesas= ctk.CTkComboBox(nova_janela, values=["Mesa 1", "Mesa 2", "Mesa 3", "Mesa 4", "Mesa 5", "Mesa 6"], font=ctk.CTkFont(family="Arial", size=30, weight="bold"))
    mesas.pack(pady=(20,30))  
    
    sabores_frame = ctk.CTkFrame(nova_janela)
    sabores_frame.pack(pady=5)
    
    linha_queijo = ctk.CTkFrame(sabores_frame)
    linha_queijo.pack(pady=5)
    ctk.CTkLabel(linha_queijo, text="Queijo", font=ctk.CTkFont(size=20)).pack(side="left", padx=10)
    queijo = ctk.CTkComboBox(linha_queijo, values=[str(i) for i in range(0, 11)], width=100)
    queijo.set("0")
    queijo.pack(side="left")

    linha_pizza = ctk.CTkFrame(sabores_frame)
    linha_pizza.pack(pady=5)        
    ctk.CTkLabel(linha_pizza, text="Pizza", font=ctk.CTkFont(size=20)).pack(side="left", padx=10)
    pizza = ctk.CTkComboBox(linha_pizza, values=[str(i) for i in range(0, 11)], width=100)
    pizza.set("0")
    pizza.pack(side="left")

    linha_carne = ctk.CTkFrame(sabores_frame)
    linha_carne.pack(pady=5)
    ctk.CTkLabel(linha_carne, text="Carne", font=ctk.CTkFont(size=20)).pack(side="left", padx=10)
    carne = ctk.CTkComboBox(linha_carne, values=[str(i) for i in range(0, 11)], width=100)
    carne.set("0")
    carne.pack(side="left")

    linha_carne_ovos = ctk.CTkFrame(sabores_frame)
    linha_carne_ovos.pack(pady=5)
    ctk.CTkLabel(linha_carne_ovos, text="Carne com ovos", font=ctk.CTkFont(size=20)).pack(side="left", padx=10)
    carne_ovos = ctk.CTkComboBox(linha_carne_ovos, values=[str(i) for i in range(0, 11)], width=100)
    carne_ovos.set("0")
    carne_ovos.pack(side="left")

    
    #Botão de confirmar pedido
    def confirmar_pedido():
        mesa = mesas.get()
        sabores = []
        if int(queijo.get()) > 0: sabores.append(f"\n{queijo.get()} - Queijo")
        if int(pizza.get()) > 0: sabores.append(f"\n{pizza.get()} - Pizza")
        if int(carne.get()) > 0: sabores.append(f"\n{carne.get()} - Carne")
        if int(carne_ovos.get()) > 0: sabores.append(f"\n{carne_ovos.get()} - Carne com ovos")
        
        enviar_pedido_para_cozinha(mesa, sabores)
        
        mesas.set("")
        queijo.set("0")
        pizza.set("0")
        carne.set("0")
        carne_ovos.set("0")

    botao_confirmar = ctk.CTkButton(nova_janela, text="Confirmar Pedido", font=ctk.CTkFont(family="Arial", size=25, weight="bold"), command=confirmar_pedido)
    botao_confirmar.pack(pady=30)    
    
#Janela principal
app = ctk.CTk()
app.title("Pastelaria Paulista")
app.geometry("1024x768")
frame = ctk.CTkFrame(app)
frame.pack(pady=100)
titulo_central= ctk.CTkLabel(frame, text="PASTELARIA PAULISTA APP", font=ctk.CTkFont(family="Arial", size=40, weight="bold"))
titulo_central.pack(pady=(0,50))

#Botões da janela principal
cozinha = ctk.CTkButton(frame, text="Cozinha", font=ctk.CTkFont(family="Arial", size=20, weight="bold"), command=janela_secundaria_cozinha)
cozinha.pack(pady=22)

balcao = ctk.CTkButton(frame, text="Balcão", font=ctk.CTkFont(family="Arial", size=20, weight="bold"), command=janela_secundaria_balcao)
balcao.pack(pady=22)




app.mainloop()