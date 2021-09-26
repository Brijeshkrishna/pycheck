import os
from subprocess import PIPE, Popen
from typing import List, Union
from termcolor import colored
from click import command, option, argument
from re import search


def inbtw_finders(string: str, start: str, end: str, middle: str = '(.+?)') \
        -> Union[str, None]:
    """

    :param string: string
    :param start: starting
    :param end: ending
    :return: filtered string
    :rtype: Union[str,None]

    """
    try:

        return search(f'{start}{middle}{end}', string).group(1)
    except AttributeError:
        return ''


def my_decode(data: bytes):
    return data if data is None else data.decode("utf-8")


def cmd(command):
    proc = Popen(
        command, shell=1, stdin=PIPE, stdout=PIPE)
    output, error = proc.communicate()
    return my_decode(output)


def join(data: List):
    rv = ''
    for i in data:
        rv += ' '+i
    return rv


def flake8_buleprint(flake_out: str, col: int = 1):
    try:
        data1 = flake_out.split(" ")

        data2 = data1[0].split(':')

        file = data2[0].replace("/.", '')

        if file.find('.\\') == -1:
            file = '.\\'+file

        if col:
            file = colored(file, 'blue')
            line = colored(data2[1], 'yellow')
            column = colored(data2[2], 'cyan')
            error = colored(data1[1], 'red', attrs=['bold'])
            msg = colored(join(data1[2:]), 'white', attrs=['bold'])
        else:
            line = data2[1]
            column = data2[2]
            error = data1[1]
            msg = join(data1[2:])

        return file, line, column, error, msg

    except Exception:
        return None


def mypy_blueprint(mypy_out, col=1):
    try:
        data = mypy_out.split(' ')
        data2 = data[0].split(":")
        file = data2[0]
        if file.find('.\\') == -1:
            file = '.\\'+file
        if col:
            file = colored(file, 'blue')
            line = colored(data2[1], 'yellow')
            error = colored(data[1].replace(':', ""), 'red', attrs=['bold'])
            msg = colored(join(data[2:]), 'white', attrs=['bold'])
        else:

            line = data2[1]
            error = data[1].replace(':', "")
            msg = join(data[2:])

        return file, line, error, msg
    except Exception:
        return None


def main_blueprint(out_f, out_m, col=1):
    rv = []
    endline = ''
    j = 1
    file_count = 0
    for i in out_f:
        try:
            file, line, column, error, msg = flake8_buleprint(i, col=col)
            if col:

                rv.append(

                    f"{colored(j,'magenta')} > {file}:{line}:{column} {error} {msg}")

            else:
                rv.append(
                    f"{j} > {file}:{line}:{column} {error} {msg}")
            j += 1
        except Exception:
            pass

    for i in out_m:
        try:

            if i.find('Found') != -1:
                file_count = found_err(i)
            if i.find('Success') != -1:
                file_count = suss(i)

            file, line, error, msg = mypy_blueprint(i, col)

            if msg.find('Skipping') == -1 and msg.find('See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports') == -1:
                if col:

                    rv.append(
                        f"{colored(j,'magenta')} > {file}:{line} {error} {msg}")
                else:
                    rv.append(f"{j} > {file}:{line} {error} {msg}")
                j += 1

        except:
            pass

    if col:
        if j == 1:
            endline = colored(
                f"Success: no issues found (checked {file_count} source files) ✔", 'green', attrs=['bold'])
        else:
            endline = f"{colored('Found','red',attrs=['bold'])} {colored(j-1,'cyan',attrs=['bold'])} {colored('errors','red',attrs=['bold'])} {colored('(','blue',attrs=['bold'])}{colored ('checked','red',attrs=['bold'])} {colored(file_count,'cyan',attrs=['bold'])} {colored('source files','red',attrs=['bold'])}{colored(')','blue',attrs=['bold'])} ❌"
    else:
        if j == 1:
            endline = f"Success: no issues found (checked {file_count} source files) "
        else:
            endline = f"Found {j-1} errors (checked {file_count} source files) "

    return rv, endline


def found_err(string):
    return string.split(' ')[7]


def suss(string):
    return string.split(' ')[5]


def style_flake(path, filename_out, ot=0):
    try:
        if os.path.exists(path):

            out_f = (cmd(f'flake8 {path}')).split("\n")
            out_m = (cmd(f'mypy {path}')).split("\n")

            if ot:
                i, j = main_blueprint(out_f, out_m, 0)
                with open(filename_out, 'w') as f:
                    for i1 in i:
                        f.write(i1)
                    f.write(j)
            else:
                i, j = main_blueprint(out_f, out_m, 1)
                for i1 in i:
                    print(i1)
                print(j)
        else:
            print(f'''{colored("PYCHECK",'green',attrs=['bold'])} {colored(":",'blue',attrs=['bold'])} {colored("can't read file ❓ ",'red',attrs=['bold'])}{colored(">>",'blue',attrs=['bold'])} {colored("No such file or directory",'red',attrs=['bold'])} {colored("->",'blue',attrs=['bold'])} {colored(path,'cyan',attrs=['bold'])}''')

    except Exception:

        print(f'''{colored("PYCHECK",'green',attrs=['bold'])} {colored(":",'blue',attrs=['bold'])} {colored("Something went wroung  ",'red',attrs=['bold'])}{colored(">>",'blue',attrs=['bold'])} {colored("No such file or directory",'red',attrs=['bold'])} {colored("->",'blue',attrs=['bold'])} {colored(path,'cyan',attrs=['bold'])}''')


def ispy(string: str):
    return 1 if string.split('.\\')[-1].split('.')[-1] == 'py' else 0


@ command()
@ option('-o', help='output file', required=False, type=str)
@ argument('filename', required=1)
def pycheck(filename, o):
    if not(ispy(filename)):
        code = str(input(colored(
            'It is not a python file Do want to continue (y/n) ', 'blue', attrs=['bold']))).lower()
        if code == "n":
            exit()
        elif code != 'y':
            print(colored('It will be considered as yes ', 'green')+colored("(", 'blue',
                  attrs=['bold']) + colored(str(code), 'cyan') + colored(")", 'blue', attrs=['bold']))

    style_flake(filename, 0) if o is None else style_flake(
        filename, filename_out=o, ot=1)
