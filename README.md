# football-app contents

This project currently contains:
- python files for Django 1.9 setup
- python files for a Django based app
- template files for the Django app

Currently, the functionality is in development - only teams can be entered and viewed, no results or tables have been included.

These files have been derived from the tutorial from joincfe.com, which was published on YouTube under the username CodingEntrepreneurs. While the structure is the same, the variable names have been change to be more suitable to a football league application.

# football-app setup

In order to download and reuse this code, it is recommended to setup a virtual environment (using virtualenv or something similar). It's then necessary to delete the following files, which are initialised when migrating the project: database file (<b>db.sqlite3</b>), migration files (in the migrations folder) and any media/static files. From here, initilise the new project by running the following commands from the venv directory in command prompt:
- python manage.py makemigrations
- python manage.py migrate
- python amnage.py createsuperuser (<i>1</i>)
- python manage.py runserver (<i>2</i>)
 
(<i>1</i>) This step is to create the new admin user.<br>
(<i>2</i>) This final step is necessary to view the project locally in the browser


# football-app purpose

This repo will contain files for a Django app, which will consist of two main pages, the first of which being a user-oritentated page, which will at first be able to display football league information (results, table, etc). The second page will be a site admin-orientated page, as it will first of all be a place to enter match results and later maybe also a place to create new leagues, teams for those leagues and maybe even player information.
