this project is for CYO

to set up, 
+install requirements listed in requirements.txt
+add pages 'Concert','Repertoire', and 'Search'
	for each page, uncheck In navigation, choose template Placeholder/Forwarding Page, and add new item of type Application Content.  For Concert, Application should be Upcoming Concert \+ Archives.  For Repertoire, Application should be Repertoire Application.  For Search, Application should be Search Application.
+load data from fixtures
+manage.py rebuild_index

when on server...
turn on virtualenv...
+cd .virtualenvs/cyo
+source bin/activate
to restart...
+cd cyorchestra.org/tmp
+touch restart.txt
FYI static populates in public folder!
