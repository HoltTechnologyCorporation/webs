====
webs
====

The package webs provides a couple of console utilities related
to web scraping:

rps
---

Usage: `rps <things per second> <number of things>`

Calculates how much time do you need to process given number of things with given speed.

.. code:: bash

    $ rps 10 100
    10 sec
    $ rps 100 5m
    13 hr, 53 min, 20 sec
    $ rps 1k 500k
    8 min, 20 sec

myip
----

Usage: `myip`

Displays your external IPv4 address

.. code:: bash

    $ myip
    2.60.212.92

Feedback
--------

Either Drop mail to lorien@lorien.name or create ticket at https://github.com/lorien/webs/issues
