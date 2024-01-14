# 0x00. AirBnB clone - The console
# Background Context
# Welcome to the AirBnB clone project!

![Example Image](hbnb.png)


Before starting, please read the AirBnB concept page.
## First step: Write a command interpreter to manage your AirBnB objects.

This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:
* put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
* create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
* create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
* create the first abstracted storage engine of the project: File storage.
* create all unittests to validate all our classes and storage engine
# What’s a command interpreter?

Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:
 * Create a new object (ex: a new User or a new Place)
 * Retrieve an object from a file, a database etc…
 * Do operations on objects (count, compute stats, etc…)
 * Update attributes of an object
 * Destroy an object
# Usage
The console works both in interactive mode and non-interactive mode, much like a Unix shell. It prints a prompt (hbnb) and waits for the user for input.

| Command | Example |
| ------- | ------- |
| Run the console | ./console.py |
| Quit the console | (hbnb) quit |
| Display the help for a command | (hbnb) help `<command>` |
| Create an object (prints its id) | (hbnb) create `<class>` |
| Show an object | (hbnb) show `<class>` `<id>` or (hbnb) `<class>`.show(`<id>`) |
| Destroy an object | (hbnb) destroy `<class>` `<id>` or (hbnb) `<class>`.destroy(`<id>`) |
| Show all objects, or all instances of a class | (hbnb) all or (hbnb) all `<class>` |


# GitHub
There should be one project repository per group. If you clone/fork/whatever a project repository with the same name before the second deadline, you risk a 0% score.

## More Info
## Execution
Your shell should work like this in interactive mode:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
But also in non-interactive mode: (like the Shell project in C)

```
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
# AUTHORS

* Victor Muthomi
* Solomon Kaniaru

