class GraphicalObject:
    def __init__(self, name: str, edges: int):
        self.name = name
        self.edges = edges

    def __str__(self):
        return f'Name of graphical object: {self.name}, count of edges:{self.edges}'


class Rectangle(GraphicalObject):
    def __init__(self, name: str, edges: int):
        super().__init__(name, edges)


class Object(GraphicalObject):
    def button_method(self, button_click: str, button_status: bool):
        self.button_click = button_click
        button_click = input('Would you like to click the button:')

        if button_click == 'Yes'.title():
            print('Button is now on pushed stage.')
        elif button_click == 'No'.title():
            print('You haven`t pushed a button.')
        else:
            print('Unknown action')


class Button(Object):
    def button_method(self, button_click: str, button_status: bool):
        return f'Button is {button_click}, button status {button_status}'


object1 = GraphicalObject('Rectangle', 4)
print(object1)
object2 = Object('Triangle', 3)
object2.button_method('Click', False)