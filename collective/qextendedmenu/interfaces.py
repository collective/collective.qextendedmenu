from zope.interface import Interface
from quintagroup.dropdownmenu.interfaces import IDropDownMenuLayer
from zope import schema
from plone.app.textfield import RichText


class ILayer(IDropDownMenuLayer):
    pass


class IExtendedMenuSettings(Interface):
    show = schema.Bool(title=u"Show Menu Text", default=False)
    html = RichText(title=u"HTML", default=u"")


class IExtendedMenuUtil(Interface):

    def allowed():
        pass
