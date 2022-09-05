0x12. JavaScript - Warm up
==========================

-   By BG

Background Context
------------------

JavaScript is used for many things. Here, you will use JavaScript for 2 reasons:

-   Scripting (same as we did with Python)
-   Web front-end

For the moment, and for learning all basic concepts of this language, we will do some scripting. After, we will make our AirBnB project dynamic by using Javascript and JQuery.

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/303/Javascript-535.png.jpeg)

Resources
---------

**Read or watch**:

-   [Writing JavaScript Code](https://alx-intranet.hbtn.io/rltoken/3HLjEesLsmyWfRUWnxgUGg "Writing JavaScript Code")
-   [Variables](https://alx-intranet.hbtn.io/rltoken/zgOWmcpVLZFEmFlmuwayyg "Variables")
-   [Data Types](https://alx-intranet.hbtn.io/rltoken/VPd6JWaLrwOBzjAeXNAEqg "Data Types")
-   [Operators](https://alx-intranet.hbtn.io/rltoken/3HLjEesLsmyWfRUWnxgUGg "Operators")
-   [Operator Precedence](https://alx-intranet.hbtn.io/rltoken/PHtcJJk30gBNmlFQ9R4RVg "Operator Precedence")
-   [Controlling Program Flow](https://alx-intranet.hbtn.io/rltoken/tsreKcNh_KmTmLPHsfvJRw "Controlling Program Flow")
-   [Functions](https://alx-intranet.hbtn.io/rltoken/e3EfHIxICdIncGBwwIDbXQ "Functions")
-   [Objects and Arrays](https://alx-intranet.hbtn.io/rltoken/jg7IbvJpV2oLIKgqOAQH1g "Objects and Arrays")
-   [Intrinsic Objects](https://alx-intranet.hbtn.io/rltoken/jg7IbvJpV2oLIKgqOAQH1g "Intrinsic Objects")
-   [Module patterns](https://alx-intranet.hbtn.io/rltoken/g-MgvO09Ur02RhM63gVyXw "Module patterns")
-   [var, let and const](https://alx-intranet.hbtn.io/rltoken/gJi61GeJTRX0g-M0Rx-0Iw "var, let and const")
-   [JavaScript Tutorial](https://alx-intranet.hbtn.io/rltoken/Y8hkOcy5jO22lQGyF6_NiA "JavaScript Tutorial")
-   [Modern JS](https://alx-intranet.hbtn.io/rltoken/NZawtiBjWUpiojnrtVywNw "Modern JS")

Learning Objectives
-------------------

At the end of this project, you are expected to be able to [explain to anyone](https://alx-intranet.hbtn.io/rltoken/UFSXQvb7c_45LRd6SdzFTg "explain to anyone"), **without the help of Google**:

### General

-   Why JavaScript programming is amazing
-   How to run a JavaScript script
-   How to create variables and constants
-   What are differences between `var`, `const` and `let`
-   What are all the data types available in JavaScript
-   How to use the `if`, `if ... else` statements
-   How to use comments
-   How to affect values to variables
-   How to use `while` and `for` loops
-   How to use `break` and `continue` statements
-   What is a function and how do you use functions
-   What does a function that does not use any `return` statement return
-   Scope of variables
-   What are the arithmetic operators and how to use them
-   How to manipulate dictionary
-   How to import a file

Requirements
------------

### General

-   Allowed editors: `vi`, `vim`, `emacs`
-   All your files will be interpreted on Ubuntu 20.04 LTS using `node` (version 14.x)
-   All your files should end with a new line
-   The first line of all your files should be exactly `#!/usr/bin/node`
-   A `README.md` file, at the root of the folder of the project, is mandatory
-   Your code should be `semistandard` compliant (version 16.x.x). [Rules of Standard](https://alx-intranet.hbtn.io/rltoken/1T1yg1vOAChRN20Yyz8crw "Rules of Standard") + [semicolons on top](https://alx-intranet.hbtn.io/rltoken/35q5Pc6A6KWPyd3kGeRQFg "semicolons on top"). Also as reference: [AirBnB style](https://alx-intranet.hbtn.io/rltoken/ilo9MmB3u0utJZjZat-W3Q "AirBnB style")
-   All your files must be executable
-   The length of your files will be tested using `wc`

More Info
---------

### Install Node 14

```
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs

```

### Install semi-standard

[Documentation](https://alx-intranet.hbtn.io/rltoken/35q5Pc6A6KWPyd3kGeRQFg "Documentation")

```
$ sudo npm install semistandard --global

```

Quiz questions
--------------

Show

Tasks
-----

### 0\. First constant, first print

mandatory

Write a script that prints "JavaScript is amazing":

-   You must create a constant variable called `myVar` with the value "JavaScript is amazing"
-   You must use `console.log(...)` to print all output
-   You are not allowed to use `var`

```
success@ubuntu:~/0x12$ ./0-javascript_is_amazing.js
JavaScript is amazing
success@ubuntu:~/0x12$
success@ubuntu:~/0x12$ semistandard ./0-javascript_is_amazing.js
success@ubuntu:~/0x12$

```

**Repo:**

-   GitHub repository: `alx-higher_level_programming`
-   Directory: `0x12-javascript-warm_up`
-   File: `0-javascript_is_amazing.js`

### 1\. 3 languages

mandatory

Write a script that prints 3 lines:

-   The first line: "C is fun"
-   The second line: "Python is cool"
-   The third line: "JavaScript is amazing"
-   You must use `console.log(...)` to print all output
-   You are not allowed to use `var`

```
success@ubuntu:~/0x12$ ./1-multi_languages.js
C is fun
Python is cool
JavaScript is amazing
success@ubuntu:~/0x12$

```

**Repo:**

-   GitHub repository: `alx-higher_level_programming`
-   Directory: `0x12-javascript-warm_up`
-   File: `1-multi_languages.js`

### 2\. Arguments

mandatory

Write a script that prints a message depending of the number of arguments passed:

-   If no arguments are passed to the script, print "No argument"
-   If only one argument is passed to the script, print "Argument found"
-   Otherwise, print "Arguments found"
-   You must use `console.log(...)` to print all output
-   You are not allowed to use `var`

Reference: [process.argv](https://alx-intranet.hbtn.io/rltoken/5kTYi3rxb6KM1_pivm-tXg "process.argv")

```
success@ubuntu:~/0x12$ ./2-arguments.js
No argument
success@ubuntu:~/0x12$ ./2-arguments.js Best
Argument found
success@ubuntu:~/0x12$ ./2-arguments.js Best School
Arguments found
success@ubuntu:~/0x12$

```

**Repo:**

-   GitHub repository: `alx-higher_level_programming`
-   Directory: `0x12-javascript-warm_up`
-   File: `2-arguments.js`

### 3\. Value of my argument

mandatory

Write a script that prints the first argument passed to it:

-   If no arguments are passed to the script, print "No argument"
-   You must use `console.log(...)` to print all output
-   You are not allowed to use `var`
-   You are not allowed to use `length`

```
success@ubuntu:~/0x12$ ./3-value_argument.js
No argument
success@ubuntu:~/0x12$ ./3-value_argument.js School
School
success@ubuntu:~/0x12$

```

**Repo:**

-   GitHub repository: `alx-higher_level_programming`
-   Directory: `0x12-javascript-warm_up`
-   File: `3-value_argument.js`

### 4\. Create a sentence

mandatory

Write a script that prints two arguments passed to it, in the following format: " is "

-   You must use `console.log(...)` to print all output
-   You are not allowed to use `var`

```
success@ubuntu:~/0x12$ ./4-concat.js c cool
c is cool
success@ubuntu:~/0x12$ ./4-concat.js c
c is undefined
success@ubuntu:~/0x12$ ./4-concat.js
undefined is undefined
success@ubuntu:~/0x12$

```

**Repo:**

-   GitHub repository: `alx-higher_level_programming`
-   Directory: `0x12-javascript-warm_up`
-   File: `4-concat.js`

### 5\. An Integer

mandatory

Write a script that prints `My number: <first argument converted in integer>` if the first argument can be converted to an integer:

-   If the argument can't be converted to an integer, print "Not a number"
-   You must use `console.log(...)` to print all output
-   You are not allowed to use `var`
-   You are not allowed to use `try/catch`

```
success@ubuntu:~/0x12$ ./5-to_integer.js
Not a number
success@ubuntu:~/0x12$ ./5-to_integer.js 89
My number: 89
success@ubuntu:~/0x12$ ./5-to_integer.js "89"
My number: 89
success@ubuntu:~/0x12$ ./5-to_integer.js 89.89
My number: 89
success@ubuntu:~/0x12$ ./5-to_integer.js School
Not a number
success@ubuntu:~/0x12$

```

**Repo:**

-   GitHub repository: `alx-higher_level_programming`
-   Directory: `0x12-javascript-warm_up`
-   File: `5-to_integer.js`

### 6\. Loop to languages

mandatory

Write a script that prints 3 lines: (like `1-multi_languages.js`) but by using an array of string and a loop

-   The first line: "C is fun"
-   The second line: "Python is cool"
-   The third line: "JavaScript is amazing"
-   You must use `console.log(...)` to print all output
-   You are not allowed to use `var`
-   You are not allowed to use any `if/else` statement
-   You can use only one `console.log`
-   You must use a loop (`while`, `for`, etc.)

```
success@ubuntu:~/0x12$ ./6-multi_languages_loop.js
C is fun
Python is cool
JavaScript is amazing
success@ubuntu:~/0x12$

```

**Repo:**

-   GitHub repository: `alx-higher_level_programming`
-   Directory: `0x12-javascript-warm_up`
-   File: `6-multi_languages_loop.js`

### 7\. I love C

mandatory

Write a script that prints `x` times "C is fun"

-   Where `x` is the first argument of the script
-   If the first argument can't be converted to an integer, print "Missing number of occurrences"
-   You must use `console.log(...)` to print all output
-   You are not allowed to use `var`
-   You can use only two `console.log`
-   You must use a loop (`while`, `for`, etc.)

```
success@ubuntu:~/0x12$ ./7-multi_c.js 2
C is fun
C is fun
success@ubuntu:~/0x12$ ./7-multi_c.js 5
C is fun
C is fun
C is fun
C is fun
C is fun
success@ubuntu:~/0x12$ ./7-multi_c.js
Missing number of occurrences
success@ubuntu:~/0x12$ ./7-multi_c.js -3
success@ubuntu:~/0x12$

```

**Repo:**

-   GitHub repository: `alx-higher_level_programming`
-   Directory: `0x12-javascript-warm_up`
-   File: `7-multi_c.js`

### 8\. Square

mandatory

Write a script that prints a square

-   The first argument is the size of the square
-   If the first argument can't be converted to an integer, print "Missing size"
-   You must use the character `X` to print the square
-   You must use `console.log(...)` to print all output
-   You are not allowed to use `var`
-   You must use a loop (`while`, `for`, etc.)

```
