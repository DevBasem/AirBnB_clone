# AirBnB Clone - Command Interpreter

## Project Description

This project is the first step towards building an AirBnB clone, starting with a command interpreter to manage AirBnB objects. The command interpreter allows users to create, retrieve, update, and delete objects, as well as perform various operations on them.

## Command Interpreter

### How to Start

To start the command interpreter, run the `console.py` script:

```bash
$ ./console.py
```
### How to Use
Once the command interpreter is running, you can use the following commands:

- `help`: Display the available commands.
- `quit` or `EOF`: Exit the command interpreter.

## Examples

- Interactive Mode

```bash
$ ./console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) quit
$
```
- Non-interactive Mode

```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

## Authors

- Basem Ahmed