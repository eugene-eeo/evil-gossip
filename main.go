package main

import (
	"flag"
	"os"
	"bufio"
	"encoding/json"
	"github.com/eugene-eeo/evil-gossip/gossip"
)

type Result struct {
	Ticks uint
	Ok bool
}

func asyncSimulate(src <-chan *gossip.Params, dst chan<- Result) {
	for params := range src {
		ticks, ok := gossip.RunSimulation(*params)
		dst <- Result{
			Ticks: ticks,
			Ok: ok,
		}
	}
}

func startSimulation(p *gossip.Params, reps uint) <-chan Result {
	jobs := make(chan *gossip.Params, reps)
	sink := make(chan Result, reps)
	for i := 0; i < 4; i++ {
		go asyncSimulate(jobs, sink)
	}
	for i := uint(0); i < reps; i++ {
		jobs <- p
	}
	close(jobs)
	return sink
}

func main() {
	reps := flag.Uint("reps", 1000, "no. of repeats")
	good := flag.Uint("good", 50, "no. of good nodes")
	evil := flag.Uint("evil", 10, "no. of evil nodes")
	hk := flag.Uint("has_knowledge", 10, "no. of good nodes with knowledge")
	t := flag.Uint("ticks", 100, "max no. of ticks")
	p := flag.Float64("p", 0.5, "prob. of an edge between any 2 nodes")
	flag.Parse()

	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()

	repeats := *reps
	params := gossip.Params{
		Good: *good,
		Evil: *evil,
		HasKnowledge: *hk,
		Ticks: *t,
		P: *p,
	}
	sink := startSimulation(&params, repeats)
	for i := uint(0); i < repeats; i++ {
		r := <-sink
		data, err := json.Marshal([]interface{}{
			&r.Ticks,
			&r.Ok,
		})
		if err != nil {
			panic(err)
		}
		w.Write(data)
		w.WriteRune('\n')
	}
}
