#Завдання 1
class Editor:
    def __init__(self):
        print('Initializing editor class.')

    def view_document(self):
        print('You can view document in free version.')

    def edit_document(self):
        print('Sorry, but you cant edit documents on free version.')


class ProEditor(Editor):
    def edit_document(self):
        lisence_key = input('Input a license key:')
        correct_key = 'admin'

        if lisence_key == correct_key:
            print('You have access to edit document.')
        else:
            print('You haven`t access to edit document.')


editor1 = Editor()
editor1.view_document()
editor1.edit_document()

editor2 = ProEditor()
editor2.view_document()
editor2.edit_document()