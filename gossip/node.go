package gossip

type Node interface {
	Broadcast() (bool, []Node)
	Update(map[bool]uint)
	SetPeers([]Node)
}

type GoodNode struct {
	counter map[bool]uint
	peers   []Node
	Ready   bool
}

func NewGoodNode() *GoodNode {
	return &GoodNode{
		counter: make(map[bool]uint),
		peers:   []Node{},
		Ready:   false,
	}
}

func (self *GoodNode) WithKnowledge() {
	self.counter[true]++
	self.Ready = true
}

func (self *GoodNode) Update(messages map[bool]uint) {
	for m, v := range messages {
		self.counter[m] += v
		self.Ready = true
	}
}

func argmax(counter map[bool]uint) bool {
	a := counter[true]
	b := counter[false]
	if a > b {
		return true
	} else {
		return false
	}
}

func (self *GoodNode) Broadcast() (bool, []Node) {
	if self.Ready {
		return argmax(self.counter), self.peers
	}
	return false, []Node{}
}

func (self *GoodNode) SetPeers(peers []Node) {
	self.peers = peers
}

type EvilNode struct {
	peers []Node
}

func (self *EvilNode) Update(messages map[bool]uint) {
}

func (self *EvilNode) Broadcast() (bool, []Node) {
	return false, self.peers
}

func (self *EvilNode) SetPeers(peers []Node) {
	self.peers = peers
}
