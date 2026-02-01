import tkinter as tk

# Fenster
root = tk.Tk()
root.title("ToDoApp")
root.geometry("600x400")
root.minsize(150, 250)
root.maxsize(650, 650)
root.resizable(False, True)

# Daten
todo = []

# Überschrift
label1 = tk.Label(root, text="To-Do Hinzufügen", bg="#0000EE", fg="white")
label1.pack(side="top", fill="x")

# Eingabe
entry = tk.Entry(root)
entry.pack(pady=5)

# Liste anzeigen
listbox = tk.Listbox(root)
listbox.pack(fill="both", expand=True, padx=10, pady=5)

# Funktionen
def add_todo():
    text = entry.get()
    if text:
        todo.append(text)
        listbox.insert(tk.END, text)
        entry.delete(0, tk.END)

def remove_todo():
    selection = listbox.curselection()
    if selection:
        index = selection[0]
        listbox.delete(index)
        todo.pop(index)

# Buttons
btn_add = tk.Button(root, text="Hinzufügen", command=add_todo)
btn_add.pack(pady=2)

btn_remove = tk.Button(root, text="Entfernen", bg="red", fg="white", command=remove_todo)
btn_remove.pack(pady=2)

root.mainloop()
