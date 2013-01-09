from collective.qextendedmenu.interfaces import IExtendedMenuSettings
from persistent.dict import PersistentDict
from zope.annotation.interfaces import IAnnotations
from zope.interface import implements
from lxml import etree
from lxml import html
from urlparse import urljoin
from plone.app.textfield.interfaces import ITransformer, IRichTextValue


class ExtendedMenuSettings(object):
    """
    Pretty much copied how it is done in Slideshow Folder
    hopefully no one is foolish enough to want a custom slider
    and a view slider.  If they are then the settings will
    overlap.
    """
    implements(IExtendedMenuSettings)

    settings_key = 'collective.qextendedmenu'

    def __init__(self, context, req=None):
        self.context = context
        annotations = IAnnotations(self.context)

        self._metadata = annotations.get(self.settings_key, None)
        if self._metadata is None:
            self._metadata = PersistentDict()
            annotations[self.settings_key] = self._metadata

    def __setattr__(self, name, value):
        if name[0] == '_' or name in ['context', 'settings_key']:
            self.__dict__[name] = value
        else:
            self._metadata[name] = value

    def getValue(self, name):
        value = getattr(self, name, None)
        if name == 'html' and IRichTextValue.providedBy(value):
            if value.mimeType == value.outputMimeType:
                return self.raw_encoded
            else:
                transformer = ITransformer(self.context, None)
                if transformer is None:
                    return None
                return transformer(value, value.outputMimeType)
        return value

    def __getattr__(self, name):
        value = self._metadata.get(name)
        if value is None:
            v = IExtendedMenuSettings.get(name)
            if v:
                return v.default
        return value
