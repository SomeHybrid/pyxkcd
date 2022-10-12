.. currentmodule:: xkcd

API Reference
===============

The following section outlines the API of pyxkcd.

.. note::
    If you get a ModuleNotFoundError when trying to import pyxkcd, check :doc:`installation`

Version Related Info
---------------------

.. data:: __version__

    A string representation of the version. e.g. ``'0.0.1'``. This is based
    off of :pep:`440`.

Clients
--------

Client
~~~~~~~

.. attributetable:: Client

.. autoclass:: Client
    :members:

AsyncClient
~~~~~~~~~~~

.. attributetable:: AsyncClient

.. autoclass:: AsyncClient
    :members:

Comic
--------

.. attributetable:: Comic

.. autoclass:: Comic
    :members:

Image
--------

.. attributetable:: Image

.. autoclass:: Image
    :members:

Exceptions
------------

The following exceptions are thrown by the library.

.. autoexception:: xkcd.errors.XkcdError
    :members:
    :show-inheritance:

.. autoexception:: xkcd.errors.InvalidComicError
    :members:
    :show-inheritance:

Exception Hierarchy
~~~~~~~~~~~~~~~~~~~~~

.. exception_hierarchy::

    - :exc:`Exception`
        - :exc:`xkcd.errors.XkcdError`
            - :exc:`xkcd.errors.InvalidComicError`