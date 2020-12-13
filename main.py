import os
from datetime import datetime
from prac import get_wiki_links


def decorator_logger(file_name):
    file_path = os.path.join(os.getcwd(), file_name)

    def get_function(function):
        def write_function_info(*args, **kwargs):
            result = function(*args, **kwargs)
            with open(file_path, 'a') as file:
                file.write('Called time' + '\n\t' + str(datetime.today()) + '\n')
                file.write('Function name' + '\n\t' + function.__name__ + '\n')
                if len(args) != 0:
                    for arg in args:
                        file.write('Arguments' + '\n\t' + str(arg) + '\n')
                elif len(kwargs) != 0 and len(args) != 0:
                    for kwarg in kwargs:
                        file.write('\t' + str(kwarg) + '\n')
                elif len(kwargs) != 0 and len(args) == 0:
                    for kwarg in kwargs:
                        file.write('Arguments' + '\n\t' + str(kwarg) + '\n')
                else:
                    file.write('Arguments' + '\n\t' + 'None' + '\n')
                file.write('Result' + '\n\t' + str(result) + '\n')
                file.write('\n')
            return result
        return write_function_info
    return get_function


def clear_logger(file_name):
    with open(file_name, 'w+') as file:
        file.seek(0)


@decorator_logger('function_info.txt')
def get_wiki_links__making_logs__():
    get_wiki_links('countries.txt')


if __name__ == '__main__':
    get_wiki_links__making_logs__()


