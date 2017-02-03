package main

import (
	"fmt"
)

func main() {
	var n int
	fmt.Scanf("%d", &n)
	result := 1
	for p:= 1; p <= n; p++ {
		result *= p
	}
	fmt.Print(result)
}
