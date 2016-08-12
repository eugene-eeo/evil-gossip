evil-gossip
===========

a simulation to find out which model - fully or sparsely connected provides
better tolerance against multiple adversaries who can actively publish messages
using a gossip protocol.

* target: get all good nodes to agree that some value ``v`` is the correct
  message, within a number of ticks ``t``.
* all nodes broadcast at the same time each tick.
* good nodes:

  * keeps an internal counter of messages.
  * will bump the corresponding entry in the counter upon receiving.
  * always sends the message with the highest count.

* evil nodes:

  * always sends a different message ``!= v``.

* once only ``v`` is in circulation (by the good nodes) then the good
  nodes have won.
* else if ``t`` is used up before the previous condition they have lost.


usage
~~~~~

.. code-block:: shell

    # install dependencies
    $ make cpython   # or if you're feeling brave: make pypy
    $ ./evil-gossip --help


todo
~~~~

* write some tests
* write more tests
* generate nice graphs and PDFs
