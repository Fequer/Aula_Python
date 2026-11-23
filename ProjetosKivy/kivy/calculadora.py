from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MainApp(App):
    def build(self):
        self.operatores = ['+', '-', '*', '/']
        self.ultimo_operador = None
        self.ultimo_botao = None
        main_layout = BoxLayout(orientation='vertical')
        self.solucao = TextInput(multiline=False, readonly=True, halign='right', font_size=55)
        main_layout.add_widget(self.solucao)
        botoes = [["7", "8", "9", "/"],
                   ["4", "5", "6", "*"],
                   ["1", "2", "3", "-"],
                   [".", "0", "C", "+"]]
        for row in botoes:
            h_layout = BoxLayout()
            for label in row:
                botao = Button(text=label, pos_hint={'center_x': 0.5, 'center_y': 0.5})
                botao.bind(on_press=self.on_button_press)
                h_layout.add_widget(botao)
            main_layout.add_widget(h_layout)
        igual_botao = Button(text="=", pos_hint={'center_x': 0.5, 'center_y': 0.5})
        igual_botao.bind(on_press=self.on_solution)
        main_layout.add_widget(igual_botao)
        return main_layout

    def on_button_press(self, instance):
        current = self.solucao.text
        botao_text = instance.text
        if botao_text == "C":
            self.solucao.text = ""
        else:
            if current and (self.ultimo_operador and botao_text in self.operatores):
                return
            elif current == "" and botao_text in self.operatores:
                return
            else:
                new_text = current + botao_text
                self.solucao.text = new_text
        self.ultimo_botao = botao_text
        self.ultimo_operador = self.ultimo_botao in self.operatores

    def on_solution(self, instance):
        text = self.solucao.text
        if text:
            solution = str(eval(self.solucao.text))
            self.solucao.text = solution

MainApp().run()