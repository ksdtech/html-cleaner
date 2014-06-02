html-cleaner
============

Clean tags and attributes for help


Apache mod\_wsgi Integration
----------------------------

In sites/0002\_any\_80\_kentweb.kentfieldschools.org.conf:

   <IfModule mod_wsgi.c>
        WSGIDaemonProcess cleaner user=www group=www processes=1 threads=5
        WSGIScriptAlias /cleaner /Volumes/kweb-d0-content/webaps-root/clean\
er/app.wsgi

        <Directory /Volumes/kweb-d0-content/webapps-root/cleaner>
            WSGIProcessGroup cleaner
            WSGIApplicationGroup %{GLOBAL}
            Order deny,allow
            Allow from all
        </Directory>
    </IfModule>
