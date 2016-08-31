package gossip

import (
	"math/rand"
)

func DistEdges(xs []Node, p float64) map[Node][]Node {
	edges := make(map[Node][]Node)
	for i, a := range xs {
		for _, b := range xs[i+1:] {
			if rand.Float64() <= p {
				edges[a] = append(edges[a], b)
				edges[b] = append(edges[b], a)
			}
		}
	}
	return edges
}
