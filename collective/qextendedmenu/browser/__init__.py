from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from quintagroup.dropdownmenu.browser.viewlets import GlobalSectionsViewlet
from collective.qextendedmenu.settings import ExtendedMenuSettings


class ExtendedGlobalSectionsViewlet(GlobalSectionsViewlet):
    recurse = ViewPageTemplateFile('templates/sections_recurse.pt')

    def _content_tabs(self):
        """Return tree of tabs based on content structure"""
        results = super(ExtendedGlobalSectionsViewlet, self)._content_tabs()
        # go through top level links and add static text if allowed
        for item in results:
            brain = item['item']
            obj = brain.getObject()
            settings = ExtendedMenuSettings(obj, self.request)
            if settings.show:
                item['show_static'] = True
                item['static_html'] = settings.getValue('html')
            else:
                item['show_static'] = False
                item['static_html'] = u''
            item['static_align'] = settings.html_align
            item['menu_align'] = settings.menu_align
        return results
