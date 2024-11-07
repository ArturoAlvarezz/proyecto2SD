import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import requests

# Datos de usuario simulados (puedes conectar esto a una base de datos)
USUARIOS = {"usuario": "1234"}

data = [
	{
        "usuario": "fringilla",
        "tipo": "medico"
    },
    {
        "usuario": "cras",
        "tipo": "admision"
    },
    {
        "usuario": "facilisis",
        "tipo": "pabellon"
    },
    {
        "usuario": "mus",
        "tipo": "examenes"
    },
    {
        "usuario": "sociosqu",
        "tipo": "pabellon"
    }
]



# Función para verificar las credenciales
def verificar_credenciales(entry_email, entry_password, ventana_usuario, frame_login):
    correo = entry_email.get()
    password = entry_password.get()

    if correo in USUARIOS and USUARIOS[correo] == password:
        mostrar_chats(ventana_usuario, frame_login)  # Si las credenciales son correctas, mostrar los chats
    else:
        messagebox.showerror("Error", "Credenciales incorrectas")  # Si son incorrectas, mostrar error

def enviar_mensaje(chat, entry_mensaje):
    mensaje = entry_mensaje.get()
    chat.insert('end', f"Yo: {mensaje}\n")
    entry_mensaje.delete(0, 'end')


def iniciar_administrador():
    ventana_admin = tk.Toplevel(root)
    ventana_admin.title("Opciones de administrador")
    ventana_admin.geometry("350x500")

    label_titulo = tk.Label(ventana_admin, text="Creación de usuario", font=('Arial', 14))
    label_titulo.pack(pady=10)

    label_nombre = tk.Label(ventana_admin, text="Nombre")
    label_nombre.pack(pady=5)
    entry_nombre = tk.Entry(ventana_admin)
    entry_nombre.pack(pady=5)

    label_tipo_usuario = tk.Label(ventana_admin, text="Tipo de usuario")
    label_tipo_usuario.pack(pady=5)

    tipo_usuario = ttk.Combobox(ventana_admin, values=["Medico", "Administrativo"])
    tipo_usuario.pack(pady=5)

    label_tipo_usuario_admin = tk.Label(ventana_admin, text="Tipo de usuario administrativo")
    tipo_usuario_admin = ttk.Combobox(ventana_admin, values=["Admisión", "Pabellón", "Exámenes", "Auxiliar"])

    def mostrar_opciones_administrativas(event):
        if tipo_usuario.get() == "Administrativo":
            label_tipo_usuario_admin.pack(pady=5)
            tipo_usuario_admin.pack(pady=5)
        else:
            label_tipo_usuario_admin.pack_forget()
            tipo_usuario_admin.pack_forget()

    tipo_usuario.bind("<<ComboboxSelected>>", mostrar_opciones_administrativas)

    def crear_usuario():
        url = "http://127.0.0.1:8000/crear-usuario/"
        nombre = entry_nombre.get()
        tipo = tipo_usuario.get()
        tipo_admin = tipo_usuario_admin.get() if tipo_usuario.get() == "Administrativo" else None

        data = {
            "nombre": nombre,
            "tipo": tipo,
            "tipo_admin": tipo_admin
        }

        print(data)
        response = requests.post(url, json=data)


    btn_crear_usuario = tk.Button(ventana_admin, text="Crear usuario", command=crear_usuario)
    btn_crear_usuario.pack(side="bottom", pady=10)

    ventana_admin.mainloop()

def iniciar_usuario():
    ventana_usuario = tk.Toplevel(root)
    ventana_usuario.title("Opciones de usuario")
    ventana_usuario.geometry("350x500")

    frame_login = tk.Frame(ventana_usuario)
    frame_login.pack(pady=50)

    label_login = tk.Label(frame_login, text="Login", font=('Arial', 14))
    label_login.pack(pady=10)

    # Campos para Login
    label_email = tk.Label(frame_login, text="Correo")
    label_email.pack(pady=5)
    entry_email = tk.Entry(frame_login)
    entry_email.pack(pady=5)

    label_password = tk.Label(frame_login, text="Password")
    label_password.pack(pady=5)
    entry_password = tk.Entry(frame_login, show='*')
    entry_password.pack(pady=5)

    # Botón de Ingresar
    btn_login = tk.Button(frame_login, text="Ingresar", command=lambda: verificar_credenciales(entry_email, entry_password, ventana_usuario, frame_login))
    btn_login.pack(pady=10)

    ventana_usuario.mainloop()

def mostrar_chats(ventana_usuario, frame_login):

    frame_login.pack_forget()

    # Crear un frame superior para el encabezado y el botón
    header_frame = tk.Frame(ventana_usuario, bg='lightblue')
    header_frame.pack(fill='x')

    # Etiqueta "Mis chats"
    label_chats = tk.Label(header_frame, text="Mis chats", bg='lightblue', font=('Arial', 14))
    label_chats.pack(side='left', padx=70)

    # Botón para ir a la vista de usuarios
    btn_usuarios = tk.Button(header_frame, text="Usuarios", command=lambda: mostrar_usuarios(ventana_usuario, frame_chats, header_frame, btn_usuarios, label_chats))
    btn_usuarios.pack(side='right', padx=10)

    frame_chats = tk.Frame(ventana_usuario)
    frame_chats.pack(fill='both', expand=True)

    # Crear los chats
    chats = [("Miguel", "❤️"), ("Teresita", "🌙")]
    for nombre, emoji in chats:
        chat_label = tk.Label(frame_chats, text=f"{emoji} {nombre}", bg='white', font=('Arial', 12), anchor="w", padx=10)
        chat_label.pack(fill='x', pady=5)

def mostrar_usuarios(ventana_usuario, frame_chats, frame_header, btn_usuarios, label_chats):

    frame_chats.pack_forget()
    btn_usuarios.pack_forget()
    label_chats.pack_forget()
    
    # Encabezado "Usuarios"
    label_usuarios = tk.Label(frame_header, text="Usuarios", bg='lightblue', font=('Arial', 14))
    label_usuarios.pack(side='left', padx=70)

    # botón para regresar a los chats
    btn_regresar_chats = tk.Button(frame_header, text="Chats", command=lambda: [mostrar_chats(ventana_usuario, frame_usuarios), label_usuarios.pack_forget(), btn_regresar_chats.pack_forget(), frame_header.pack_forget()])
    btn_regresar_chats.pack(side='right', padx=10)

    frame_usuarios = tk.Frame(ventana_usuario)
    frame_usuarios.pack(fill='both', expand=True)

    frame_medicos = tk.Frame(frame_usuarios)
    frame_medicos.pack(fill='both', expand=True)

    label_titulo_medicos = tk.Label(frame_medicos, text="Médicos", bg='salmon1', font=('Arial', 14))
    label_titulo_medicos.pack(fill='x', pady=5)
    
    frame_admision = tk.Frame(frame_usuarios)
    frame_admision.pack(fill='both', expand=True)

    label_titulo_admision = tk.Label(frame_admision, text="Admisión", bg='salmon1', font=('Arial', 14))
    label_titulo_admision.pack(fill='x', pady=5)

    frame_pabellon = tk.Frame(frame_usuarios)
    frame_pabellon.pack(fill='both', expand=True)

    label_titulo_pabellon = tk.Label(frame_pabellon, text="Pabellón", bg='salmon1', font=('Arial', 14))
    label_titulo_pabellon.pack(fill='x', pady=5)

    frame_examenes = tk.Frame(frame_usuarios)
    frame_examenes.pack(fill='both', expand=True)

    label_titulo_examenes = tk.Label(frame_examenes, text="Exámenes", bg='salmon1', font=('Arial', 14))
    label_titulo_examenes.pack(fill='x', pady=5)

    frame_auxiliar = tk.Frame(frame_usuarios)
    frame_auxiliar.pack(fill='both', expand=True)

    label_titulo_auxiliar = tk.Label(frame_auxiliar, text="Auxiliar", bg='salmon1', font=('Arial', 14))
    label_titulo_auxiliar.pack(fill='x', pady=5)

    for usuario in data:
        if usuario["tipo"] == "medico":
            medico_label = tk.Button(frame_medicos, text=usuario["usuario"], bg='white', font=('Arial', 12), anchor="w", padx=10, command=lambda: sala_de_chat(ventana_usuario, frame_header, label_usuarios, frame_usuarios, btn_regresar_chats))
            medico_label.pack(fill='x', pady=5)
        elif usuario["tipo"] == "auxiliar":
            auxiliar_label = tk.Button(frame_auxiliar, text=usuario["usuario"], bg='white', font=('Arial', 12), anchor="w", padx=10, command=lambda: sala_de_chat(ventana_usuario, frame_header, label_usuarios, frame_usuarios, btn_regresar_chats))
            auxiliar_label.pack(fill='x', pady=5)
        elif usuario["tipo"] == "admision":
            admision_label = tk.Button(frame_admision, text=usuario["usuario"], bg='white', font=('Arial', 12), anchor="w", padx=10, command=lambda: sala_de_chat(ventana_usuario, frame_header, label_usuarios, frame_usuarios, btn_regresar_chats))
            admision_label.pack(fill='x', pady=5)
        elif usuario["tipo"] == "pabellon":
            pabellon_label = tk.Button(frame_pabellon, text=usuario["usuario"], bg='white', font=('Arial', 12), anchor="w", padx=10, command=lambda: sala_de_chat(ventana_usuario, frame_header, label_usuarios, frame_usuarios, btn_regresar_chats))
            pabellon_label.pack(fill='x', pady=5)
        elif usuario["tipo"] == "examenes":
            examenes_label = tk.Button(frame_examenes, text=usuario["usuario"], bg='white', font=('Arial', 12), anchor="w", padx=10, command=lambda: sala_de_chat(ventana_usuario, frame_header, label_usuarios, frame_usuarios, btn_regresar_chats))
            examenes_label.pack(fill='x', pady=5)
        else:
            pass

            
def sala_de_chat(ventana_usuario, header_frame, label_usuarios, frame_usuarios, btn_regresar_chats):
    frame_usuarios.pack_forget()
    label_usuarios.pack_forget()
    btn_regresar_chats.pack_forget()

    # Encabezado "Chat"
    label_chat = tk.Label(header_frame, text="Chat", bg='lightblue', font=('Arial', 14))
    label_chat.pack(side='left', padx=70)

    # Botón para regresar a los chats
    btn_regresar_chats = tk.Button(header_frame, text="Chats", command=lambda: [mostrar_chats(ventana_usuario, frame_usuarios), label_usuarios.pack_forget(), btn_regresar_chats.pack_forget(), header_frame.pack_forget(), frame_chat.pack_forget()])
    btn_regresar_chats.pack(side='right', padx=10)

    # Frame para el área de chat
    frame_chat = tk.Frame(ventana_usuario)
    frame_chat.pack(fill='both', expand=True)

    # Área de chat con un límite de altura
    chat = tk.Text(frame_chat, height=20)  # Limita la altura del chat
    chat.pack(fill='both', expand=True, padx=10, pady=(10, 0))

    # Entrada de mensaje y botón para enviar
    entry_frame = tk.Frame(frame_chat)
    entry_frame.pack(fill='x', padx=10, pady=10)

    entry_mensaje = tk.Entry(entry_frame)
    entry_mensaje.pack(fill='x', side='left', expand=True)

    btn_enviar = tk.Button(entry_frame, text="Enviar", command=lambda: enviar_mensaje(chat, entry_mensaje))
    btn_enviar.pack(side='right', padx=10)
    

# Crear ventana principal
root = tk.Tk()
root.title("Aplicación de Chats")
root.geometry("350x500")


# ==================== inicio de la aplicación ====================

# Crear un frame superior para el encabezado
header_frame = tk.Frame(root)
header_frame.pack(fill='x')

# Etiqueta "Bienvenido"
label_bienvenido = tk.Label(header_frame, text="Bienvenido", font=('Arial', 14))
label_bienvenido.pack(pady=10)

# botón iniciar como administrador

btn_admin = tk.Button(header_frame, text="Iniciar como administrador", command=iniciar_administrador)
btn_admin.pack(pady=10) 

# iniciar como usuario

btn_usuario = tk.Button(header_frame, text="Iniciar como usuario", command=iniciar_usuario)
btn_usuario.pack(pady=10)


# Iniciar la aplicación con la pantalla de login
root.mainloop()
