|PyPI Version|

django-templates-macros
=======================

Add macros to your django templates

------
Origin
------

The original code of this app is taken from https://djangosnippets.org/snippets/2892/ by MattP.

This snippets cites::

    Based on snippet by
        Michal Ludvig <michal@logix.cz> http://www.logix.cz/michal
        http://djangosnippets.org/snippets/363/

    Extended for args and kwargs into templatetags/kwacro.py by
        Skylar Saveland <michal@logix.cz> http://skyl.org
        https://gist.github.com/skyl/1715202

    Modified to support rendering into context by matt@peloquin.com


-----
Where
-----

You can find this package here:

- Github repository: https://github.com/twidi/django-templates-macros
- Pypi package: https://pypi.python.org/pypi/django-templates-macros


-----
Usage
-----

0) Add this app "macros" to your INSTALLED_APPS

1) In your template load the library::

    {% load macros %}

2) Define a new macro called 'my_macro' that takes args and/or kwargs
   All will be optional::

    {% macro my_macro arg1 arg2 baz="Default baz" %}
        {% firstof arg1 "default_arg1" %}
        {% if arg2 %}{{ arg2 }}{% else %}default_arg2{% endif %}
        {{ baz }}
    {% endmacro %}

3) Use the macro with string parameters or context variables::

    {% usemacro my_macro "foo" "bar" baz="KW" %}
    <br>
    {% usemacro my_macro num_pages "bar" %}

  Renders like::

    foo bar KW
    77 bar Default baz

4) Alternatively save your macros in a separate file, e.g. "mymacro.html" and load it to the current template with::

        {% loadmacros "mymacros.html" %}

    Then use these loaded macros in as described above.

Bear in mind that defined and loaded macros are local to each template
file and are not inherited through `{% extends ... %}` tags.

5) When recursive macros are needed, use the 'recurse_macro' template tag::

    {% macro MENU entries %}
    <ul>
        {% for entry in entries %}
        <li>
            <a href="{{ entry.link }}"> {{ entry.label }} </a>
            {% if entry.children %}
                {% recurse_macro MENU entry.children %}
            {% endif %}
        </li>
        {% endfor %}
    </ul>
    {% endmacro %}
    {% usemacro MENU menu.children %}


.. |PyPI Version| image:: https://img.shields.io/pypi/v/django-templates-macros.svg
   :target: https://pypi.python.org/pypi/django-templates-macros
