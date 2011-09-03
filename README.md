# Ubuntu One SyncDaemon REST API Server

## What's it do?

Creates a RESTful interface to Ubuntu One's DBus interface that lives on port 3000 and can be utlized to build client side web applications on top of Ubuntu One.

## Why does this exist?

This little server is the result of fighting with the PHP DBus bindings and trying it to work in the local user space. This is a rewrite of a Node.js version I wrote previously to utilize actual DBus bindings instead of relying on parsing the output of dbus-send

## How do I run it?

Assuming you already have Python (and any additional libraries) on your system and are running Ubuntu (Only OS I'll be testing this one) then all you need to do is run:

	./ubuntuone.py

## How do I talk to it?

Communicating with the server can be done by pointing your web browser to http://localhost:3000/status/current_status

The format of the URI is /objectPath/method

The data is returned as JSON

## What's the future hold?

* Documentation page when calling the server with no path
* Support for the root object path's methods (connect, disconnect, et cetera)
* POST methods to push as well as pull data
* Potentially spinning off this server into a more generic DBus web interface
