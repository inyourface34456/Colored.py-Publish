Colored.py
===============
This is a library for coloring text in python.  This library has 7 functions.  They are as follows:

1. ``cprint()``
	1. This function will print the text inputed with color.  If no color is chosen, then i will through an error.  For this function to work, you *must* have a forground and background color. The arguments are keyword arguments, the order of arguments dose not matter.  The format is as follows:
	
	   1. `rgb`, `on_rgb`: These arguments are for the Foreground and background, respectivly. They take arguments in the form of a list of three elements, in the order of Red, Green, Blue
	   
	   2. `hex`, `on_hex`: These arguments are for background and forground, respectively.  They acept arguments of a 6-byte hex string(i.e `FFFFFF` or `12AB34`).
	   
       3. `keyword`, `on_keyword`: These arguments are for the Foreground and background, respectivly. They accept any css extended keywords. Not case sensitive.
       
       4. `attrs`: This is a list of arguments that has suport for all text attributes
       
2. ``type_print()``
	1. This is the same arguments as the `cprint` function, with the exeption of one argument.
	   1. `delay`: This is a `int` or `float` number.
3. ``check_in_array()``
	1. This is farly self expanatory. The arguments ar as follows:
	    1. `list_to_cheack`: this is the list that you look in.
	    2. `thing_to_cheack_for`: This is the string or float to cheack for.
	    3. `case_sensativity`: This is weather to enable case sensativity or not.
4. ``average()``
	1. This take as many arguments an you feed it. it can also take the average of a list.
	    1. `*nums`: This is in case you wanted to take the average of a set number of numbers.
	    2. `list`: This is a keyword argument, takes a list.
5. ``generator()``
	1. This takes the same pramaters as `cprint()`, exept that it returs the color values instead of printing them.
6. ``reset()``
	1. By defult, this will return the escape charater `\u001b[0m`. To make it print the same, use the argument `print = True`.
7. ``clear()``
	1. By defult, this will return the escape charater `\033c`. To make it print the same, use the argument `print = True`.



Installing
============

```bash
pip install colored
```

Usage
=====

```python
print(f'This will test the avarge function.\nThe average of the numbers 1 through 10 (5.5 is correct).\nFunction return: {average(1,2,3,4,5,6,7,8,9,10)}\nTesting the list input for the avrage function for numbers 1 through 10 (5.5 is correct).\nFunction return: {average(array = onethrough10)}')

cprint('RGB example', rgb = [0, 255, 0], on_rgb = [0, 0, 255])

cprint('HEX example', hex = '00FF00', on_hex = '0000FF')

cprint('Keyword example', keyword = 'aQua', on_keyword = 'coRnflOwerbLue')

cprint('Two diffrent color methods example', rgb = [0, 255, 0], on_hex = '0000FF')

cprint('Atributes example', attrs = ['bold', 'underline'],  rgb = [255,255,255], on_rgb = [0, 0, 0])

type_print('RGB example', rgb = [255, 255, 255], on_rgb = [0, 0, 0])

type_print('HEX example',hex = 'FFFFFF', on_hex = '000000')

type_print('Keyword example', keyword = 'wHite', on_keyword = 'black')

type_print('Two diffrent color methods example', rgb = [255, 255, 255], on_keyword = 'goldenrod')

type_print('Atributes example', keyword = 'wHite', on_keyword = 'black', attrs = ['bold', 'underline'])
```