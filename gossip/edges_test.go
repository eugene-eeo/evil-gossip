package gossip_test

import (
	"github.com/eugene-eeo/evil-gossip/gossip"
	"github.com/deckarep/golang-set"
	"math/rand"
	"testing"
	"testing/quick"
	"reflect"
)

type Params struct {
	Nodes []gossip.Node
	P float64
}

func (self Params) Generate(rand *rand.Rand, size int) reflect.Value {
	nodes := []gossip.Node{}
	for i := 0; i < rand.Intn(50); i++ {
		nodes = append(nodes, gossip.NewGoodNode())
	}
	return reflect.ValueOf(Params{
		P: rand.Float64(),
		Nodes: nodes,
	})
}

func makeSet(nodes []gossip.Node) mapset.Set {
	s := mapset.NewSet()
	for _, v := range nodes {
		s.Add(v)
	}
	return s
}

func TestDistEdges(t *testing.T) {
	assertion := func(x Params) bool {
		n := makeSet(x.Nodes)
		m := gossip.DistEdges(x.Nodes, x.P)
		for node, peers := range m {
			p := makeSet(peers)
			if p.Contains(node) || !p.IsSubset(n) {
				return false
			}
		}
		return true
	}
	if err := quick.Check(assertion, nil); err != nil {
		t.Error(err)
	}
}
