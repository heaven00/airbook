import sys

#activate_this = '/home/jayant/dev/bin/activate'
#execfile(activate_this, dict(__file__=activate_this))

sys.path.insert(0,'/var/www/airbook')

from app import app
application = app
