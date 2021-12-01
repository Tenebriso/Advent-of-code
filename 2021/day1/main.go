package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func first(fn string) int {
	file, err := os.Open(fn)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	var prevDepth, totalIncreases = 0, 0
	
	for scanner.Scan() {
		depth, err := strconv.Atoi(scanner.Text())
		if err != nil {
			log.Fatal(err)
		}
		if prevDepth != 0 && prevDepth < depth {
			totalIncreases++
		}
		prevDepth = depth
	}

	return totalIncreases
}

func second(fn string) int {
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
		idx++
		currentDepth += depth
		if idx <= 3 {
			window = append(window, depth)
		} else {
			currentDepth -= window[idx%3]
			if currentDepth > prevDepth {
				totalIncreases++
			}
			window[idx%3] = depth
		}
		prevDepth = currentDepth
	}

	return totalIncreases
}

func main() {
	// day 1
	fn := "input.txt"
	fmt.Println(first(fn))

	// day 2
	fmt.Println(second(fn))
}
