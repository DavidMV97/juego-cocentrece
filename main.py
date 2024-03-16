import tkinter as tk
import random 

class Aplicacion:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Juego concéntrate')
        self.window.geometry("500x400")
        self.window.resizable(False, False)
        
    
        self.count = 0
        self.valor_botones = [1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8]
        self.valor_boton = 0
        self.botones = []
        self.buttons_couple= []
        self.values_couple_buttons = []
        
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
            self.boton1.config(command=lambda btn=self.boton1: self.show_button(btn))
            self.botones.append(self.boton1)

            
        #Boton para ocultar los demas botones
        self.hide_buttons = tk.Button(self.window, text='Ocultar botones')
        self.hide_buttons.grid(column=1, row=5)
        self.hide_buttons.config(command=self.ocultar_botones)
        self.window.mainloop()
    
       
    def ocultar_botones(self):
        for boton in self.botones:
            boton.config(background='orange', foreground='orange')
    
    
    #Validar botones activos
    def show_button(self, button):
        self.count += 1
        button.config(background='blue', foreground='white', state='disabled')
        value_button = button.cget('text')
        
        if self.count > 1:
            for boton in self.botones:
                if boton.cget('state') == 'disabled' and not boton.cget('background') == 'orange':
                    print('state buttons =>', boton.cget('state'), boton.cget('text'))
                    self.buttons_couple.append(boton)
                    print('len aqui =>' , len(self.buttons_couple))
                    self.check_match_buttos(self.buttons_couple)
                    
            self.count = 0
        
    
    def check_match_buttos(self, buttons):
        
        if len(self.values_couple_buttons) > 2 :
            self.values_couple_buttons = []
        
        for boton in buttons:
            
            self.values_couple_buttons.append(boton.cget('text'))
            

        print('couple buttons =>' , self.values_couple_buttons)
        #if len(self.values_couple_buttons) > 2:
        #
        #self.values_couple_buttons = []
        print('count =>', self.count)
        
        
        
        
        
        
        
        
        
        
        #value_first_button = buttons[0].cget('text')
        #value_second_button = buttons[1].cget('text')
            
            #Cooredenadas primer boton 
            # value_row_first_button = buttons[0].grid_info()['row']
            # value_column_first_button = buttons[0].grid_info()['column']
            # #Coordenadas segundo boton
            # value_row_second_button = buttons[1].grid_info()['row']
            # value_column_second_button = buttons[1].grid_info()['column']
            # # primer botón seleccionado
            # boton_select1 = tk.Button(self.window, height=3, width=10)
            # boton_select1.grid(column=value_column_first_button, row=value_row_first_button)
            # # segundo botón seleccionado
            # boton_select2 = tk.Button(self.window, height=3, width=10)
            # boton_select2.grid(column=value_column_second_button, row=value_row_second_button)
            
        #print('value first button =>',  value_first_button)
        #print('value second button =>',  value_second_button)
            
        # if value_first_button == value_second_button:
        #     print('Match de botones')
            #boton_select1.config(background='green', state='disabled', text=value_first_button)
            #boton_select2.config(background='green', state='disabled', text=value_first_button)
                
        # else:
        #     print('no match')
            #boton_select1.config(background='orange', state='normal', text=value_first_button)
            #boton_select2.config(background='orange', state='normal', text=value_second_button)
            #boton.config(background=boton.cget("background"), foreground=boton.cget("background"))
                
            
        self.buttons_couple = []

        
        
aplicacion = Aplicacion()
