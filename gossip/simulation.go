package gossip

func allocateGood(good, has_knowledge uint) (pool []*GoodNode) {
	for i := uint(1); i <= good; i++ {
		node := NewGoodNode()
		if i <= has_knowledge {
			node.WithKnowledge()
		}
		pool = append(pool, node)
	}
	return
}

func allocateEvil(evil uint) (pool []*EvilNode) {
	for i := uint(1); i <= evil; i++ {
		pool = append(pool, &EvilNode{})
	}
	return
}

func combine(g []*GoodNode, e []*EvilNode) []Node {
	nodes := []Node{}
	for _, v := range g {
		nodes = append(nodes, v)
	}
	for _, v := range e {
		nodes = append(nodes, v)
	}
	return nodes
}

func broadcast(node Node, mailbox map[Node]map[bool]uint) bool {
	message, targets := node.Broadcast()
	for _, v := range targets {
		if mailbox[v] == nil {
			mailbox[v] = make(map[bool]uint)
		}
		mailbox[v][message]++
	}
	return message
}

func RunSimulation(good, evil, has_knowledge uint, p float64, ticks uint) (uint, bool) {
	good_nodes := allocateGood(good, has_knowledge)
	evil_nodes := allocateEvil(evil)
	mapping := DistEdges(combine(good_nodes, evil_nodes), p)
	for node, peers := range mapping {
		node.SetPeers(peers)
	}

	t := uint(0)
	for t < ticks {
		t++
		all_sent := true
		all_ok := true
		all_no := true
		mailbox := make(map[Node]map[bool]uint)

		for _, node := range good_nodes {
			message := broadcast(node, mailbox)
			if !node.Ready {
				all_sent = false
			}
			if message == true {
				all_no = false
			} else {
				all_ok = false
			}
		}

		if all_sent {
			if all_ok {
				return t, true
			}
			if all_no {
				break
			}
		}

		for _, node := range evil_nodes {
			broadcast(node, mailbox)
		}

		for node, inbox := range mailbox {
			node.Update(inbox)
		}
	}
	return t, false
}
