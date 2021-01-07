
import functools
import xmlrpc.client

HOST = '172.16.240.36'
PORT = 8069
DB   = 'pruebas'
USER = 'empalacios@ing.usac.edu.gt'
PASS = 'pruebas'
ROOT = 'http://%s:%d/xmlrpc/' % (HOST, PORT)

# Login
uid = xmlrpc.client.ServerProxy(ROOT + 'common').login(DB, USER, PASS)
print('Logged in as %s (uid: %d' % (USER, uid))

call = functools.partial(
    xmlrpc.client.ServerProxy(ROOT + 'object').execute,
    DB,
    uid,
    PASS
)

# Read all sessions
sessions = call('openacademy.session',
    'search_read',
    [],
    [
        'name',
        'seats',
    ]
)
for session in sessions:
    print('Session %s (%s seats)' % (session['name'], session['seats']))

session_id = call(
    'openacademy.session',
    'create',
    {
        'name': 'My Session',
        'course_id': 2,
    }
)
