import time


def bracket_sequence_check(string: str) -> bool:
    """Function takes a string and tells whether he is a bracket sequence."""
    return not bool(string.strip('()[]'))


def count_wrong_brackets(bracket_seq: str) -> dict[str, list[tuple[int, str]]]:
    """
    Function returns dictionary of unclosed brackets
    and incorrectly closing brackets.
    """
    # Example of return: {'left_brackets': [(1, '(')], 'right_brackets': [(12, ']')]}
    # Init dicts and variables
    unclosed_left_br = []
    unclosed_right_br = []
    wrong_left_br = []
    wrong_right_br = []
    previous_sym = None
    # Searching wrong brackets
    for i_enum, i_sym in enumerate(bracket_seq):
        # If opening bracket, continue cycle
        if i_sym in '([':
            unclosed_left_br.append((i_enum, i_sym))
        # If bracket does not close previous, remove or swap
        elif i_sym == ')':
            if previous_sym == '(':
                unclosed_left_br.pop()
            elif unclosed_left_br:
                wrong_left_br.append(unclosed_left_br.pop())
                wrong_right_br.append((i_enum, i_sym))
            else:
                unclosed_right_br.append((i_enum, i_sym))
        # Same as the previous one
        elif i_sym == ']':
            if previous_sym == '[':
                unclosed_left_br.pop()
            elif unclosed_left_br:
                wrong_left_br.append(unclosed_left_br.pop())
                wrong_right_br.append((i_enum, i_sym))
            else:
                unclosed_right_br.append((i_enum, i_sym))
        try:
            previous_sym = unclosed_left_br[-1][1]
        except IndexError:
            previous_sym = None
    unclosed_brackets = unclosed_left_br + unclosed_right_br

    return {
        'lefts_swap': wrong_left_br,
        'rights_swap': wrong_right_br,
        'brackets_remove': unclosed_brackets,
    }


def fix_bracket_seq(string: str) -> str:
    """Function makes bracket sequence correct."""
    wrongs = count_wrong_brackets(string)
    symbols: dict = {i_num: i_sym for i_num, i_sym in enumerate(string)}

    if lefts_swap := wrongs.get('lefts_swap'):
        for i_num, i_sym in lefts_swap:
            symbols[i_num] = '(' if i_sym != '(' else '['
    if brackets_remove := wrongs.get('brackets_remove'):
        for i_num, _ in brackets_remove:
            symbols.pop(i_num)

    return ''.join(symbols.values())


def ui_main_func(user_input: str = None) -> None:
    """
    Function takes bracket sequence as user input, outputs result.
    You can use this function as user interface or as common func.
    """
    if not user_input:
        user_input = input('You can input new bracket sequence: ')
    if not bracket_sequence_check(user_input):
        print(f'{user_input} is not a bracket sequence')
    else:
        print(f'{user_input} is a bracket sequence')
    wrong_brackets: dict = count_wrong_brackets(user_input)
    print(wrong_brackets)
    new_sequence = fix_bracket_seq(user_input)
    print('New sequence:', new_sequence, end='\n\n')


if __name__ == '__main__':
    # examples
    for i_str in (
        '[((())()(())]]',
        '((((()', '][[])(()', '())))))))', '))))(((]]]]]',
        ')()(((((()))))][][][))()][][]())()'
    ):
        ui_main_func(i_str)
        time.sleep(2)

    # with user input
    while True:
        ui_main_func()
