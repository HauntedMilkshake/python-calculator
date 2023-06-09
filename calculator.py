#използвмае библиотека за потребителския интерфейс 
import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        
        # Създаваме дисплейа на калкулатора
        self.display_var = tk.StringVar()
        display = tk.Entry(master, textvariable=self.display_var, font=("Arial", 18))
        display.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")
        
        # бутоните, които калкулаторът ще има
        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+",
            "c"
        ]
        
        # добавяне на бутоникте към калкулатора
        row = 1
        col = 0
        for button in buttons:
            command = lambda x=button: self.button_click(x)
            tk.Button(master, text=button, command=command, font=("Arial", 14)).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            col += 1
            if col > 3:
                col = 0
                row += 1
    #метод за проверка дали бутон е натиснат
    def button_click(self, button):
        if button == "C":
            self.display_var.set("")
        elif button == "=":
            try:
                self.display_var.set(str(eval(self.display_var.get())))
            except:
                self.display_var.set("Error")
        elif button == "c":
            self.display_var.set("");
        else:
            self.display_var.set(self.display_var.get() + button)

root = tk.Tk()
calc = Calculator(root)
root.mainloop()
