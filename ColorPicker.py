from kivy.app import App
from kivy.uix.colorpicker import ColorPicker

class ColorPickerApp(App):
    def build(self):
        cp = ColorPicker()

        def on_color(instance, value):
            print('RGBA = ', str(instance.color))
            print('HSV = ', str(instance.hsv))
            print('HEX = ', str(instance.hex_color))

        cp.bind(color = on_color)
        return cp

if __name__ == '__main__':
    ColorPickerApp().run()