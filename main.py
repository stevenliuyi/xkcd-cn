from google.appengine.api import users
from google.appengine.ext import ndb
import jinja2
import webapp2
import os
import os.path
import random
import re

JINJA_ENVIRONMENT = jinja2.Environment(
	loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
	extensions = ['jinja2.ext.autoescape'],
	autoescape = True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        xkcd_id, title, filename = randomize()
        template_values = {
            'id': xkcd_id,
			'title': title,
            'filename': filename
        }
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))

def randomize():
    # 'pics_copy' is a copy of 'pics' directory
    # 'pics' is a static directory, wihich is at a different location
    # in the server, so have to make a copy and not set it to be static
    pics = os.listdir(os.path.dirname(__file__) + '/pics_copy')
    rand_num = random.randint(0, len(pics)-1)
    filename = pics[rand_num]

    # extract id number from file name
    xkcd_id = re.search('^\d+_', filename).group(0)[:-1]

    # extract title from file name
    title = re.search('_.+_cn', filename).group(0)[1:-3]
    title = title.replace('_', ' ')

    return xkcd_id, title.upper(), filename

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
