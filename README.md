# TwitterAPI_IoT

============
Introduction
============
This application displays 10 recent posts about IoT
Using the buttons the user is able to:
1) Refresh for new searches
2) Save searches to a CSV file
3) Display the saved searches for offline functionality 

This application was tested using Python 3.5.2
This application was tested using Linux Mint 18.2

==========
Instal General Libraries
==========
To install the general libraries:

pip install tkinter
pip install pandas

==========
Installing python-twitter
==========

You can install python-twitter using::

    $ pip install python-twitter


If you are using python-twitter on Google App Engine, see `more information <GAE.rst>`_ about including 3rd party vendor library dependencies in your App Engine project.

The code is hosted at https://github.com/bear/python-twitter

Check out the latest development version anonymously with::

    $ git clone git://github.com/bear/python-twitter.git
    $ cd python-twitter

To install dependencies, run either::

	$ make dev

or::

    $ pip install -Ur requirements.testing.txt
    $ pip install -Ur requirements.txt

Note that ```make dev``` will install into your local ```pyenv``` all of the versions needed for test runs using ```tox```.

To install the minimal dependencies for production use (i.e., what is installed
with ``pip install python-twitter``) run::

    $ make env

or::

    $ pip install -Ur requirements.txt
    
==========
Running the application
==========
1)  Download the source using:
    git clone https://github.com/DanielSerebro/TwitterAPI_IoT.git

2)  Install the dependencies as seen above

3)  Using python 3:
    python main.py
                    OR
    python3 main.py
    
==========
Credit
==========
Application by Daniel Serebro

Thanks to the Python-Twitter Developers for the great API Library


