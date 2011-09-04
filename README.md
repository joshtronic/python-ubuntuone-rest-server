# Client-side REST Server for interfacing with Ubuntu One

## What's it do?

Creates a RESTful interface to Ubuntu One's D-Bus interface that lives on port 3000 and can be utlized to build client side web applications on top of Ubuntu One.

## How do I run it?

Assuming you already have Python on your system (and the required libraries) and are running Ubuntu (Only OS I'll be testing this on) then all you need to do is run:

	./ubuntuone.py

## How do I talk to it?

Communicating with the server can be done by pointing your web browser to http://localhost:3000/status/current_status

The format of the URI is /objectPath/method

The data is returned as JSON

## What's the future hold?

Nothing, any future development will be done against my generic D-Bus server available here: https://github.com/joshtronic/python-dbus-rest-server