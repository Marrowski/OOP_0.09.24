class GraphicalObject:
    def __init__(self, name: str, edges: int):
        self.name = name
        self.edges = edges

    def __str__(self):
        return f'Name of graphical object: {self.name}, count of edges:{self.edges}'


class Rectangle(GraphicalObject):
    pass


class Object(GraphicalObject):
    def button_method(self, button_click: str):
        self.button_click = button_click
        button_click = input('Would you like to click the button:')

        if button_click == 'Yes'.upper():
            print('Button is now on pushed stage.')
        elif button_click == 'No'.upper():
            print('You havent pushed a button.')
        else:
            print('Unknown action')


class Button(Object):
    def __init__(self, color: str, name: str, edges: int):
        super().__init__(name, edges)

