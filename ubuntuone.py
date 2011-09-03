#!/usr/bin/env python 

from BaseHTTPServer import BaseHTTPRequestHandler
import urlparse
import dbus
import json

bus = dbus.SessionBus()

class GetHandler(BaseHTTPRequestHandler):

	def do_GET(self):
		parts = self.path.lower().split('/')

		payload = '{"error": "invalid request"}'

		if len(parts) == 3:
			interface = parts[1]
			method    = parts[2]

			u1_object    = bus.get_object('com.ubuntuone.SyncDaemon', '/' + interface)
			u1_interface = dbus.Interface(u1_object, 'com.ubuntuone.SyncDaemon.' + interface.capitalize())

			try:
				func = getattr(u1_interface, method)
			except AttributeError:
				payload = '{"error": "unknown method"}'
			else:
				payload = json.dumps(func())

		self.send_response(200)
		self.send_header('Content-Type', 'application/json')
		self.end_headers()
		self.wfile.write(payload)
		return

if __name__ == '__main__':
	from BaseHTTPServer import HTTPServer
	server = HTTPServer(('', 3000), GetHandler)
	print 'Starting server, use <Ctrl-C> to stop'
	server.serve_forever()
