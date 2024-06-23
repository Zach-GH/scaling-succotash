# byte-builders

A repository made for Foundations of Software Engineering project building.

The chosen language for this project is Python.

Style for this project shall be dictated by PEP 8 - Style Guide for Python Code.

<https://peps.python.org/pep-0008/>

## To contribute to the project

- Create an issue that explains the problem you are trying to solve.
- Create a branch where the name describes your issue or change.
- Clone your branch to a local repository.
- Write, add, and commit your changes to your branch.
- Create a pull request into the Master branch with yours as the head.
- There shall be a default reviewer assigned.
- All threads commented on the pull request must be resolved.
- Upon approval, the pull request will be merged.

To learn how to set up an SSH key and clone a git repository
read the following article:

<https://phoenixnap.com/kb/git-clone-ssh>

## Release

To release our project, I have chosen to use the Python module pyinstaller.
There are many benefits to pyinstaller, such as single file install which
make delivering software incredibly clean, and easy.  In addition, you are able
to run the executable without any of the needed modules installed on the target
audiences computer, (even Python!).

To create a release, `cd` into the directory of your project,
and run `pyinstaller -F main.py` this creates a `dist` directory
where the main executable that is created resides.  We then create
a release folder in our main repository, and copy the executable
to this location along with all of the assets required by our project.
Lastly, we zip the folder up, naming it project_name.zip which imagine
will change to the required format for our team project submittal.
This gets stored back into the same folder we just zipped up for ease
of cleaning, and cleanliness of our repo.

A closer look at how `pyinstaller` works can be read about here:

<https://pyinstaller.org/en/stable/>

## Template

Within the template folder there is a hello.py file to help detail what
file contributions should be stuctured like.  To run this file, navigate
to the corresponding folder in a CLI and enter `make project`.  This will
run a series of defined commands as well as the hello.py file.  You should
then see the following output appear in your terminal.

![running](template/running.png)
