## Nome: Lucas Nascimento da Silva

from tkinter import * ## Importar o Tkinter

class Calculadora: ## Criar a classe "Calculadora"
    def __init__(self,master): ## Container pai
        self.frame = Frame(master) ## Primeiro widget
        self.frame.grid() ## Tipo de posicionamento
        self.operações = Entry(master,width=34) ## Widget de entrada, onde aparecerão as operações feitas na calculadora
        self.operações.grid(row=1,column=0) ## Posicionamente do widget de entrada
        bts = ["0","1","2","3","4","5","6","7","8","9","+","-","*","/","=","C"] ## Botões que aparecerão na calculadora
        r = 1 ## Variável da posição da linha dos botões
        c = 0 ## Variável da posição da coluna dos botões
        for bt in bts:
            self.button = Button(self.frame, text=bt, width=6) ## Widget para adicionar os botões
            self.button.grid(row=r, column=c) ## Posicionamento dos botões
            c+=1
            if c>3: ## Define a largura da calculadora
                c=0
                r+=1

root = Tk() ## Permite que os widgets sejam usados na aplicação
root.title("Calculadora") ## Dá um título para a janela
Calculadora(root) ## Torna a variável root como parâmetro para construir a classe Calculadora
root.mainloop() ## Faz com que a tela seja exibida