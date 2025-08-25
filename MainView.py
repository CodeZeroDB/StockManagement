import tkinter as tk
from tkinter import ttk, messagebox

class StockManagementView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestión de Stock")
        self.geometry("700x500")
        self.products = []  # Lista para almacenar los productos
        self.create_widgets()

    def create_widgets(self):
        # Título
        title = tk.Label(self, text="Gestión de Stock", font=("Arial", 18))
        title.pack(pady=10)

        # Barra de búsqueda
        search_frame = tk.Frame(self)
        search_frame.pack(pady=5)
        tk.Label(search_frame, text="Buscar:").pack(side=tk.LEFT, padx=5)
        self.search_var = tk.StringVar()
        self.search_var.trace("w", self.update_search)
        search_entry = tk.Entry(search_frame, textvariable=self.search_var)
        search_entry.pack(side=tk.LEFT, padx=5)

        # Tabla de productos
        columns = ("ID", "Nombre", "Cantidad", "Precio")
        self.tree = ttk.Treeview(self, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)
        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Controles de entrada
        form_frame = tk.Frame(self)
        form_frame.pack(pady=5)

        tk.Label(form_frame, text="Nombre:").grid(row=0, column=0, padx=5)
        self.name_entry = tk.Entry(form_frame)
        self.name_entry.grid(row=0, column=1, padx=5)

        tk.Label(form_frame, text="Cantidad:").grid(row=0, column=2, padx=5)
        self.qty_entry = tk.Entry(form_frame)
        self.qty_entry.grid(row=0, column=3, padx=5)

        tk.Label(form_frame, text="Precio:").grid(row=0, column=4, padx=5)
        self.price_entry = tk.Entry(form_frame)
        self.price_entry.grid(row=0, column=5, padx=5)

        # Botones
        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=10)

        add_btn = tk.Button(btn_frame, text="Agregar", command=self.add_product)
        add_btn.grid(row=0, column=0, padx=5)

        del_btn = tk.Button(btn_frame, text="Eliminar", command=self.delete_product)
        del_btn.grid(row=0, column=1, padx=5)

    def add_product(self):
        name = self.name_entry.get()
        qty = self.qty_entry.get()
        price = self.price_entry.get()
        if not name or not qty or not price:
            messagebox.showwarning("Campos vacíos", "Por favor, complete todos los campos.")
            return
        try:
            qty = int(qty)
            price = float(price)
        except ValueError:
            messagebox.showerror("Error", "Cantidad debe ser un número entero y precio un número válido.")
            return
        item_id = len(self.products) + 1
        product = (item_id, name, qty, price)
        self.products.append(product)
        self.update_treeview()
        self.name_entry.delete(0, tk.END)
        self.qty_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)

    def delete_product(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showinfo("Seleccionar", "Seleccione un producto para eliminar.")
            return
        for item in selected:
            values = self.tree.item(item, "values")
            self.products = [p for p in self.products if str(p[0]) != str(values[0])]
            self.tree.delete(item)
        self.update_treeview()

    def update_treeview(self, filtered=None):
        # Limpia la tabla
        for item in self.tree.get_children():
            self.tree.delete(item)
        # Muestra productos filtrados o todos
        data = filtered if filtered is not None else self.products
        for product in data:
            self.tree.insert("", "end", values=product)

    def update_search(self, *args):
        query = self.search_var.get().lower()
        if not query:
            self.update_treeview()
            return
        filtered = [p for p in self.products if query in str(p[1]).lower()]
        self.update_treeview(filtered)

if __name__ == "__main__":
    app = StockManagementView()
    app.mainloop()