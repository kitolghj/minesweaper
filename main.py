# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.core.window import Window

class GameWidget(Widget):
    # Create a numeric property for the score
    score = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.score_label = Label(text="Score: 0", pos=(0, Window.height - 50))
        self.add_widget(self.score_label)
        self.start_game()

    def start_game(self):
        Clock.schedule_interval(self.update, 1.0 / 60.0)

    def update(self, dt):
        self.score += 1
        self.score_label.text = f"Score: {self.score}"

class GameApp(App):
    def build(self):
        return GameWidget()

if __name__ == "__main__":
    GameApp().run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
