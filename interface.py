import tkinter as tk
from tkinter import Tk, StringVar, ttk, messagebox
from tkinter import *

## Importar imagem
from PIL import Image, ImageTk

## Gráfico 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure 

# Lista de Cores ---------------------------------------------------------------------------------------------

cores = {
    '1. Cores Básicas': {
        'vermelho': '#FF0000',
        'verde': '#00FF00',
        'azul': '#0000FF',
        'amarelo': '#FFFF00',
        'ciano': '#00FFFF',
        'magenta': '#FF00FF',
        'azul escuro': '#00008B'
    },
    '2. Cores Secundárias': {
        'laranja': '#FFA500',
        'roxo': '#800080',
        'rosa': '#FFC0CB',
        'marrom': '#A52A2A'
    },
    '3. Tons de Cinza': {
        'branco': '#FFFFFF',
        'cinza claro': '#D3D3D3',
        'cinza': '#808080',
        'cinza escuro': '#A9A9A9',
        'preto': '#000000'
    }
}

# Escolher as cores que serão utilizadas 
color = ["#FFA500", '#D3D3D3', '#00FF00', '#00FF00', '#FFFF00', '#FF0000']

# Criar uma janela ------------------------------------------------------

janela = Tk()  # Criar uma janela vazia
janela.title("")  # Definir o título
janela.geometry("840x650")  # Tamanho altura e largura
janela.configure(background='#FFFFFF') ## Cor de Fundo 
janela.resizable(width=False, height=False)

style = ttk.Style(janela)  # Aplicar o estilo que foi escolhido 

## Dividir a janela utilizando frames (Definir cada quadrante da interface) --------------------------------------------

# width: Largura (dimensão)
# height: Altura (dimensão)
# bg: define a cor de fundo.
# fg: cor das palavras
# pady: controla o espaçamento vertical interno.
# relief:define o estilo da borda do Frame.
# sticky: é usado para alinhar o widget 
# padx: define o espaçamento adicional horizontal interno

#---------------------------------------------------------------------------------------------------------------------

frameCima = Frame(janela, width = 1043, height = 50, bg = '#FFFFFF') ## Faixa do Título -- Branco
frameCima.grid(row = 0, column = 0)

frameMeio = Frame(janela, width = 1043, height = 290, bg = '#FFFFFF', padx = 10) ## Janela do meio -- Branco
frameMeio.grid(row = 1, column = 0)

frameEsquerda = Frame(frameMeio, width = 250, height = 290, bg = '#D3D3D3', pady = 0, relief = "raised") ## Janeja que vai ficar a esquerda -- Cinza 
frameEsquerda.place(x = 0, y = 5)

frameDireita = Frame(frameMeio, width = 630, height = 290, bg = '#FFFFFF', pady = 0, relief = "raised") ## Frame onde ficará o gráfico
frameDireita.place(x = 250, y = 5)

frame_baixo = Frame(janela, width = 820, height = 300, bg = '#FFFFFF')
frame_baixo.grid(row = 2, column = 0, pady = 0, padx = 10, sticky = NSEW)

## Inserir a Logo ---------------------------------------------------------------------------------------------------

logo = Label(frameCima, # Posição 
             text="Orçamento de Viagem", # Texto
             compound = LEFT, # Posição da imagem
             padx=5, # define o espaçamento adicional horizontal interno
             anchor=NW, ## Controlar a posição
             font=("Verdana 20"), ## Fonte do texto
             bg='#FFFFFF', ## Cor de fundo 
             fg='#FFA500') # Cor das palavras
logo.place(x= 0, y = 0) # posiciona o Label no canto superior esquerdo da janela principal

# Adicionar a imagem ------------------------------------------------------------------------------------------------

logo_img = Image.open("logo.png")  # Carregar a imagem
logo_img = logo_img.resize((45, 45))  # Redimensionar a imagem conforme necessário
logo_img = ImageTk.PhotoImage(logo_img)  # Converter para o formato do tkinter

imagem = Label(frameCima,
                 image=logo_img, # Imagem que sera colocado no app
                 width=900, # Largura
                 compound = LEFT, #Posição da imagem
                 padx=5, # É usado para posicionar os widgets na janela principal 
                 anchor=NW, ## Controlar a posição
                 bg= '#FFFFFF', ## Cor de fundo
                 fg= '#FFFFFF') ## Cor das palavras

imagem.place(x = 320, y = 0)  ## Posicionamento 


## Frame esquerdo ------------------------------------------------------------------------------------------

# Definir os widgets no frameEsquerda ---------------------------------------
def Totais():
    l_nome = Label(frameEsquerda, ## Posição à esquerda
                   text="Orçamento e despesas", 
                   width=32, # Largura
                   anchor=tk.NW, # Controlar a posição
                   font=("Arial Black", 12), # Fonte
                   bg='#00008B', #Cor de fundo
                   fg='#FFFFFF') # COr das palavras
    l_nome.place(x=0, y=0)

    # Orçamento total ---------------------------------------------------------
    l_total = Label(frameEsquerda, # Posição dos resultados 
                    text="Orçamento Total:", 
                    anchor=tk.E,
                    font=("Arial", 12),
                    bg='#D3D3D3',
                    fg='#000000')
    l_total.place(x=10, y=50)

    valor_total = 10000  # Exemplo de valor, você pode ajustar conforme necessário

    l_orcamento_total = Label(frameEsquerda, 
                              text="R$ {:,.2f}".format(valor_total), # Resultado do orçamento total
                              width=20, #Largura
                              anchor=tk.NW,
                              font=("Arial", 12),
                              bg='#FFFFFF',
                              fg='#000000')
    l_orcamento_total.place(x=10, y=80)

    # Despesa Total -----------------------------------------------------------
    l_despesa = Label(frameEsquerda, 
                      text="Despesas Totais: ",
                      anchor=tk.NW,
                      font=("Arial", 12),
                      bg='#D3D3D3',
                      fg='#000000')
    l_despesa.place(x=10, y=120)

    valor_despesa = 10000

    l_orcamento_despesas = Label(frameEsquerda, 
                                 text="R$ {:,.2f}".format(valor_despesa),
                                 width=20,
                                 anchor=tk.NW,
                                 font=("Arial", 12),
                                 bg='#FFFFFF',
                                 fg='#000000')
    l_orcamento_despesas.place(x=10, y=150)

    # Restante total ----------------------------------------------------------
    l_resto = Label(frameEsquerda, 
                    text="Total restante:",
                    anchor=tk.NW,
                    font=("Arial", 12),
                    bg='#D3D3D3', # Azul escuro
                    fg='#000000' ## Preto
                    )
    l_resto.place(x=10, y=190)

    valor_resto = 10000

    l_orcamento_resto = Label(frameEsquerda, 
                              text="R$ {:,.2f}".format(valor_resto),
                              width=20,
                              anchor=tk.NW,
                              font=("Arial", 12),
                              bg='#FFFFFF', # Branco 
                              fg='#000000' # Preto
                              )
    l_orcamento_resto.place(x=10, y=220)

# Gráfico --------------------------------------------------------------------
def grafico():
    figura = plt.Figure(figsize=(7, 4), dpi=87) 
    ax = figura.add_subplot(111)

    lista_valores = [56, 98, 52, 65]
    lista_categoria = ['Alimentação', "Transporte", "Acomodação", "Outros"]

    explode = []  # Destacar a primeira fatia

    for i in lista_categoria:
        explode.append(0.05)

    ax.pie(lista_valores,
           explode=explode,
           wedgeprops=dict(width=0.2),
           autopct="%1.1f%%",
           shadow=True,
           startangle=90)

    ax.legend(lista_categoria, loc="center right", bbox_to_anchor = (1.55, 0.50))

    ##Frame pie
    frame_meio_pie = Frame(frameDireita, 
                           width=600,
                           height=290,
                           bg = '#FFFFFF', ## Branco
                           pady=0, 
                           relief="raised")
    
    frame_meio_pie.place(x=-140, y=-25)

    l_nome = Label(frameDireita, 
                   text="Relatório das despesas da viagem",
                   width=83,
                   height=1,
                   anchor=CENTER,
                   padx=2,
                   font = ("Arial Black", 12), 
                   bg = '#000000', ## Cor preto
                   fg = '#FFFFFF' ## Branco
                   )
    l_nome.place(x=0, y=0)

    canvas = FigureCanvasTkAgg(figura, master=frame_meio_pie)
    canvas.get_tk_widget().grid(row=0, column=0, padx=0)


## Frames das tabelas dinamicas --------------------------------------------------------------------------------------
l_nome = Label(frame_baixo, text="Descrição das despesas",
               width=83,# Largura
               height=1, # altura
               anchor= CENTER,
               padx = 2,
               font=("Arial Black", 12),
               bg='#000000',# Preto
               fg = '#FFFFFF' ## Branco
                )
l_nome.grid(row = 0, column=0, columnspan=6, pady=0)

frame_tabela = Frame(frame_baixo, width=300, height=250, bg = '#FFFFFF')
frame_tabela.grid(row=1, column= 0, pady=0)

frame_operacoes = Frame(frame_baixo, width = 220, height=250, bg = '#FFFFFF')
frame_operacoes.grid(row=1, column=1, padx=5)

frame_configuracoes = Frame(frame_baixo, width=350, height=250, bg='#FFFFFF')
frame_configuracoes.grid(row=1, column= 2, padx=5)

## Criar a função para a renda 
def mostrar_renda():
    # Cabeçalho da tabela
    tabela = ["id", "Tipo", "Descrição", "Total"]
    
    global tree  # Se você planeja acessar a treeview fora desta função

    # Criar a treeview (ttk.Treeview)
    tree = ttk.Treeview(frame_tabela, selectmode="extended", columns=tabela, show="headings")

    vsb = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky="nsew")
    vsb.grid(column=1, row=0, sticky="ns")
    hsb.grid(column=0, row=1, sticky="ew")

    # Configurar cabeçalhos e colunas da treeview
    for col in tabela:
        tree.heading(col, text=col.title())
        tree.column(col, width=100, anchor="center")  # Ajuste a largura conforme necessário

    # Função para adicionar um novo item à treeview
    def adicionar_item():
        # Capturar valores inseridos pelo usuário
        tipo = categoria_despesas.get()
        descricao = e_descricao.get()
        total = e_valor_quantia.get()

        # Validar os dados, se necessário
        # Por exemplo, você pode verificar se o total é um número válido

        # Inserir os dados na treeview
        tree.insert("", "end", values=(len(tree.get_children()) + 1, tipo, descricao, total))

        # Limpar os campos de entrada após a inserção
        categoria_despesas.set('')
        e_descricao.delete(0, 'end')
        e_valor_quantia.delete(0, 'end')

    # Botão para adicionar novo item
    btn_adicionar = Button(frame_operacoes, text="Adicionar", command=adicionar_item)
    btn_adicionar.place(x=10, y=180)

# Exemplo de como chamar a função para mostrar a tabela
mostrar_renda()

mostrar_renda() ## Mostrar funções


# Configurações de despesas -------------------------------------------------------
l_info = Label(frame_operacoes, text="Insira novas despesas", anchor=NW, font=("Calibre 12 bold"),
               bg = "#FFFFFF", fg = "#000000")
l_info.place(x=10, y=10)

## Criar caixa de seleção

### Icone categoria -----------------------
l_categoria = Label(frame_operacoes, text="Categoria", height=1, anchor=NW, font=("Arial 10"),
               bg = "#FFFFFF", fg = "#000000") # nome da caixa de seleção
l_categoria.place(x=10, y=40)

## Caixa de seleção da Categoria
categorias = ["Transporte", "Alimentação", "Entretenimento", "Hospedagem", "Outros"]
categoria_despesas = ttk.Combobox(frame_operacoes, width=12, font=("Arial 10"))
categoria_despesas['value'] = (categorias)
categoria_despesas.place(x = 80, y = 41)

## Caixa de seleção da Descrição
l_descricao = Label(frame_operacoes, text="Descrição", height=1, anchor=NW, font=("Arial 10"),
               bg = "#FFFFFF", fg = "#000000") # nome da caixa de seleção
l_descricao.place(x=10, y=70)
e_descricao = Entry(frame_operacoes, width=16, justify="left", relief="solid")
e_descricao.place(x=80, y=71)

## Caixa de seleção da quantia
l_valor_quantia = Label(frame_operacoes, text="Quantia", height=1, anchor=NW, font=("Arial 10"),
               bg = "#FFFFFF", fg = "#000000") # nome da caixa de seleção
l_valor_quantia.place(x=10, y=120)
e_valor_quantia = Entry(frame_operacoes, width=16, justify="left", relief="solid")
e_valor_quantia.place(x=80, y=121)

## Botão de inserir 
add_adicionar = Image.open("adicionar.png")
add_adicionar = add_adicionar.resize((17,17))
add_adicionar = ImageTk.PhotoImage(add_adicionar)
inserir_despesas = Button(frame_operacoes, image=add_adicionar, compound=LEFT, anchor= NW,
                          text="Adicionar".upper(), width=94, overrelief=RIDGE,
                           font=("Arial 9 bold"), bg="#FFFFFF", fg="#000000")
inserir_despesas.place(x=80, y=151)
# Configuração do botão de inserir na configuração das quantias total
inserir_despesas.config(command=inserir_quantia_total)


## Configuração das quantias Total-------------------Atualizar ----------------------------------------------

l_descricao = Label(frame_configuracoes, text="Atualizar quantia total", height=1, anchor=NW, font=("Calibre 12 bold"),
               bg = "#FFFFFF", fg = "#000000") # nome da caixa de seleção
l_descricao.place(x=10, y=10)

## Caixa de seleção da quantia
l_valor_quantia = Label(frame_configuracoes, text="Quantia Total", height=1, anchor=NW, font=("Arial 10"),
               bg = "#FFFFFF", fg = "#000000") # nome da caixa de seleção
l_valor_quantia.place(x=10, y=40)
e_valor_quantia = Entry(frame_configuracoes, width=16, justify="left", relief="solid")
e_valor_quantia.place(x=110, y=41)

## Botão de Atualizar
atualizar = Image.open("atualizar.png")
atualizar = atualizar.resize((17,17))
atualizar = ImageTk.PhotoImage(atualizar)
atualizar_despesas = Button(frame_configuracoes, image=atualizar, compound=LEFT, anchor= NW,
                          text="Atualizar".upper(), width=94, overrelief=RIDGE,
                           font=("Arial 9 bold"), bg="#FFFFFF", fg="#000000")
atualizar_despesas.place(x=110, y=70)
# Configuração do botão de atualizar na configuração das quantias total
atualizar_despesas.config(command=atualizar_quantia_total)
## Operação Excluir -----------------------------------------------------------------------------------------------

# Carregar imagem para o botão "Cancelar"
excluir_img = Image.open("cancelar.png")
excluir_img = excluir_img.resize((17, 17))
excluir_img_tk = ImageTk.PhotoImage(excluir_img)
# Botão para cancelar
excluir_despesas = Button(frame_configuracoes, image=excluir_img_tk, compound=LEFT, anchor=NW,
                          text="Cancelar".upper(), width=94, overrelief=RIDGE,
                          font=("Arial 9 bold"), bg="#FFFFFF", fg="#000000",
                          )
excluir_despesas.place(x=110, y=120)


grafico()
Totais()

## Estilo do cabeçalho da tabela 
style.theme_use("clam")
style.configure("Treeview", highlightthickness = 0, bd=0, font=("Calibri", 9))

# Iniciar o loop principal da interface gráfica
janela.mainloop()



