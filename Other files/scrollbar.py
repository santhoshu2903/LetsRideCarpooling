import tkinter as tk
from tkinter import ttk
import CTkTable  as ctkTable

class ScrollableTable(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.create_widgets()

    def create_widgets(self):
        # Create CTKTable
        self.table = ctkTable.CTkTable(self, rows=10, cols=5, selecttype='row', height=10)
        self.table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create Scrollbar
        yscrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.table.yview)
        yscrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Configure CTKTable to use the scrollbar
        self.table.configure(yscrollcommand=yscrollbar.set)

def main():
    root = tk.Tk()
    root.geometry('600x400')
    root.title('Scrollable CTKTable Example')

    app = ScrollableTable(root)
    app.pack(fill=tk.BOTH, expand=True)

    root.mainloop()

if __name__ == '__main__':
    main()
