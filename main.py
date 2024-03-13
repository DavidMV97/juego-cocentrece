import tkinter as tk
import random 

class Aplicacion:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('ventana')
        
        self.valor_botones = [1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8]
        self.valor_boton = 0
        
        for i in range(1, 17):
            self.valor_boton = self.valor_botones.pop(random.randrange(len(self.valor_botones))) 
            print('valor ramdon =>' , self.valor_boton)
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
    
            self.boton1 = tk.Button(self.window, text=self.valor_boton)
            self.boton1.grid(column=self.colum_buttom, row=self.row_button)
            
        self.window.mainloop()



aplicacion = Aplicacion()
