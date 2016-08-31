package main

import "github.com/eugene-eeo/evil-gossip/gossip"
import "fmt"

func main() {
	fmt.Println(gossip.RunSimulation(
		50,
		10,
		5,
		0.2,
		100,
	));
}
