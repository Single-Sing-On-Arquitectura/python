import tkinter as tk 
from tkinter import messagebox
import requests

class lol(tk.Frame):


    def __init__(self, root = None):
        super().__init__(root, width=489, height=350)
        self.root = root
        self.pack()
        self.config(bg='lightblue')
        self.campos()

    def campos(self):

        self.title_login = tk.Label(self, text = 'Bienvenido',font =('Arial',24) )
        self.title_login.grid(row=0, column = 0, padx =10, pady=10, columnspan=2)


        self.label_user = tk.Label(self, text = 'User:')
        self.label_user.config(font =('Arial',12,'bold'))
        self.label_user.grid(row=1, column = 0, padx =10, pady=10)

        self.entry_user = tk.Entry(self)
        self.entry_user.grid(row=1, column = 1, padx =10, pady=10)

        self.label_pass = tk.Label(self, text = 'Password:')
        self.label_pass.config(font =('Arial',12,'bold'))
        self.label_pass.grid(row=2, column = 0, padx =10, pady=10)

        self.entry_pass = tk.Entry(self, show ='*')
        self.entry_pass.grid(row=2, column = 1, padx =10, pady=10)

        self.button_login = tk.Button(self, text = 'Iniciar sesión', command=Frame.login)
        self.button_login.config(font =('Arial',12,'bold'))
        self.button_login.grid(row=3, column = 0, padx =10, pady=10)

        self.button_register = tk.Button(self, text = 'Registrar', command=Frame.register)
        self.button_register.config(font =('Arial',12,'bold'))
        self.button_register.grid(row=3, column = 1, padx =10, pady=10)

    def login():
        payload = {'user': 'andrey', 'password': '123', 'app': 1}
        response = requests.post('https://ssoufps.herokuapp.com/login', json=payload)
         
       
    def register():
        ventana_secundaria = tk.Toplevel()
        ventana_secundaria.title("Ventana secundaria")
        ventana_secundaria.config(width=300, height=200)
        
        title_register = tk.Label(ventana_secundaria, text = 'Registrese',font =('Arial',24) )
        title_register.grid(row=0, column = 0, padx =10, pady=10, columnspan=2)


        label_user_register = tk.Label(ventana_secundaria, text = 'User:')
        label_user_register.config(font =('Arial',12,'bold'))
        label_user_register.grid(row=1, column = 0, padx =10, pady=10)

        entry_user_register = tk.Entry(ventana_secundaria)
        entry_user_register.grid(row=1, column = 1, padx =10, pady=10)

        label_pass_register = tk.Label(ventana_secundaria, text = 'Password:')
        label_pass_register.config(font =('Arial',12,'bold'))
        label_pass_register.grid(row=2, column = 0, padx =10, pady=10)

        entry_pass_register = tk.Entry(ventana_secundaria, show ='*')
        entry_pass_register.grid(row=2, column = 1, padx =10, pady=10)

        label_name_register = tk.Label(ventana_secundaria, text = 'Name:')
        label_name_register.config(font =('Arial',12,'bold'))
        label_name_register.grid(row=3, column = 0, padx =10, pady=10)

        entry_name_register = tk.Entry(ventana_secundaria)
        entry_name_register.grid(row=3, column = 1, padx =10, pady=10)
        
        button_login = tk.Button(ventana_secundaria, text = 'Registrarse', command=Frame.register2)
        button_login.config(font =('Arial',12,'bold'))
        button_login.grid(row=4, column = 0, padx =10, pady=10)
     

    
        # Crear un botón dentro de la ventana secundaria
        # para cerrar la misma.
        button_cerrar = tk.Button(ventana_secundaria,text="Cerrar ventana", command=ventana_secundaria.destroy)
        button_cerrar.config(font =('Arial',12,'bold'))
        button_cerrar.grid(row=4, column = 1, padx =10, pady=10)

    def register2():
       
        payload = {'user': user_register.get(), 'password': pass_register.get(), 'name': name_register.get()}
        response = requests.post('https://ssoufps.herokuapp.com/register', json=payload)
     
        if response.status_code == 200:
          messagebox.showinfo("Éxito", response.json()['mensaje'])  
        else:
           messagebox.showerror("Error", response.json()['mensaje'])





