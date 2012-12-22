from collective.qextendedmenu import mf as _
from z3c.form import form, field
from plone.app.z3cform.layout import wrap_form
from collective.qextendedmenu.interfaces import IExtendedMenuSettings


class ExtendedMenuSettings(form.EditForm):
    """
    The page that holds all the gallery settings
    """

    fields = field.Fields(IExtendedMenuSettings)

    label = _(u'heading_menu_settings_form', default=u'Menu Settings')
    # description = _(u'description_gallery_settings_form',
    #     default=u'Configure the parameters for this gallery.')

    # successMessage = _(u'successMessage_gallery_settings_form',
    #     default=u'Gallery Settings Saved.')
    # noChangesMessage = _(u'noChangesMessage_gallery_settings_form',
    #     default=u'There are no changes in the Gallery settings.')


ExtendedMenuSettingsView = wrap_form(ExtendedMenuSettings)
