html-cleaner
============

Clean tags and attributes from Schoolwires HTML in preparation for 
move to new content management system.


Python paths
------------

From the command line as serveradm user:

      '', 
      '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/setuptools-2.1-py2.7.egg', 
      '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/pip-1.2.1-py2.7.egg', 
      '/Library/Frameworks/Python.framework/Versions/2.7/lib/python27.zip', 
      '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7', 
      '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-darwin', 
      '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-mac', 
      '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-mac/lib-scriptpackages', 
      '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-tk', 
      '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-old', 
      '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-dynload', 
      '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages'

From the app.wsgi environment (user=www, group=www):

      /System/Library/Frameworks/Python.framework/Versions/2.5/lib/python25.zip,
      /System/Library/Frameworks/Python.framework/Versions/2.5/lib/python2.5,
      /System/Library/Frameworks/Python.framework/Versions/2.5/lib/python2.5/plat-darwin,
      /System/Library/Frameworks/Python.framework/Versions/2.5/lib/python2.5/plat-mac,
      /System/Library/Frameworks/Python.framework/Versions/2.5/lib/python2.5/plat-mac/lib-scriptpackages,
      /System/Library/Frameworks/Python.framework/Versions/2.5/Extras/lib/python,
      /System/Library/Frameworks/Python.framework/Versions/2.5/lib/python2.5/lib-tk,
      /System/Library/Frameworks/Python.framework/Versions/2.5/lib/python2.5/lib-dynload,
      /Library/Python/2.5/site-packages,
      /System/Library/Frameworks/Python.framework/Versions/2.5/Extras/lib/python/PyObjC,
      /Volumes/kweb-d0-content/webapps-root/cleaner,
      /Volumes/kweb-d0-content/webapps-root/cleaner

Bottle 0.12 will still install in Python 2.5, so we're OK I guess.

In sites/0002\_any\_80\_kentweb.kentfieldschools.org.conf:

     <IfModule mod_wsgi.c>
        WSGIDaemonProcess cleaner user=www group=www processes=1 threads=5
        WSGIScriptAlias /cleaner /Volumes/kweb-d0-content/webapps-root/cleaner/app.wsgi

        <Directory /Volumes/kweb-d0-content/webapps-root/cleaner>
            WSGIProcessGroup cleaner
            WSGIApplicationGroup %{GLOBAL}
            Order deny,allow
            Allow from all
        </Directory>
      </IfModule>

