import sae
from mblog import wsgi

application = sae.create_wsgi_app(wsgi.application)