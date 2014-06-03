import os
import sys

# Change working directory so relative paths (and template lookup) work again
my_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(my_dir)
os.chdir(my_dir)

TESTING = False
if TESTING:
  def application(environ, start_response):
      status = '200 OK'
      output = ",\n".join(sys.path)
      response_headers = [('Content-type', 'text/plain'),
                          ('Content-Length', str(len(output)))]
      start_response(status, response_headers)
      return [output]
        
else:
  # ... build or import your bottle application here ...
  import bottle
  import cleaner

  # Do NOT use bottle.run() with mod_wsgi
  application = bottle.default_app()
