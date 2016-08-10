evil-gossip
===========

a simulation to find out which model - fully or sparsely connected provides
better tolerance against multiple adversaries who can actively publish messages
using a gossip protocol.

- the target is to get all good nodes to agree that some value ``v``
  is the correct message, within a number of ticks ``t``.
- all nodes broadcast at the same time each tick.
- internally each node keeps a counter of messages.
- upon receiving a new message it will bump the corresponding entry in
  the counter.
- 'good' nodes will only send the message with the highest count.
- once only ``v`` is in circulation (by the good nodes) then the good
  nodes have won.
- else if ``t`` is used up before the previous condition they have lost.
