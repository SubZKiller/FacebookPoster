#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import datetime
import json
import logging
import re
import random
import requests
import shutil
from pyquery import PyQuery as pq


def main(username, password, page):

    logging.basicConfig(filename='imgur2fb.log', level=logging.DEBUG)

    session = requests.session()

    uid, dtsg = login(session, username, password)

    grupoID = "Your_GroupID" #(Fijo)

    Mensaje = raw_input("Inserte mensaje ")

    postToFacebook(session, dtsg, grupoID, Mensaje,uid)


def login(session, username, password):

    '''
    Login to Facebook
    '''

    # Navigate to the Facebook homepage
    response = session.get('https://facebook.com')

    # Construct the DOM
    dom = pq(response.text)

    # Get the lsd value from the HTML. This is required to make the login request
    lsd = dom('[name="lsd"]').val()

    # Perform the login request
    response = session.post('https://www.facebook.com/login.php?login_attempt=1', data={
        'lsd': lsd,
        'email': username,
        'pass': password,
        'default_persistent': '0',
        'timezone': '-60',
        'lgndim': '',
        'lgnrnd': '',
        'lgnjs': '',
        'locale':'en_GB',
        'qsstamp': ''
    })

    '''
    Get the users ID and fb_dtsg token. The fb_dtsg token is required when making requests as a logged in user. It
    never changes, so we only need to grab this token once.

    If the login was successful a cookie 'c_user' is set by Facebook. If the login failed, the 'c_user' cookie
    will not be present. This will raise an exception.
    '''
    try:
        uid = session.cookies['c_user']
        dtsg = re.search(r'(type="hidden" name="fb_dtsg" value="([0-9a-zA-Z-_:]+)")', response.text).group(1)

        dtsg = dtsg[dtsg.find("value")+6:]
        dtsg = dtsg[1:-1]

    except KeyError:
        raise Exception('Login Failed!')

    return uid, dtsg


def postToFacebook(session, dtsg, pageID, message,uID):

    data = {
        "[0]":"",
        "[1]":"",
        "__ajax__":"",  #AYmIVqL7VfighmiRmFWSBGl6Aucepl7b-I5RPZaAyEEk7rT-6UQQ2zOpUe433RwWQaZACpH9gA--j8otSHry0_Kmd6iZtK2QHyufgZ59eoLtwA
        "__dyn":"",#    1KQdAm1mxu4UpwDF3GAgy6K6Acgy6F8mxq2K2i5U9EowRwFzohxO3J0GwywlEf8lwJwsE2xCyoe8hwv9E887u4o2CyUb852i1gw
        "__req":"",#    e
    "__user":"100016215514801",
    "album_fbid":"0",
    "appid":"",
    "at":"",
    "backdated_day":"",
    "backdated_month":"",
    "backdated_year":"",
    "ch":"",
    "csid":"",  #b4f44053-0da3-46b8-8c54-782fb428a624
    "fb_dtsg":dtsg, #AQEHse9gjZYA:AQGng01UK1fd
    "freeform_tag_place":"",
    "fs":"",
    "internal_extra":"",
    "is_backdated":"",
    "iscurrent":"",
    "linkUrl":"",
    "link_no_change":"",
    "loc":"{}",
    "m_sess":"",
    "message":message,# prueba 88
    "npa":"",
    "npc":"",
    "npn":"",
    "npp":"",
    "npw":"",
    "npz":"",
    "ogaction":"",
    "oghideattachment":"",
    "ogicon":"",
    "ogobj":"",
    "ogphrase":"",
    "ogsuggestionmechanism":"",
    "rating":"0",
    "scheduled_am_pm":"",
    "scheduled_day":"",
    "scheduled_hours":"",
    "scheduled_minutes":"",
    "scheduled_month":"",
    "scheduled_year":"",
    "sid":"",
    "source_loc":"composer_group",
    "target":pageID,
    "text_[0]":"",
    "text_[1]":"",
    "unpublished_content_type":"0",
    "waterfall_id":"988d79257398ec678a8e287046f322ca",  # Esto cambia en cada logueo??
    "waterfall_source":"composer_group"

    }


    response = session.post('https://m.facebook.com/a/group/post/add/?gid='+pageID+'&refid=18',

                            #params=params,
                            data=data,
                            #headers = {'content-type': 'multipart/form-data'})
                            headers = {'Content-Type':'application/x-www-form-urlencoded'})

    print response


try:
    main(username='insert_username', password='insert_password', page='insert URL')
except Exception, e:
    logging.exception(e)
    print e
