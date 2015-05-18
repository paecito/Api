#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gdata import service
import gdata.blogger.client
import gdata.client
import gdata.sample_util
import gdata.data
import atom.data

#Funcion para crear un post en blogger
def CreatePublicPost(blogger_service, blog_id, title, content):
	entry = gdata.GDataEntry()
	entry.title = atom.Title('xhtml', title)
	entry.content = atom.Content(content_type='html', text=content)
	return blogger_service.Post(entry, '/feeds/%s/posts/default' % blog_id)

#Funcion para autenficarse en blogger
def login_blog():
    blogger_service = service.GDataService('sdkodiblog@gmail.com','blogkodisd')
    blogger_service.source = 'https://sdkodi-juang7.c9.io/'
    blogger_service.service = 'blogger'
    blogger_service.account_type = 'GOOGLE'
    blogger_service.server = 'www.blogger.com'
    blogger_service.ProgrammaticLogin()
    return blogger_service

#Metodo observador del id del blog
def blog_id():    
    blog_id = 5185572784043208024
    return blog_id
