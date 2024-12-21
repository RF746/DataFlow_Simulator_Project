import tkinter as tk
from tkinter import ttk, messagebox


# Encapsulation and Decapsulation Functions
def osi_encapsulation(data):
    """Simulate data encapsulation through the OSI model with protocol headers."""
    layers = [
        ("Application Layer", "AppHeader"),
        ("Presentation Layer", "PresHeader"),
        ("Session Layer", "SessHeader"),
        ("Transport Layer", "TCPHeader"),
        ("Network Layer", "IPHeader"),
        ("Data Link Layer", "EthernetHeader"),
        ("Physical Layer", "PhysicalSignal"),
    ]

    encapsulated_data = data
    log = "\nEncapsulation Process:\n"
    for layer, header in layers:
        encapsulated_data = f"{header} + {encapsulated_data}"
        log += f"{layer}: {encapsulated_data}\n"
    return encapsulated_data, log


def osi_decapsulation(data):
    """Simulate data decapsulation through the OSI model."""
    headers = [
        "PhysicalSignal",
        "EthernetHeader",
        "IPHeader",
        "TCPHeader",
        "SessHeader",
        "PresHeader",
        "AppHeader",
    ]

    decapsulated_data = data
    log = "\nDecapsulation Process:\n"
    for header in headers:
        decapsulated_data = decapsulated_data.replace(f"{header} + ", "", 1)
        log += f"Removed {header}: {decapsulated_data}\n"
    return decapsulated_data, log


# GUI Implementation
def run_visualizer():
    """Run the network packet visualizer GUI."""
    def encapsulate():
        data = entry_data.get()
        if not data:
            messagebox.showwarning("Input Error", "Please enter data to encapsulate.")
            return

        encapsulated, log = osi_encapsulation(data)
        text_output.delete(1.0, tk.END)
        text_output.insert(tk.END, log)
        text_output.insert(tk.END, f"\nFinal Encapsulated Data:\n{encapsulated}")

    def decapsulate():
        data = entry_data.get()
        if not data:
            messagebox.showwarning("Input Error", "Please enter encapsulated data.")
            return

        decapsulated, log = osi_decapsulation(data)
        text_output.delete(1.0, tk.END)
        text_output.insert(tk.END, log)
        text_output.insert(tk.END, f"\nFinal Decapsulated Data:\n{decapsulated}")

    # GUI Setup
    root = tk.Tk()
    root.title("Network Packet Visualizer")

    frame = ttk.Frame(root, padding="10")
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    # Input
    ttk.Label(frame, text="Enter Data:").grid(row=0, column=0, sticky=tk.W, pady=5)
    entry_data = ttk.Entry(frame, width=50)
    entry_data.grid(row=0, column=1, pady=5)

    # Buttons
    button_encapsulate = ttk.Button(frame, text="Encapsulate", command=encapsulate)
    button_encapsulate.grid(row=1, column=0, pady=5)

    button_decapsulate = ttk.Button(frame, text="Decapsulate", command=decapsulate)
    button_decapsulate.grid(row=1, column=1, pady=5)

    # Output
    ttk.Label(frame, text="Output:").grid(row=2, column=0, sticky=tk.W, pady=5)
    text_output = tk.Text(frame, width=80, height=20, wrap="word")
    text_output.grid(row=3, column=0, columnspan=2, pady=5)

    # Start GUI loop
    root.mainloop()


if __name__ == "__main__":
    run_visualizer()
