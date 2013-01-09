Introduction
============

This product extends quintagroup.dropdownmenu to add static text to the right
of the menu. This makes it more of a "Mega" menu.

Warning
-------

This product is only meant to be used with 2 levels and will prevent
more levels from being used with quintagroup.dropdownmenu.


How it works
------------

1) add collective.qextendedmenu to list of eggs
2) re-run buildout
3) restart server and install the collective.qextendedmenu on
   your plone site
4) on any top level object, click the "Actions" drop down and then
   click "Edit Menu Text"
5) select "Show Menu Text" checkbox and fill out html you would like
6) hit "Apply"

this also assumed you already have sub-menu items in folder you're
 applying it to


TODO
----

- handle left alignment of static text
- handle right alignment of menu
- handle links that are relative
