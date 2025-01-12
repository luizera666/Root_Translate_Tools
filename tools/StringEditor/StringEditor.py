import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import re
import os

# Função para carregar arquivo e extrair chaves e strings
def carregar_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as f:
        conteudo = f.readlines()

    linhas = {}
    padrao = re.compile(r"^(.*?)=(.*)$")  # Regex para separar chave e string

    for linha in conteudo:
        match = padrao.match(linha.strip())
        if match:
            chave, string = match.groups()
            chave = chave.strip()
            string = string.strip()
            linhas[chave] = string

    return linhas

# Função para iniciar uma nova tradução
def nova_traducao():
    caminho_arquivo_ingles = filedialog.askopenfilename(title="Selecione o arquivo original em inglês")

    if not caminho_arquivo_ingles:
        messagebox.showerror("Erro", "Você precisa selecionar o arquivo original em inglês.")
        return

    # Carregar as linhas do arquivo em inglês
    linhas_ingles = carregar_arquivo(caminho_arquivo_ingles)

    # Limpar a tabela antes de preencher
    for widget in tabela.get_children():
        tabela.delete(widget)

    # Preencher a tabela apenas com as strings em inglês (strings em português vazias)
    for i, chave in enumerate(linhas_ingles):
        string_ingles = linhas_ingles[chave]
        tabela.insert("", "end", values=(i + 1, chave, string_ingles, ""))

    # Atualizar contador de linhas
    contador_linhas.config(text=f"Linhas carregadas: {len(linhas_ingles)}")

# Função para abrir uma tradução em andamento
def abrir_traducao():
    caminho_arquivo_ingles = filedialog.askopenfilename(title="Selecione o arquivo original em inglês")
    caminho_arquivo_portugues = filedialog.askopenfilename(title="Selecione o arquivo traduzido")

    if not caminho_arquivo_ingles or not caminho_arquivo_portugues:
        messagebox.showerror("Erro", "Você precisa selecionar ambos os arquivos.")
        return

    # Carregar as linhas dos dois arquivos
    linhas_ingles = carregar_arquivo(caminho_arquivo_ingles)
    linhas_portugues = carregar_arquivo(caminho_arquivo_portugues)

    # Limpar a tabela antes de preencher
    for widget in tabela.get_children():
        tabela.delete(widget)

    # Preencher a tabela com chave, string em inglês e string em português
    for i, chave in enumerate(linhas_ingles):
        string_ingles = linhas_ingles[chave]
        string_portugues = linhas_portugues.get(chave, "")
        tabela.insert("", "end", values=(i + 1, chave, string_ingles, string_portugues))

    # Atualizar contador de linhas
    contador_linhas.config(text=f"Linhas carregadas: {len(linhas_ingles)}")

# Função para salvar apenas as traduções editadas
def salvar_arquivo():
    caminho_saida = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Arquivo de Texto", "*.txt")])
    if not caminho_saida:
        return

    # Obter os valores editados da tabela
    linhas_editadas = []
    for item in tabela.get_children():
        chave, _, string_portugues = tabela.item(item, "values")[1:]  # Pegar chave e string traduzida
        linhas_editadas.append(f"{chave}={string_portugues}\n")  # Salvar apenas a tradução

    # Salvar no arquivo selecionado
    with open(caminho_saida, "w", encoding="utf-8") as f:
        f.writelines(linhas_editadas)

    messagebox.showinfo("Sucesso", f"Arquivo salvo como: {caminho_saida}")

# Variáveis globais para navegação
resultados_busca = []  # Lista de IDs dos itens encontrados
indice_atual = -1  # Índice do resultado atual

# Função para buscar termo nas colunas
def buscar_termo():
    global resultados_busca, indice_atual

    termo = entrada_busca.get().strip().lower()
    if not termo:
        messagebox.showwarning("Aviso", "Digite um termo para buscar.")
        return

    # Limpar destaques anteriores
    limpar_destaques()

    resultados_busca = []  # Reiniciar lista de resultados
    indice_atual = -1  # Reiniciar índice atual

    # Percorrer todas as linhas da tabela
    for item in tabela.get_children():
        valores = tabela.item(item, "values")
        string_ingles = valores[2].lower()
        string_portugues = valores[3].lower()

        # Verificar se o termo está presente em uma das colunas
        if termo in string_ingles or termo in string_portugues:
            resultados_busca.append(item)
            tabela.item(item, tags=("destaque",))

    if resultados_busca:
        indice_atual = 0
        navegar_resultados()
    else:
        messagebox.showinfo("Resultado", "Nenhum resultado encontrado.")

# Função para limpar destaques
def limpar_destaques():
    for item in tabela.get_children():
        tabela.item(item, tags=())

# Função para navegar entre os resultados
def navegar_resultados(direcao=0):
    global indice_atual

    if not resultados_busca:
        return

    indice_atual += direcao
    if indice_atual < 0:
        indice_atual = 0
    elif indice_atual >= len(resultados_busca):
        indice_atual = len(resultados_busca) - 1

    item_atual = resultados_busca[indice_atual]
    tabela.see(item_atual)  # Rolagem automática até o item
    tabela.selection_set(item_atual)  # Selecionar o item

# Função para permitir a edição direta da string (em inglês ou português)
def editar_string(event):
    item_selecionado = tabela.focus()  # Obter item selecionado
    coluna_selecionada = tabela.identify_column(event.x)  # Identificar coluna clicada

    if coluna_selecionada in ("#3", "#4"):  # Permitir edição apenas nas colunas 3 (Inglês) e 4 (Português)
        coluna_index = int(coluna_selecionada.strip("#")) - 1
        valor_atual = tabela.item(item_selecionado, "values")[coluna_index]

        # Janela de edição
        janela_edicao = tk.Toplevel(janela)
        janela_edicao.title("Editar String")
        janela_edicao.geometry("500x200")  # Largura fixa e altura suficiente para exibir o botão

        # Frame principal para conter o campo de texto e a barra de rolagem
        frame_texto = tk.Frame(janela_edicao)
        frame_texto.pack(fill="both", expand=True, padx=10, pady=10)

        # Barra de rolagem
        barra_rolagem = tk.Scrollbar(frame_texto)
        barra_rolagem.pack(side="right", fill="y")

        # Campo de texto com barra de rolagem
        text_area = tk.Text(frame_texto, font=("Arial", 12), wrap="word", yscrollcommand=barra_rolagem.set, height=5)
        text_area.insert("1.0", valor_atual)  # Inserir o valor atual na área de texto
        text_area.pack(fill="both", expand=True)
        barra_rolagem.config(command=text_area.yview)

        # Função para salvar a edição
        def salvar_edicao():
            nova_string = text_area.get("1.0", "end").strip().replace("\n", " ")  # Remover quebras de linha extras
            valores = list(tabela.item(item_selecionado, "values"))
            valores[coluna_index] = nova_string  # Atualizar a string na tabela
            tabela.item(item_selecionado, values=valores)
            janela_edicao.destroy()

        # Botão "Salvar" fixo abaixo do campo de texto
        btn_salvar = tk.Button(janela_edicao, text="Salvar", command=salvar_edicao, font=("Arial", 12))
        btn_salvar.pack(pady=5)

        # Fechar a janela ao pressionar "Enter"
        janela_edicao.bind("<Return>", lambda _: salvar_edicao())

        # Cancelar edição ao fechar a janela
        janela_edicao.protocol("WM_DELETE_WINDOW", janela_edicao.destroy)

# Criar a janela principal
janela = tk.Tk()
janela.title("Editor de Traduções")

# Contador de linhas
contador_linhas = tk.Label(janela, text="Linhas carregadas: 0", font=("Arial", 12))
contador_linhas.pack(pady=5)

# Campo de busca
frame_busca = tk.Frame(janela)
frame_busca.pack(pady=5)

entrada_busca = tk.Entry(frame_busca, font=("Arial", 12), width=40)
entrada_busca.pack(side="left", padx=5)

btn_buscar = tk.Button(frame_busca, text="Buscar", command=buscar_termo, font=("Arial", 11))
btn_buscar.pack(side="left", padx=5)

btn_anterior = tk.Button(frame_busca, text="Anterior", command=lambda: navegar_resultados(-1), font=("Arial", 11))
btn_anterior.pack(side="left", padx=5)

btn_proximo = tk.Button(frame_busca, text="Próximo", command=lambda: navegar_resultados(1), font=("Arial", 11))
btn_proximo.pack(side="left", padx=5)

# Criar a tabela
colunas = ("num", "chave", "ingles", "portugues")
tabela = ttk.Treeview(janela, columns=colunas, show="headings", height=20)
tabela.heading("num", text="#")
tabela.heading("chave", text="Chave")
tabela.heading("ingles", text="String em Inglês (Editável)")
tabela.heading("portugues", text="String em Português (Editável)")

tabela.column("num", width=50, anchor="center")
tabela.column("chave", width=150)
tabela.column("ingles", width=300)
tabela.column("portugues", width=300)

tabela.tag_configure("destaque", background="#ffff99")  # Cor de fundo para destaque

tabela.pack(fill="both", expand=True, padx=10, pady=5)
tabela.bind("<Double-1>", editar_string)  # Permitir edição ao dar duplo clique

# Separador visual
separador = ttk.Separator(janela, orient="horizontal")
separador.pack(fill="x", pady=5)

# Botões de abrir arquivos, iniciar nova tradução e salvar
frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=10)

btn_nova = tk.Button(frame_botoes, text="Nova Tradução", command=nova_traducao, font=("Arial", 11))
btn_nova.pack(side="left", padx=5)

btn_abrir = tk.Button(frame_botoes, text="Abrir Tradução", command=abrir_traducao, font=("Arial", 11))
btn_abrir.pack(side="left", padx=5)

btn_salvar = tk.Button(frame_botoes, text="Salvar Tradução", command=salvar_arquivo, font=("Arial", 11))
btn_salvar.pack(side="left", padx=5)

# Iniciar a interface
janela.mainloop()
