from zope.interface import Interface
from quintagroup.dropdownmenu.interfaces import IDropDownMenuLayer
from zope import schema
from plone.app.textfield import RichText
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm


class ILayer(IDropDownMenuLayer):
    pass


AlignVocab = SimpleVocabulary([
    SimpleTerm('left', 'left', u'Left'),
    SimpleTerm('right', 'right', u"Right")
])


class IExtendedMenuSettings(Interface):
    show = schema.Bool(title=u"Show Menu Text", default=False)

    html = RichText(title=u"HTML", default=u"")

    html_align = schema.Choice(
        title=u"HTML Align",
        description=u"To place the static html to the right or "
                    u"left of the links",
        default='right',
        vocabulary=AlignVocab)

    menu_align = schema.Choice(
        title=u"Menu Align",
        description=u"Menu edge alignment",
        default='left',
        vocabulary=AlignVocab)


class IExtendedMenuUtil(Interface):

    def allowed():
        pass
