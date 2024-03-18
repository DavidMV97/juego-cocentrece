
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random 

class Aplicacion:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Juego concéntrate')
        self.window.geometry("520x380")
        self.window.resizable(False, False)
        
        #contar clicks
        self.count = 0
        #contar coincidencias
        self.counter_match = 0
        self.valor_botones = [1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8]
        self.valor_boton = 0
        self.botones = []
        self.values_couple_buttons = []
        #Marco inferior
        self.botton_frame = ttk.Frame(self.window)
        self.botton_frame.grid(row=5, column=0, columnspan=4, pady=12)
        
     
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
    
            self.boton = tk.Button(self.window, text=self.valor_boton, height=3, width=12)
            self.boton.grid(column=self.colum_buttom, row=self.row_button, padx=3, pady=3)
            self.boton.config(command=lambda btn=self.boton: self.validate_click_button(btn))
            self.botones.append(self.boton)

            
        self.hide_buttons = tk.Button(self.botton_frame, text='Ocultar botones')
        self.hide_buttons.config(command=self.ocultar_botones, width=14, height=2, padx=3, pady=3)
        self.hide_buttons.pack(side="bottom")
        self.window.mainloop()
    
       
    def ocultar_botones(self):
        for boton in self.botones:
            boton.config(background='orange', foreground='orange', activebackground='orange', activeforeground='orange')
    
    
    def validate_click_button(self, button):
        self.count += 1
        button.config(background='blue', foreground='white', state='disabled')
        self.values_couple_buttons.append(button)
        if self.count > 1:
            self.window.after(1000, self.check_match_buttons, self.values_couple_buttons)
            self.count = 0
            self.values_couple_buttons = []
            
            
    
    def check_match_buttons(self, buttons):
        value_first_button = buttons[0].cget('text')
        value_second_button = buttons[1].cget('text')
        
        if value_first_button == value_second_button:
            buttons[0].config(background='green', foreground='white', state='disabled')
            buttons[1].config(background='green', foreground='white', state='disabled')
            self.counter_match += 1
        else:                                                                                                                                              
            buttons[0].config(background='orange', foreground='orange', state='normal')
            buttons[1].config(background='orange', foreground='orange', state='normal')
                    
        if self.counter_match == 8:
            nuew_game = messagebox.askyesno("Juego terminado", "¿Quieres jugar de nuevo?")
            if nuew_game:
                print('Jugar de nuevo')
            else:
                messagebox.showinfo("Juego terminado", "Muchas gracias por jugar")

    
aplicacion = Aplicacion()
