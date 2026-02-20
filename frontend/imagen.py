#Importamos la librerías
import tkinter as tk
#Llamamos a PIL para poner imagenes 
from PIL import Image, ImageTk

def boton_clic():
    print("Holaaa Richi")

def actualizar_etiqueta():
    nuevo_texto= entrada.get()
    cuatro.config(text=nuevo_texto)

#Definimos la ventana
ven1= tk.Tk()
#Le damos un título a la ventana
ven1.title("Pug Leo")
#Programamos dimensiones
ven1.geometry("600x500")

etiqueta= tk.Label(ven1,text="Holaaa soy el capi y ando en las canchas",
    font=("Times New Roman", 14, "bold"), fg="White", bg="#46BAF0", padx=20, pady=10)
etiqueta.pack() #.pack() te centra la etiqueta desde arriba y los va acomodando
#etiqueta.place(x=50, y=200) te ayuda a posicionar en coordenadas

uno= tk.Label(ven1, text="Mi nombre es Daniel Elihud",
    font=("Arial", 24, "bold"), fg="black", bg="yellow", padx=20, pady=10)
uno.pack()

dos= tk.Label(ven1, text="Estudio Ingenería en ciencias de la computación",
    font=("Consolas", 15, "bold"), fg="#C0C2EE", bg="#5146F0", padx=20, pady=10)
dos.pack()

tres= tk.Label(ven1, text="Me gusta las enchiladas",
    font=("Arial", 15, "bold"), fg="white", bg="#1505F0", padx=20, pady=10)
tres.pack()

#crear un boton 
boton = tk.Button(ven1, text="Dale click", command=boton_clic,
                  font=("Comic Sans", 18, "bold"), fg="white", bg="#0048F0")
boton.pack(pady=10)

#código de la imagen
pug= Image.open("pug.jpg")
pug= pug.resize((275, 200))
pug_tk= ImageTk.PhotoImage(pug)
label_pug= tk.Label(ven1, image=pug_tk)
label_pug.pack(pady=15)

#etiqueta dinamica con actualizacion de texto y colocacion
entrada= tk.Entry(ven1, width=60)
entrada.pack(padx=10)

boton1 = tk.Button(ven1, text="Actualizar", command=actualizar_etiqueta)
boton1.pack()

cuatro= tk.Label(ven1, text="Texto inicial", font=("Arial", 12))
cuatro.pack(pady=10)

#Iniciar el bucle principal de la aplicación
ven1.mainloop()

