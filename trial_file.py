import tkinter as tk

def main():
    root = tk.Tk()
    w = tk.Label(root, text="Hello, world!")
    w.pack(side="left")
    root.mainloop()
def create_board(self):
    # Draw top vertical lines
    self.canvas.create_line(self.space_size, 0, self.space_size, self.height)
    for i in range(2, 11):
        self.canvas.create_line(i * self.space_size, 0, i * self.space_size, self.height // 11)

    # Left Horizontal Lines
    self.canvas.create_line(0, self.space_size, self.height, self.space_size, fill="black")
    for i in range(1, 11):
        self.canvas.create_line(0, i * self.space_size, self.height // 11, i * self.space_size, fill="black")

    # Draw bottom vertical lines
    for i in range(1, 10):
        self.canvas.create_line(i * self.space_size, 10 * self.space_size, i * self.space_size,
                                self.height, fill="black")
    self.canvas.create_line(10 * self.space_size, 0, 10 * self.space_size, self.height, fill="black")

    # Right horizontal lines
    for i in range(1, 10):
        self.canvas.create_line(10 * self.space_size, i * self.space_size, self.height,
                                i * self.space_size, fill="black")
    self.canvas.create_line(0, 10 * self.space_size, self.height, 10 * self.space_size, fill="black")

    self.canvas.create_line(self.height, 0, self.height, self.height)
    self.canvas.create_line(0, self.height, self.height, self.height)

if __name__=="__main__":
    main()