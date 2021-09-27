## Starting the interpreter

Type the `math` command to start the interpreter

~~~
bash$ math
Math 0.1.0
Python 3.7.3 (default, Apr 24 2020, 18:51:23) 
[Clang 11.0.3 (clang-1103.0.32.62)]

math>
~~~

## Real numbers

To perform a real-valued calculation just enter the formula

~~~
math> 2+2
4
~~~

## Complex numbers

Complex number are represented in the form `x+yj`, where `x+` can be omitted when the value has only an imaginary part.

~~~
math> 1j**2
(-1+0j)
math> 1j**0.5
(0.7071067811865476+0.7071067811865475j)
~~~

## Answers

To view previous answers, type the `answer` command

~~~
math> answer
[(-1+0j), 2j, (0.7071067811865476+0.7071067811865475j)]
~~~

You can use a previous answer in a formula:

~~~
math> answer[1]**2
4
~~~

## History

To view the history type the `history` command

~~~
math> history
['1j**2', '(1+1j)**2', '(1j)**0.5', 'answer[1]**2']
~~~

You can re-evaluate a command in the history:

~~~
math> eval(history[2])**2
(2.220446049250313e-16+1j)
~~~
