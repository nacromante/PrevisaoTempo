from tkinter import *
from tkinter import ttk
from previsao import PrevisaoTempo
# Cria formulario
formulario = Tk()

#A linha abaixo define o tamanho do frame
formulario.geometry("630x850")

#A linha abaixo nao permite modificar o tamanho do frame
formulario.resizable(width=True, height=True)

#Aplica um imagem de fundo 
fundo = PhotoImage(file="fundo.png")
lblfundo=Label(formulario,image=fundo).place(x=0,y=0)

formulario.title = "Previsão do tempo"
# Cria itens
itens = {
            "Rio Branco-AC":     240,
            "Maceió-AL":         233,
            "Macapá-AP":         232,
            "Manaus-AM":         234,
            "Salvador-BA":       242,
            "Fortaleza-CE":      229,
            "Brasília-DF":       224,
            "Vitória-ES":        246,
            "Goiânia-GO":        230,
            "São luís-MA":       243,
            "Cuiabá-MT":         226,
            "Campo Grande-MS":   225,
            "Belo Horizonte-MG": 222,
            "Belém-PA":          221,
            "João Pessoa-PB":    231,
            "Curitiba-PR":	 227,
            "Recife-PI":         239,
            "Teresina-PI":       245,
            "Rio de Janeiro-RJ": 241,
            "Natal-RN":          235,
            "Porto Alegre-RS":   237,
            "Porto Velho-RO":    238,
            "Boa Vista-RR":      223,
            "Florianópolis-SC":  228,
            "São Paulo-SP":      244,
            "Aracaju-SE":        220,
            "Palmas-TO":         236
        }

 
# Evento ocorre quando muda a seleção do combo
def evento(*args):
    
    codCid=itens[combo.get()]
    prevCid=PrevisaoTempo(codCid)
    prevs=prevCid.pesquisar()
    
    Label(formulario, relief=RIDGE, width=25, anchor=N, bg="#1E90FF", font=('Arial','12','bold'), fg='#ffffff', text="Previsão para " + combo.get()).grid()
    
    lblDia = Label(formulario, relief=RIDGE, width=30, anchor=W, bg="#B0C4DE", font=('Arial','12','bold'), text="Dia: " + prevs["dia"]).grid(column=1)
    lblTempo = Label(formulario, relief=RIDGE, width=30, anchor=W, bg="#E0FFFF", fg='#4682B4', font=('Arial','12','bold'), text="Tempo: " + prevCid.situacao(prevs["tempo"])).grid(column=1)
    lblMax = Label(formulario, relief=RIDGE, width=30, anchor=W, bg="#E0FFFF", fg='#4682B4', font=('Arial','12','bold'), text="Máxima: " + prevs["maxima"]).grid(column=1)
    lblMin = Label(formulario, relief=RIDGE, width=30, anchor=W, bg="#E0FFFF", fg='#4682B4', font=('Arial','12','bold'), text="Mínima: " + prevs["minima"]).grid(column=1)
    lblIuv = Label(formulario, relief=RIDGE, width=30, anchor=W, bg="#E0FFFF", fg='#4682B4', font=('Arial','12','bold'), text="Iuv: " + prevs["iuv"]).grid(column=1) 

    
    
# Cria Labels
titCombo=Label(formulario, text="Selecione a Cidade Desejada", relief=RIDGE, width=25, height=1, anchor=N, bg="#FFFFFF", font=('Arial','14','bold'))
 
# Cria um ComboBox - e adicona prorpriedades e eventos
combo=ttk.Combobox(formulario, width=20, height=20, font=('Arial','14','bold'))
combo["values"]=list(itens.keys())
combo.current(0)
combo.bind("<<ComboboxSelected>>", evento)
 
# Posiciona componentes na tela
#titulo.grid(row=1)
titCombo.grid(row=5, pady=60)
combo.grid(row=5, column=1, pady=70)
 
# Roda o loop principal do tcl
mainloop()
