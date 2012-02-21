# coding=utf-8
from five import grok
from zope import schema

from Products.CMFCore.utils import getToolByName
from zope.app.component.hooks import getSite 
from Products.CMFCore.interfaces import ISiteRoot


class HomePageView(grok.View):
    grok.context(ISiteRoot)
    grok.require('zope2.View')
    grok.name('home-page')
    
    def get_Noticias(self):    
        local = self.context.getPhysicalPath()
        self.pc = getToolByName(self.context, 'portal_catalog')
        news = self.pc(portal_type=('News Item'),
                       review_state='published',
                       path={'query':'/'.join(local)},
                       sort_on='effective',
                       sort_order='descending',)
        
        if news:
            return [i.getObject() for i in news]
        else:
            return []
        
        
    def get_Video(self):
        
        if 'video' in getSite():
            obj = getSite()['video']
            return obj
        else:
            return None

    def get_Video2(self):
        
        if 'video-2' in getSite():
            obj = getSite()['video-2']
            return obj
        else:
            return None        
        
    def busca(self,path):    
        self.pc = getToolByName(self.context, 'portal_catalog')
        news = self.pc(portal_type=('Document'),
                       review_state='published',
                       path={'query': path},
                       sort_on='effective',
                       sort_order='descending',)
        
        if news:
            return [i.getObject() for i in news]
        else:
            return []
        
    def get_python(self):
        item = self.busca('/portal/dicas-e-exemplos/python')
        if item:
            return item
        else:
            return None
    
    def get_jquery(self):
        item = self.busca('/portal/dicas-e-exemplos/jquery')
        if item:
            return item
        else:
            return None

    def get_plone(self):
        item = self.busca('/portal/dicas-e-exemplos/plone')
        if item:
            return item
        else:
            return None        