from bnsManager import lookup
import tkinter as tk
from tkinter import ttk

class SimpleBrowser(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("betterWeb")
        self.geometry("800x600")

        navigation_frame = ttk.Frame(self)
        navigation_frame.pack(pady=10, fill=tk.X)

        self.url_bar = ttk.Entry(navigation_frame, width=70)
        self.url_bar.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        self.url_bar.bind("<Return>", self.load_url)  # Bind Enter key

        self.back_button = ttk.Button(navigation_frame, text="Back", command=self.go_back)
        self.back_button.pack(side=tk.LEFT, padx=5)

        self.forward_button = ttk.Button(navigation_frame, text="Forward", command=self.go_forward)
        self.forward_button.pack(side=tk.LEFT, padx=5)

        self.reload_button = ttk.Button(navigation_frame, text="Reload", command=self.reload)
        self.reload_button.pack(side=tk.LEFT, padx=5)

        self.web_view = tk.Text(self, wrap=tk.WORD)
        self.web_view.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)

        self.status_bar = ttk.Label(self, text="betterWeb", relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def go_back(self):
        print("Back button pressed")

    def go_forward(self):
        print("Forward button pressed")

    def reload(self):
       
        print("Reload button pressed")

    def load_url(self, event):
        domain_to_lookup = self.url_bar.get()
        ip_address = lookup(domain_to_lookup)
        print(f"{domain_to_lookup} {ip_address}")

if __name__ == "__main__":
    app = SimpleBrowser()
    app.mainloop()
