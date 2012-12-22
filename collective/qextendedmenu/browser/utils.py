from zope.component import getMultiAdapter
from zope.interface import implements
from Products.Five.browser import BrowserView
from collective.qextendedmenu.interfaces import IExtendedMenuUtil
from Products.CMFCore.interfaces._content import IContentish


class ExtendedMenuUtil(BrowserView):
    implements(IExtendedMenuUtil)

    def allowed(self):
        context_state = getMultiAdapter((self.context, self.request),
                                        name="plone_context_state")
        folder = context_state.folder()
        return IContentish.providedBy(folder)
