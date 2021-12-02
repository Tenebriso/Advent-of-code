package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func first(prevDepth *int, depth int, totalIncreases *int) {
	if *prevDepth != 0 && *prevDepth < depth {
			*totalIncreases++
	}
	*prevDepth = depth
}

func second(idx *int, currentDepth *int, prevDepth *int, depth int, window *[]int, totalIncreases *int) {
	(*idx)++
	(*currentDepth) += depth
	if *idx <= 3 {    // first sum
		*window = append(*window, depth)
	} else {
		*currentDepth -= (*window)[*idx%3]
		if *currentDepth > *prevDepth {
			*totalIncreases++
		}
		(*window)[*idx%3] = depth
	}
	*prevDepth = *currentDepth
}

func solve(fn string, part int) int {
	file, err := os.Open(fn)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	var prevDepth, currentDepth, totalIncreases, idx = 0, 0, 0, 0
	var window []int

	for scanner.Scan() {
		depth, err := strconv.Atoi(scanner.Text())
		if err != nil {
			log.Fatal(err)
		}
		if part == 1 {
			first(&prevDepth, depth, &totalIncreases)
		} else if part == 2{
			second(&idx, &currentDepth, &prevDepth, depth, &window, &totalIncreases)
		}
	}

	return totalIncreases
}

func main() {
	fn := "input.txt"
	// day 1
	fmt.Println(solve(fn, 1))
	// day 2
	fmt.Println(solve(fn, 2))
}
