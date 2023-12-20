from tkinter import*
from tkinter.messagebox import*
from PIL import ImageTk, Image
from tkinter import filedialog
import webbrowser
import os

root = Tk()
root.minsize(650,650)
root.maxsize(850,850)

abrir_img = ImageTk.PhotoImage(Image.open("abrir.png"))
cerrar_img = ImageTk.PhotoImage(Image.open("guardar.png"))
render_img = ImageTk.PhotoImage(Image.open("render.jpg"))

nombre_de_archivo = Label(root, text="nombre del archivo")
nombre_de_archivo.place(relx=0.28, rely=0.03, anchor=CENTER)

campo_archivo = Entry(root)
campo_archivo.place(relx=0.46, rely=0.03, anchor=CENTER)

area_de_texto = Text(root, height=35, width=80)
area_de_texto.place(relx=0.5, rely=0.55, anchor=CENTER)

name = ""

def abrir_archivo ():
    global name
    area_de_texto.delete(1.0, END)
    html_archivo = filedialog.askopenfilename(title="Abrir archivo html", filetypes=(("archivos html", "*.html"),))
    name = os.path.basename(html_archivo)
    formato_archivo = name.split(".")[0]
    campo_archivo.insert(END, formato_archivo)
    root.title(formato_archivo)
    html_archivo = open(name, "r")
    texto = html_archivo.read()
    area_de_texto(END, texto)
    html_archivo.close()
    
def guardar_archivo ():
    nombre_campo = campo_archivo.get
    archivo_permiso = open(nombre_campo + "html", "w")
    texto_escrito = are_de_texto.get(1.0, END)
    archivo_permiso.write(texto_escrito)
    campo_archivo.delete(0, END)
    area_de_texto.delete(1.0, END)
    showinfo("actualizar", "¡¡¡exito!!!")

def correr ():
    global name
    webbrowser.open(name)

boton_abrir = Button(root, image=abrir_img, command=abrir_archivo)
boton_abrir.place(relx=0.05, rely=0.03, anchor=CENTER)

boton_guardar = Button(root, image=cerrar_img, command=guardar_archivo)
boton_guardar.place(relx=0.11, rely=0.03, anchor=CENTER)

boton_render = Button(root, image=render_img, command=correr)
boton_render.place(relx=0.17, rely=0.03, anchor=CENTER)

root.mainloop()



