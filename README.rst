evil-gossip (WIP)
=================

a simulation to find out which model - fully or sparsely connected provides
better tolerance against multiple adversaries who can actively publish messages
using a gossip protocol.

* target: get all neutral nodes to agree that ``v`` is the correct message,
  within a number of ticks ``t``.
* all nodes broadcast at the same time each tick.
* neutral nodes:

  * keep an internal counter of messages.
  * will bump the corresponding entry in the counter upon receiving.
  * always sends the message with the highest count.

* good/evil nodes:

  * good always sends ``v``.
  * evil always sends a different message ``!= v``.
  * in this implementation the potency of the evil nodes is necessarily
    maximised as they all send the identical evil message.

* once only ``v`` is in circulation (by the neutral nodes) then the good
  nodes have won.
* once ``t`` is used up they have lost.

default parameters:

* **0 < p ≤ 1.0** (p = prob. of a link between two nodes)
* **K = 10** (K = no. of good nodes)
* **N = 100** (N = no. of neutral nodes)
* **10 ≤ B ≤ 50** (B = no. of evil nodes)
* **t = 500**
