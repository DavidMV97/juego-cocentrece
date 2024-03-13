import tkinter as tk
import random 

class Aplicacion:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Juego concéntrate')
        self.window.geometry("500x400")
        self.window.resizable(False, False)
        
        self.valor_botones = [1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8]
        self.valor_boton = 0
        self.botones = []
        
        for i in range(1, 17):
            self.valor_boton = self.valor_botones.pop(random.randrange(len(self.valor_botones))) 
            if i <= 4:
                self.row_button = 0
                self.colum_buttom = i - 1
            elif i <= 8:
                self.row_button = 1
                self.colum_buttom = i - 5
            elif i <= 12:
                self.row_button = 2
                self.colum_buttom = i - 9
            else:
                self.row_button = 3
                self.colum_buttom = i - 13
    
            self.boton1 = tk.Button(self.window, text=self.valor_boton, height=3, width=10)
            self.boton1.grid(column=self.colum_buttom, row=self.row_button)
            self.boton1.config(command=lambda btn=self.boton1: self.click_button(btn))
            self.botones.append(self.boton1)

            
        #Boton para ocultar los demas botones
        self.hide_buttons = tk.Button(self.window, text='Ocultar botones')
        self.hide_buttons.grid(column=1, row=5)
        self.hide_buttons.config(command=self.ocultar_botones)
        self.window.mainloop()
        
    def ocultar_botones(self):
        for boton in self.botones:
            boton.config(background=boton.cget("background"), foreground=boton.cget("background"))
    
        
    def click_button(self, button):
        print(button)
    

        
        
aplicacion = Aplicacion()
