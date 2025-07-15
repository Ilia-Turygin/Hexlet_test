from functions import get_function

get = get_function()

if get({"key": "value"}, "key") != "value":
    raise Exception("Функция работает неверно!")

if get({"key": "value"}, "key", "default_value") != "value":
    raise Exception("Функция работает неверно!")

if get({}, "key", "default_value") != "default_value":
    raise Exception("Функция работает неверно!")
