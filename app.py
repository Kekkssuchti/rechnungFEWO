from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

class RechnungFEWO(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.windowsize = 800
        
        #add widgets to window
        #add input box
        
        self.line = Label(text="Rechnungs Erstellungs Programm", font_size=24,)
        self.line.set_top(self.windowsize)
        self.line.set_center_x(self.windowsize)
             
        self.label = Label(text="Kundenname:") 
        self.kundenname = TextInput(multiline=False, hint_text='Vor- und Nachname')
        
        self.submit = Button(text="Submit", font_size=18)
        self.submit.bind(on_press = self.submit_pressed)
        self.submit.set_center_y(self.windowsize)
        
        self.window.add_widget(self.line)
        self.window.add_widget(self.label)
        self.window.add_widget(self.kundenname)
        self.window.add_widget(self.submit)
        
        return self.window
      
    def submit_pressed(self, instance):
      print("Button pressed")
      kundenname = self.kundenname.text
      print("Kundenname:", kundenname)
      self.kundenname.text = ""

if __name__ == "__main__":
    RechnungFEWO().run()