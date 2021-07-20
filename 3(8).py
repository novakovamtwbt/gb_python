class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):


        while True:
            try:
                val = int(input('Type the integer and press "Enter":'))
                self.my_list.append(val)
                print(f'LIST - {self.my_list} \n ')
            except:
                print(f" You can enter only integers! ")
                y_or_n = input(f'Would You like to try again? Yes/No ')

                if y_or_n == 'Yes' or y_or_n == 'yes':
                    print(try_except.my_input())
                elif y_or_n == 'No' or y_or_n == 'no':
                    return f'the program has been terminated'
                else:
                    return f'the program has been terminated'

try_except = Error(1)
print(try_except.my_input())