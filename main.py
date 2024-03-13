import tkinter as tk 

def create_buttons():
    boton1 = tk.Button(self.window, text='Incrementar', command=self.incrementar)
    boton1.grid(column=0, row=1)


class Aplicacion:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Juego concéntrate')
        self.row_button = 0 
        self.colum_buttom = 0 
        
        for i in range(0, 16):
            self.colum_buttom +=1
            if i > 4:
                self.colum_buttom = 0
                self.row_button = 1
                
            self.boton1 = tk.Button(self.window, text='1')
            self.boton1.grid(column=self.row_button, row=self.row_button)
            if i == 4:
                pass
              
    
        self.window.mainloop()
    
    
        
        
    
        
aplicacion = Aplicacion()