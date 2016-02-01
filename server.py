from BaseHTTPServer import BaseHTTPRequestHandler
import subprocess as sp
import cgi

class PostHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        # Parse the form data posted
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type'],
                     })

        # Begin the response
        self.send_response(200)
        self.end_headers()
        self.wfile.write('Client: %s\n' % str(self.client_address))
        self.wfile.write('User-agent: %s\n' % str(self.headers['user-agent']))
        self.wfile.write('Path: %s\n' % self.path)
        self.wfile.write('Form data:\n')
        
        for field in form.keys():
            field_item = form[field]
            print field_item
            self.wfile.write('\t%s=%s\n' % (field, form[field].value))

        filename = form["Song"].value + '.out'
        if form['Action'].value == 'Start':
            sp.Popen(['./'+filename])

        elif form['Action'].value == 'Stop':
            p = sp.Popen(['ps','|', 'grep', filename, '|', 'grep', '-o', '^[^ ]*'])
            (pid,err) = p.communicate()
            print 'killing process', pid
            sp.call(['kill', pid])
        elif form['Action'].value == 'Tempo':
            sp.call(['gcc', filename + "_" + "tempo.c"])
        else:
            print 'wrong Action'

        return

from BaseHTTPServer import HTTPServer
server = HTTPServer(('localhost', 8000), PostHandler)
print 'Starting server on 8000, use <Ctrl-C> to stop'

server.serve_forever()
