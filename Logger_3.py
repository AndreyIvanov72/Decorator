from datetime import datetime
import csv


def logger(path):
    def __logger(old_function):
        date = datetime.now()

        def new_function(*args, **kwargs):
            nonlocal date
            result = old_function(*args, **kwargs)
            for item in result:
                item['date'] = date
            fieldnames = [item for item in result[0].keys()]
            sort_list = sorted(fieldnames, key=lambda x: x[0])
            with open(path, 'w', encoding='utf-8', newline='') as file:
                data_writer = csv.DictWriter(file, sort_list)
                data_writer.writerows(result)

        return new_function

    return __logger
