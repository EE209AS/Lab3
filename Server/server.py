from BaseHTTPServer import BaseHTTPRequestHandler
import subprocess as sp
import cgi
import urlparse
import json

class PostHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed_path = urlparse.urlparse(self.path)
        origin = ""

        for name, value in sorted(self.headers.items()):
            print name, value
            if name == "origin":
                origin = value

        arr = range(0,40)
        message = json.dumps(arr)
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', origin)
        self.send_header('Access-Control-Allow-Methods', 'GET')
        self.end_headers()
        self.wfile.write(message)
        return


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


        filename = form["Song"].value + '.out'
        if form['Action'].value == 'Start':
            sp.Popen(['./'+filename])

        elif form['Action'].value == 'Stop':
	    filename2 = form["Song"].value + '\.out'
	    print 'filename: ', filename2
            p1 = sp.Popen(['ps'], stdout=sp.PIPE)
	    p2 = sp.Popen(['grep', filename2],stdin=p1.stdout, stdout=sp.PIPE)
      	    output = p2.communicate()[0]
	    pid = output.split()[0]
            print 'killing process', pid
            sp.call(['kill', pid])

        elif form['Action'].value == 'Tempo':
            sp.call(['./', filename + "_" + "tempo.out"])
        else:
            print 'wrong Action'
        return

from BaseHTTPServer import HTTPServer
server = HTTPServer(('0.0.0.0', 8000), PostHandler)
print 'Starting server on 8000, use <Ctrl-C> to stop'


server.serve_forever()
