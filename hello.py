#!/usr/bin/python3
#!-*-coding:utf8-*-
def hellowsgiapp(environ, start_response):
    qs = environ.get('QUERY_STRING', None)
    response = b''

    if qs:
        for l in qs.split('&'):
            response = response + l + '\n'

    start_response("200 OK", [
        ("Content-Type", "text/plain")
    ])
    return iter([response])
