import tkinter as tk

def main():
    root = tk.Tk()
    w = tk.Label(root, text="Hello, world!")
    w.pack(side="left")
    root.mainloop()

if __name__=="__main__":
    main()