import time


def input_check(user_input: str = None) -> None:
    """
    The function takes a string as input and
    outputs a print depending on the content.
    You can use this function as user interface or as common func.
    """
    if user_input is None:
        user_input = input('\nInput some number, name or numbers array: ')
    if user_input.isdigit():
        if int(user_input) > 7:  # Digit input check
            print('Hello')
    elif user_input.isalpha():  # Name input check
        if user_input.title() == 'John':
            print('Hello, John')
        else:
            print('There is no such name')
    else:  # Numbers array input check
        array = []
        for i_elem in user_input.strip('[]()').split(','):
            if i_elem.strip().isdigit():
                array.append(int(i_elem.strip()))
            else:
                return
        else:
            print('Your array: ', end='')
            print(list(filter(lambda x: not x % 3, array)))  # Filter numbers


if __name__ == '__main__':
    # examples
    for i_str in (
        '5', '7', '8', '10',
        'John', 'john', 'Natan', 'Drake',
        '[2]', '[999]', '(1, 2,3, 9, 4,     768,4)', '4, 5, 7, 8, 9, 123'
    ):
        input_check(i_str)
        time.sleep(1)

    # with user input
    while True:
        input_check()
