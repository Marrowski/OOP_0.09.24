#Завдання 1
class Editor:
    def view_document(self):
        print('You can view document in free version.')

    def edit_document(self):
        print('Sorry, but you cant edit documents on free version.')


class ProEditor(Editor):
    def edit_document(self):
        lisence_key = input('Input a license key:')
        correct_key = 'admin'

        if lisence_key == correct_key:
            Editor()
            print('You have access to edit document.')
        else:
            ProEditor()
            print('You haven`t access to edit document.')


edit1 = ProEditor()
edit1.edit_document()