from tkinter import *

# Aqui é a janela
janela = Tk()

# Colocando o título da janela
janela.title("Calculadora")

def enviarNumeroPara(char):

    global calculoOperacoes

    calculoOperacoes += str(char)
    textoDeEntrada.set(calculoOperacoes)

def deletarNumero():

    global calculoOperacoes

    textoSemOUltimoDigito = calculoOperacoes[:-1]
    calculoOperacoes = textoSemOUltimoDigito
    textoDeEntrada.set(calculoOperacoes)

def limparTudo():

    global calculoOperacoes
    
    calculoOperacoes = ""
    textoDeEntrada.set(calculoOperacoes)

def funcaoIgual():

    global calculoOperacoes

    resultadoCalculo = str(eval(calculoOperacoes))
    textoDeEntrada.set(resultadoCalculo)
    calculoOperacoes = resultadoCalculo

calculoOperacoes = ""
textoDeEntrada = StringVar()

#Caixa de texto que irá aparecer as operações e resultados
textoExibeOperacoesResultado = Entry(janela, font=("Arial 20 bold"),
                                     textvariable=textoDeEntrada, #Variável
                                     border=5, #Borda
                                     background="#BBB", #Cor do fundo
                                     foreground="black" #Cor da letra
                                     ).grid(row=1, columnspan=5, padx=10, pady=15)

# Botão número 7
botaoNumero7 = Button(janela, 
                      text=7, #Texto que aparece no botão
                      border=5, #Borda
                      foreground="black", #Cor da letra
                      background="#BBB", #Cor do fundo
                      font=("Arial 20 bold"), #Fonte, tamanho e estilo do texto
                      command=lambda:enviarNumeroPara("7")).grid(row=2, column=0, sticky="NSEW")

# Botão número 8
botaoNumero8 = Button(janela, 
                      text=8, #Texto que aparece no botão
                      border=5, #Borda
                      foreground="black", #Cor da letra
                      background="#BBB", #Cor do fundo
                      font=("Arial 20 bold"), #Fonte, tamanho e estilo do texto
                      command=lambda:enviarNumeroPara("8")).grid(row=2, column=1, sticky="NSEW")

# Botão número 9
botaoNumero9 = Button(janela, 
                      text=9, #Texto que aparece no botão
                      border=5, #Borda
                      foreground="black", #Cor da letra
                      background="#BBB", #Cor do fundo
                      font=("Arial 20 bold"), #Fonte, tamanho e estilo do texto
                      command=lambda:enviarNumeroPara("9")).grid(row=2, column=2, sticky="NSEW")

# Botão Deletar
botaoDeletar = Button(janela, 
                      text="DEL", #Texto que aparece no botão
                      border=5, #Borda
                      foreground="#000", #Cor da letra
                      background="#DC143C", #Cor do fundo
                      font=("Arial 20 bold"), #Fonte, tamanho e estilo do texto
                      command=deletarNumero).grid(row=2, column=3, sticky="NSEW")

# Botão Deletar Tudo
botaoDeletarTudo = Button(janela, 
                      text="AC", #Texto que aparece no botão
                      border=5, #Borda
                      foreground="#000", #Cor da letra
                      background="#DC143C", #Cor do fundo
                      font=("Arial 20 bold"), #Fonte, tamanho e estilo do texto
                      command=limparTudo).grid(row=2, column=4, sticky="NSEW")

# Botão número 4
botaoNumero4 = Button(janela, 
                      text=4, #Texto que aparece no botão
                      border=5, #Borda
                      foreground="black", #Cor da letra
                      background="#BBB", #Cor do fundo
                      font=("Arial 20 bold"), #Fonte, tamanho e estilo do texto
                      command=lambda:enviarNumeroPara("4")).grid(row=3, column=0, sticky="NSEW")

# Botão número 5
botaoNumero5 = Button(janela, 
                      text=5, #Texto que aparece no botão
                      border=5, #Borda
                      foreground="black", #Cor da letra
                      background="#BBB", #Cor do fundo
                      font=("Arial 20 bold"), #Fonte, tamanho e estilo do texto
                      command=lambda:enviarNumeroPara("5")).grid(row=3, column=1, sticky="NSEW")

# Botão número 6
botaoNumero6 = Button(janela, 
                      text=6, #Texto que aparece no botão
                      border=5, #Borda
                      foreground="black", #Cor da letra
                      background="#BBB", #Cor do fundo
                      font=("Arial 20 bold"), #Fonte, tamanho e estilo do texto
                      command=lambda:enviarNumeroPara("6")).grid(row=3, column=2, sticky="NSEW")

# Botão de Multiplicação
botaoMultiplicacao = Button(janela, 
                      text="*", #Texto que aparece no botão
                      border=5, #Borda
                      foreground="black", #Cor da letra
                      background="#BBB", #Cor do fundo
                      font=("Arial 20 bold"), #Fonte, tamanho e estilo do texto
                      command=lambda:enviarNumeroPara("*")).grid(row=3, column=3, sticky="NSEW")

# Botão de Divisão
botaoDivisao = Button(janela, 
                      text="/", #Texto que aparece no botão
                      border=5, #Borda
                      foreground="black", #Cor da letra
                      background="#BBB", #Cor do fundo
                      font=("Arial 20 bold"), #Fonte, tamanho e estilo do texto
                      command=lambda:enviarNumeroPara("/")).grid(row=3, column=4, sticky="NSEW")

# Botão número 1
botaoNumero1 = Button(janela, 
                      text=1, #Texto que aparece no botão
                      border=5, #Borda
                      foreground="black", #Cor da letra
                      background="#BBB", #Cor do fundo
                      font=("Arial 20 bold"), #Fonte, tamanho e estilo do texto
                      command=lambda:enviarNumeroPara("1")).grid(row=4, column=0, sticky="NSEW")

# Botão número 2
botaoNumero2 = Button(janela, 
                      text=2, #Texto que aparece no botão
                      border=5, #Borda
                      foreground="black", #Cor da letra
                      background="#BBB", #Cor do fundo
                      font=("Arial 20 bold"), #Fonte, tamanho e estilo do texto
                      command=lambda:enviarNumeroPara("2")).grid(row=4, column=1, sticky="NSEW")

# Botão número 3
botaoNumero3 = Button(janela, 
                      text=3, #Texto que aparece no botão
                      border=5, #Borda
                      foreground="black", #Cor da letra
                      background="#BBB", #Cor do fundo
                      font=("Arial 20 bold"), #Fonte, tamanho e estilo do texto
                      command=lambda:enviarNumeroPara("3")).grid(row=4, column=2, sticky="NSEW")

# Botão de Adição
botaoAdicao = Button(janela, 
                      text="+", #Texto que aparece no botão
                      border=5, #Borda
                      foreground="black", #Cor da letra
                      background="#BBB", #Cor do fundo
                      font=("Arial 20 bold"), #Fonte, tamanho e estilo do texto
                      command=lambda:enviarNumeroPara("+")).grid(row=4, column=3, sticky="NSEW")

# Botão de Subtração
botaoSubtracao = Button(janela, 
                      text="-", #Texto que aparece no botão
                      border=5, #Borda
                      foreground="black", #Cor da letra
                      background="#BBB", #Cor do fundo
                      font=("Arial 20 bold"), #Fonte, tamanho e estilo do texto
                      command=lambda:enviarNumeroPara("-")).grid(row=4, column=4, sticky="NSEW")

# Botão número 0
botaoNumero0 = Button(janela, 
                      text=0, #Texto que aparece no botão
                      border=5, #Borda
                      foreground="black", #Cor da letra
                      background="#BBB", #Cor do fundo
                      font=("Arial 20 bold"), #Fonte, tamanho e estilo do texto
                      command=lambda:enviarNumeroPara("0")).grid(row=5, column=0, sticky="NSEW")

# Botão ponto(para decimais)
botaoPonto = Button(janela, 
                      text=".", #Texto que aparece no botão
                      border=5, #Borda
                      foreground="black", #Cor da letra
                      background="#BBB", #Cor do fundo
                      font=("Arial 20 bold"), #Fonte, tamanho e estilo do texto
                      command=lambda:enviarNumeroPara(".")).grid(row=5, column=1, sticky="NSEW")

# Botão de Igualdade
botaoIgual = Button(janela, 
                      text="=", #Texto que aparece no botão
                      border=5, #Borda
                      foreground="black", #Cor da letra
                      background="#BBB", #Cor do fundo
                      font=("Arial 20 bold"), #Fonte, tamanho e estilo do texto
                      command=funcaoIgual).grid(row=5, column=2, columnspan=3, sticky="NSEW")

# Executando a janela em um loop para ela aparecer infinitamente
janela.mainloop()