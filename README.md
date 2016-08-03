pyfcgi
======

- Version: 0.0.1
- Technologies:
  - Python
- Compatibility:
  - Apache HTTP Server (>= 2.4)
  - mod_fcgid (>= 2.3)
  - Python (>= 2.7)
- Dependencies:
  - flup (= 1.0.2) or flipflop (= 1.0)
- Copyright / Authors:
  - Krystian Pietruszka <kpietru@lokolab.net>
- Licenses:
  - MIT <http://opensource.org/licenses/MIT>
- Download: <https://github.com/lokolab/pyfcgi/releases>
- Homepage: <http://www.lokolab.net>

Wrapper for applications in Python via "mod_fcgid".
___________________________________________________

Installing and configuring
--------------------------

First, install the "lokolab.pyfcgi" Python package:

    cd /tmp
    wget https://github.com/lokolab/pyfcgi/archive/v0.0.1.tar.gz -O pyfcgi-0.0.1.tar.gz
    tar -xzvf pyfcgi-0.0.1.tar.gz
    cd pyfcgi-0.0.1
    python ./setup.py install

Or via another installer:

    pip install https://github.com/lokolab/pyfcgi/archive/v0.0.1.tar.gz

Second, create a file named "python3.fcgi" outside
your home directory and add the following lines*:

    #!/usr/local/python/3.4.3/bin/python

    from lokolab.pyfcgi.wrapper import PyfcgiWrapper

    w = PyfcgiWrapper()
    w.run()

Third, add the following lines to your Apache configuration*:

    <IfModule fcgid_module>
        Options +ExecCgi
        AddHandler fcgid-script .py
        FcgidWrapper /path/to/wrapper/python3.fcgi .py
        <IfModule suexec_module>
            SuexecUserGroup someuser someuser
        </IfModule>
    </IfModule>

Fourth, create a file named "app.py" inside your
website’s document root and add the following lines:

    from lokolab.pyfcgi.server import PyfcgiServer

    def app(environ, start_response):
        start_response('200 OK', [('content-type', 'text/html')])
        return '<h1>Hello world!</h1>'

    pyfcgi_init = PyfcgiServer(app).run()

Fifth, execute commands via shell*:

    chmod 744 /path/to/wrapper/python3.fcgi
    chown someuser:someuser /path/to/wrapper/python3.fcgi

Sixth, restart the Apache HTTP Server via shell:

    service apache2 restart

Finally, in the browser, enter `http://localhost/app.py`

References
----------

1. [FastCGI Specification][1]
2. [Flup – random assortment of WSGI servers][2]
3. [Flup – random Python WSGI stuff – documentation][3]
4. [FlipFlop – FastCGI wrapper for WSGI applications][4]
5. [FastCGI, Python, Apache, Ngnix, ...][5]
6. [Python Web Server Gateway Interface – documentation][6]
7. [Why is WSGI deployment under FASTCGI so painful?][7]
8. [Apache & "mod_fcgid" deployment][8]

[1]: http://web.archive.org/web/20160306081510/http://fastcgi.com/drupal/node/6?q=node/22
[2]: http://pypi.python.org/pypi/flup
[3]: http://www.saddi.com/software/flup/
[4]: http://pypi.python.org/pypi/flipflop
[5]: http://flask.pocoo.org/docs/0.10/deploying/fastcgi/
[6]: http://www.python.org/dev/peps/pep-3333/
[7]: http://blog.dscpl.com.au/2011/09/why-is-wsgi-deployment-under-fastcgi-so.html
[8]: http://mediadrop.net/docs/install/apache-fastcgi.html

________________________________________________________
[*] Paths and username should be modified to the server.

