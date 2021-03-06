import os
import sys
import itertools
import functools

def project_stats(path, extensions):
    """
    Вернуть число строк в исходниках проекта.

    Файлами, входящими в проект, считаются все файлы
    в папке ``path`` (и подпапках), имеющие расширение
    из множества ``extensions``.
    """
    filenames = iter_filenames(path)
    #print(filenames)
    filenames_with_extensions = list(with_extensions(extensions, filenames))
    #print(filenames_with_extensions)
    return functools.reduce(lambda x, y: x + y, list(total_number_of_lines(filenames_with_extensions)))



def total_number_of_lines(filenames):
    """
    Вернуть общее число строк в файлах ``filenames``.
    """
    return map(number_of_lines, filenames)

def number_of_lines(filename):
    """
    Вернуть число строк в файле.
    """
    return sum(map(lambda x: 1, open(filename, 'r', encoding="utf8")))


def iter_filenames(path):
    """
    Итератор по именам файлов в дереве.
    """
    # get filenames of all subdirectories
    list_ = list(os.walk(path))
    #filenames = (os.path.join(root, name) for root, dir, file in os.walk(path) for name in file)
    list1 = list(map(lambda x: x[0], list_))
    list2 = list(map(lambda x: x[-1], list_))
    list3 = list(map(lambda x, y: list(map(lambda z: os.path.join(x, z), y)), list1, list2))
    # make a flat list out of a list of lists
    filenames = list(itertools.chain.from_iterable(list3))
    return filenames


def with_extensions(extensions, filenames):
    """
    Оставить из итератора ``filenames`` только
    имена файлов, у которых расширение - одно из ``extensions``.
    """
    filenames_with_extensions = filter(lambda file: get_extension(file) in extensions, filenames)
    return filenames_with_extensions


def get_extension(filename):
    """ Вернуть расширение файла """
    return os.path.splitext(filename)[-1]


def print_usage():
    print("Usage: python project_sourse_stats_3.py <project_path>")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print_usage()
        sys.exit(1)

    project_path = sys.argv[1]
    print(project_stats(project_path, {'.py'}))
    #t = open("C:\\Users\\cvetk\\PycharmProjects\\pythonProject\BUF.py")
    #count = 1
    #print(sum(map(lambda x: 1, t)))
    # list_ = [('1', '2', ['a', 'b', 'c']), ('3', '4', ['d', 'e', 'f'])]
    # list2 = list(map(lambda x: x[-1], list_))
    # list1 = list(map(lambda x: x[0], list_))
    # print(list1)
    # print(list2)
    # list3 = list(map(lambda x, y: list(map(lambda z: x+z, y)), list1, list2))
    # print(list3)



