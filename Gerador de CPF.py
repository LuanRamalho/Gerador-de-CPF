import tkinter as tk
import random

def gerar_cpf():
    # Gera um número de CPF aleatório
    cpf_numero = f"{random.randint(100, 999)}.{random.randint(100, 999)}.{random.randint(100, 999)}-{random.randint(10, 99)}"
    cpf_label.config(text=cpf_numero)

# Criar a janela principal
root = tk.Tk()
root.title("Gerador de CPF")
root.geometry("300x200")
root.configure(bg="#ADD8E6")  # Cor de fundo bem colorida

# Texto de título
title_label = tk.Label(root, text="Gerador de CPF", font=("Helvetica", 16, "bold"), bg="#ADD8E6")
title_label.pack(pady=10)

# Botão para gerar o CPF
generate_button = tk.Button(root, text="Gerar CPF", command=gerar_cpf, bg="#87CEEB", font=("Helvetica", 14))
generate_button.pack(pady=10)

# Label para exibir o CPF gerado
cpf_label = tk.Label(root, text="", font=("Courier", 14, "bold"), bg="#ADD8E6")
cpf_label.pack(pady=10)

# Iniciar o loop principal
root.mainloop()
