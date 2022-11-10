import tkinter as tk
from tkinter import messagebox
import requests

root = tk.Tk()

user_login = tk.StringVar()
pass_login = tk.StringVar()

user_register = tk.StringVar()
pass_register = tk.StringVar()
name_register = tk.StringVar()

def main():
    root.title('Aplicación SSO')

    app = tk.Frame(root, width=489, height=350, bg='lightblue')
    app.pack()

    title_login = tk.Label(app, text = 'Bienvenido',font =('Arial',24) )
    title_login.grid(row=0, column = 0, padx =10, pady=10, columnspan=2)


    label_user = tk.Label(app, text = 'User:')
    label_user.config(font =('Arial',12,'bold'))
    label_user.grid(row=1, column = 0, padx =10, pady=10)

    entry_user = tk.Entry(app, textvariable=user_login)
    entry_user.grid(row=1, column = 1, padx =10, pady=10)

    label_pass = tk.Label(app, text = 'Password:')
    label_pass.config(font =('Arial',12,'bold'))
    label_pass.grid(row=2, column = 0, padx =10, pady=10)

    entry_pass = tk.Entry(app, show ='*', textvariable=pass_login)
    entry_pass.grid(row=2, column = 1, padx =10, pady=10)

    button_login = tk.Button(app, text = 'Iniciar sesión', command = login)
    button_login.config(font =('Arial',12,'bold'))
    button_login.grid(row=3, column = 0, padx =10, pady=10)

    button_register = tk.Button(app, text = 'Registrar', command = register)
    button_register.config(font =('Arial',12,'bold'))
    button_register.grid(row=3, column = 1, padx =10, pady=10)

    app.mainloop()

def login():
        payload = {'user': user_login.get(), 'password': pass_login.get(), 'app':1}
        response = requests.post('https://ssoufps.herokuapp.com/login', json=payload)

        if response.status_code == 200:
          token = response.json()['token']
          
          # falta agregar funcionalidad despues de que inicia sesión
          #
          #
        
        else:
          if response.json()['mensaje'] == 'Ya existe una sesión activa, debe cerrar sesión en el otro dispositivo':
            if messagebox.askyesno(message= response.json()['mensaje'] + "¿Desea cerrarla?", title="Sesión Activa"):
              cerrarSesiones()
          else:
            messagebox.showerror("Error", response.json()['mensaje'])

           
def cerrarSesiones():
  payload = {'user': user_login.get(), 'password': pass_login.get()}
  response = requests.post('https://ssoufps.herokuapp.com/signoffall', json=payload)
  if response.status_code == 200:
    messagebox.showinfo("Éxito", response.json()['mensaje'])  
  else:
    messagebox.showerror("Error", response.json()['mensaje'])

         
def register():
        ventana_secundaria = tk.Toplevel()
        ventana_secundaria.title("Ventana secundaria")
        ventana_secundaria.config(width=300, height=200)
        
        title_register = tk.Label(ventana_secundaria, text = 'Registrese',font =('Arial',24) )
        title_register.grid(row=0, column = 0, padx =10, pady=10, columnspan=2)


        label_user_register = tk.Label(ventana_secundaria, text = 'User:')
        label_user_register.config(font =('Arial',12,'bold'))
        label_user_register.grid(row=1, column = 0, padx =10, pady=10)

        entry_user_register = tk.Entry(ventana_secundaria, textvariable=user_register)
        entry_user_register.grid(row=1, column = 1, padx =10, pady=10)

        label_pass_register = tk.Label(ventana_secundaria, text = 'Password:')
        label_pass_register.config(font =('Arial',12,'bold'))
        label_pass_register.grid(row=2, column = 0, padx =10, pady=10)

        entry_pass_register = tk.Entry(ventana_secundaria, show ='*', textvariable=pass_register)
        entry_pass_register.grid(row=2, column = 1, padx =10, pady=10)

        label_name_register = tk.Label(ventana_secundaria, text = 'Name:')
        label_name_register.config(font =('Arial',12,'bold'))
        label_name_register.grid(row=3, column = 0, padx =10, pady=10)

        entry_name_register = tk.Entry(ventana_secundaria, textvariable=name_register)
        entry_name_register.grid(row=3, column = 1, padx =10, pady=10)
        
        button_login = tk.Button(ventana_secundaria, text = 'Registrarse', command=register2)
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

if __name__ == '__main__':
   main()