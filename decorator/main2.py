
from functools import wraps
import os



def parametr_decor(path):

    def logger(old_function, path=path):
        import datetime
        time = datetime.datetime.now()
        @wraps(old_function)
        def new_function(*args, **kwargs,):

            result_old_function = old_function(*args, **kwargs)
            for path_ in path:

                with open(path_, 'a') as f:
                    str = f'{old_function(*args, **kwargs)}\n{args}\n{kwargs}\ntime={time}\nresult_old_function={result_old_function}\nname={old_function.__name__}\n'
                    f.write(str)
            return old_function(*args, **kwargs)
        return new_function
    return logger

# paths = ('log_1.log', 'log_2.log', 'log_3.log')
# @parametr_decor(paths)
# @parametr_decor(paths)
# def func(a, b):
#     return a / b
# a = func(1, 2)
def test_2():
    paths = ('log_1.log', 'log_2.log', 'log_3.log')

    for path in paths:
        if os.path.exists(path):
            os.remove(path)

        @parametr_decor(paths)
        def hello_world():
            return 'Hello World'

        @parametr_decor(paths)
        def summator(a, b=0):
            return a + b

        @parametr_decor(paths)
        def div(a, b):
            return a / b

        assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
        result = summator(2, 2)
        assert isinstance(result, int), 'Должно вернуться целое число'
        assert result == 4, '2 + 2 = 4'
        result = div(6, 2)
        assert result == 3, '6 / 2 = 3'
        summator(4.3, b=2.2)

    for path in paths:

        assert os.path.exists(path), f'файл {path} должен существовать'

        with open(path) as log_file:
            log_file_content = log_file.read()

        assert 'summator' in log_file_content, 'должно записаться имя функции'

        for item in (4.3, 2.2, 6.5):
            assert str(item) in log_file_content, f'{item} должен быть записан в файл'


if __name__ == '__main__':
    test_2()