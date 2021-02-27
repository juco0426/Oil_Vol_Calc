#Programa para el cálculo de volúmen de carga de hidrocarburos en Tractocamiones usando Interfaz gráfica 

import tkinter as tk
from tkinter import ttk

#Se define operación de cálculo para obtener el volumen de cargue
def operacion():
     if combo1.get()=='2':
        dens = 141.5 / (131.5 + grav_api.get()) * 999.016
        resultado = (48000 - (peso_cabezote.get() + peso_trailer.get())) / dens * 6.28981
        resultado = round(resultado, 2)
        if resultado > vol_trailer.get()/42:
            resultado = round(0.98*vol_trailer.get()/42, 2)
        reslb = tk.Label(root, text=resultado, relief='flat',state='normal').grid(row = 104, column = 4)
     else:
         dens = 141.5 / (131.5 + grav_api.get()) * 999.016
         resultado = (52000 - (peso_cabezote.get() + peso_trailer.get())) / dens * 6.28981
         resultado = round(resultado, 2)
         if resultado > vol_trailer.get()/42:
            resultado = round(0.98*vol_trailer.get()/42, 2)
         reslb = tk.Label(root, text=resultado, relief='flat',state='normal').grid(row = 104, column = 4)    
  
#Definición de variables
root=tk.Tk()
combo1=tk.StringVar()
bot1=tk.StringVar()
dens=tk.DoubleVar()
placa=tk.StringVar()
placa_trailer =tk.StringVar()
peso_cabezote=tk.DoubleVar()
peso_trailer=tk.DoubleVar()
vol_trailer=tk.DoubleVar()
grav_api=tk.DoubleVar()
resultado=tk.DoubleVar()

#Configuración de la ventana de aplicación
root.title("Cálculo de Volumen de Cargue de Tractocamiones")
root.geometry("700x500")
root.configure(background="#006")
root.iconbitmap("cálculo_CTK.ico")


#Creación y disposición de los widgets
lb1=tk.Label(root, text = "PLACA CABEZOTE ", background="#006", fg="#FFF", anchor='e').grid(row = 14, column = 2)
box1 = tk.Entry(root, textvariable=placa)
box1.grid(row = 14, column = 4)

lb2=tk.Label(root, text = "PESO CABEZOTE, Kg   ", background="#006", fg="#FFF", anchor='e').grid(row = 24, column = 2)
box2 = tk.Entry(root, textvariable=peso_cabezote).grid(row = 24, column = 4)

lb3=tk.Label(root, text = "PLACA TRAILER   ", background="#006", fg="#FFF", anchor='e').grid(row = 34, column = 2)
box3 = tk.Entry(root).grid(row = 34, column = 4)

lb4=tk.Label(root, text = "PESO TRAILER, kg   ", background="#006", fg="#FFF", anchor='e').grid(row = 44, column = 2)
box4 = tk.Entry(root, textvariable=peso_trailer).grid(row = 44, column = 4)

lb5=tk.Label(root, text = "GRAVEDAD API@60F ", background="#006", fg="#FFF", anchor='e').grid(row = 54, column = 2)
box5 = tk.Entry(root, textvariable=grav_api ).grid(row = 54, column = 4)

lb6=tk.Label(root, text = "CAPACIDAD DEL TRAILER, GAL ", background="#006", fg="#FFF", anchor='e').grid(row = 64, column = 2)
box6 = tk.Entry(root, textvariable=vol_trailer ).grid(row = 64, column = 4)

#Lista desplegable para seleccionar el número de ejes
combo1=ttk.Combobox(root)
combo1.grid(row = 84, column = 4)
combo1['values'] = ('2', '3')

lb7=tk.Label(root, text = "# EJES DEL TRAILER", background="#006", fg="#FFF", anchor='e').grid(row = 84, column = 2)

bot2= tk.Button(root, text = "Calcular", command = operacion).grid (row = 104, column = 2)

lb6=tk.Label(root, text = "Resultado ", background="#006", fg="#FFF").grid(row = 104, column = 3)



root.mainloop()
        
        
