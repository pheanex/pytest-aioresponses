===================
pytest-aioresponses
===================

.. image:: https://img.shields.io/pypi/v/pytest-aioresponses.svg
    :target: https://pypi.org/project/pytest-aioresponses
    :alt: PyPI version

.. image:: https://img.shields.io/pypi/pyversions/pytest-aioresponses.svg
    :target: https://pypi.org/project/pytest-aioresponses
    :alt: Python versions

An integration of `aioresponses`_ for `py.test`_ similar to `pytest-responses`_

----

Installation
------------

You can install "pytest-aioresponses" via `pip`_ from `PyPI`_::

    $ pip install pytest-aioresponses


Usage
-----

.. sourcecode:: python


    import aiohttp
    import pytest

    @pytest.mark.asyncio
    async def test_something(aioresponses):
        aioresponses.get("https://hello.aio")

        async with aiohttp.ClientSession() as session:
            async with session.get("https://hello.aio") as response:
                assert response.status == 200

Contributing
------------
Contributions are very welcome.

License
-------

Distributed under the terms of the `MIT`_ license, "pytest-aioresponses" is free and open source software


Issues
------

If you encounter any problems, please `file an issue`_ along with a detailed description.

.. _`Cookiecutter`: https://github.com/audreyr/cookiecutter
.. _`@hackebrot`: https://github.com/hackebrot
.. _`MIT`: http://opensource.org/licenses/MIT
.. _`BSD-3`: http://opensource.org/licenses/BSD-3-Clause
.. _`GNU GPL v3.0`: http://www.gnu.org/licenses/gpl-3.0.txt
.. _`Apache Software License 2.0`: http://www.apache.org/licenses/LICENSE-2.0
.. _`cookiecutter-pytest-plugin`: https://github.com/pytest-dev/cookiecutter-pytest-plugin
.. _`file an issue`: https://github.com/pheanex/pytest-aioresponses/issues
.. _`pytest`: https://github.com/pytest-dev/pytest
.. _`tox`: https://tox.readthedocs.io/en/latest/
.. _`pip`: https://pypi.org/project/pip/
.. _`PyPI`: https://pypi.org/project/pytest-aioresponses/
.. _`aioresponses`: https://pypi.org/project/aioresponses/
.. _`pytest-responses`: https://pypi.org/project/pytest-responses/
.. _`py.test`: https://pypi.org/project/pytest/