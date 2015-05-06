Open West 2015 - django-fixtureless
===================================

This repository was created to support the presentation given at Open West 2015.  You can find the presentation .pdf included in this repository.

The bulk of this repository is an example website that provides a few use-cases for how (and why) you should use django-fixtureless (https://www.github.com/ricomoss/django-fixtureless) when building your Django projects.  Note this example is using Python 3 but should be Python 2.7+ compatible.

Installation
============

To begin you can clone this repository and setup Django using the following instructions.

Linux Installation (Debian/Ubuntu)
----------------------------------

.. note::

   The following will assume you are cloning the sourcecode to **~/Projects/open-west-2015-fixtureless**.  If you are cloning to a different location, you will need to adjust these instructions accordingly.

.. note::

   A dollar sign ($) indicates a terminal prompt, as your user, not root.

1.  Clone the source::

        $ cd ~/Projects
        $ git clone git@github.com:ricomoss/open-west-2015-fixtureless.git

2. Install some required packages::

        $ sudo apt-get install python3 python3-dev python-pip

3.  Install virtualenv and virtualenvwrapper::

        $ pip install virtualenv
        $ pip install virtualenvwrapper

4.  Add the following to your **~/.bashrc** or **~/.zshrc** file::

        source /usr/local/bin/virtualenvwrapper.sh

5.  Type the following::

        $ source /usr/local/bin/virtualenvwrapper.sh

6.  Create your virtualenv (for Python 3)::

        $ mkvirtualenv owf -p /usr/bin/python3


.. note::

    If you are using any virtualenv version prior to 1.10 it is strongly
    recommended that you upgrade to the most recent version (especially
    if you want to use Python 3).

7.  Add the following to the end of the file
    **~/.virtualenvs/owf/bin/postactivate**::

        export DJANGO_SETTINGS_MODULE=owc_fixtureless.settings
        export PYTHONPATH=~/Projects/open-west-2015-fixtureless/owc_fixtureless

8.  Activate the virtualenv::

        $ workon owf

9.  Install the required Python libraries (ensure you're within the new virtual environment).::

        (owf)$ pip install -r ~/open-west-2015-fixtureless/requirements.pip

10.  Sync the database (follow the Django instructions).::

        (owf)$ python ~/Projects/open-west-2015-fixtureless/owc_fixtureless/manage.py syncdb
        
11.  Start the runserver.::

        (owf)$ python ~/Projects/open-west-2015-fixtureless/owc_fixtureless/manage.py runserver
        
12.  Open your browser and see your site.::

        http://127.0.0.1:8000/
