from bnsManager import lookup
import tkinter as tk
from tkinter import ttk

class SimpleBrowser(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Simple Browser")
        self.geometry("800x600")

        # Create a frame for the URL bar and buttons
        navigation_frame = ttk.Frame(self)
        navigation_frame.pack(pady=10, fill=tk.X)

        # URL bar
        self.url_bar = ttk.Entry(navigation_frame, width=70)
        self.url_bar.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        self.url_bar.bind("<Return>", self.load_url)  # Bind Enter key

        # Navigation buttons
        self.back_button = ttk.Button(navigation_frame, text="Back", command=self.go_back)
        self.back_button.pack(side=tk.LEFT, padx=5)

        self.forward_button = ttk.Button(navigation_frame, text="Forward", command=self.go_forward)
        self.forward_button.pack(side=tk.LEFT, padx=5)

        self.reload_button = ttk.Button(navigation_frame, text="Reload", command=self.reload)
        self.reload_button.pack(side=tk.LEFT, padx=5)

        # Web view (placeholder)
        self.web_view = tk.Text(self, wrap=tk.WORD)
        self.web_view.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)

        # Add a status bar
        self.status_bar = ttk.Label(self, text="Welcome to Simple Browser", relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def go_back(self):
        # Placeholder for back functionality
        print("Back button pressed")

    def go_forward(self):
        # Placeholder for forward functionality
        print("Forward button pressed")

    def reload(self):
        # Placeholder for reload functionality
        print("Reload button pressed")

    def load_url(self, event):
        domain_to_lookup = self.url_bar.get()  # Get the URL from the entry
        lookup(domain_to_lookup)
        print(f"{domain_to_lookup} {ip_address}")  # Replace with actual loading functionality

if __name__ == "__main__":
    app = SimpleBrowser()
    app.mainloop()
