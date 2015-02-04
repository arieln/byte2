#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# standard imports you should have already been using
import webapp2
import logging
from webapp2_extras import jinja2
import urllib

# this library is for decoding json responses
from webapp2_extras import json

# this is used for constructing URLs to google's APIS
from apiclient.discovery import build

# This uses discovery to create an object that can talk to the 
# fusion tables API using the developer key
service = build('fusiontables', 'v1', developerKey=API_KEY)

API_KEY = 'AIzaSyAJ4Oy3T8l7pIzZcESKE_7BRdEQSzjVTZ4'

TABLE_ID = '14j_2miyTl5H78UEwDQTbo4jzJV700JD1Hvtk6J5M'


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.render_response('index.html', context)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)