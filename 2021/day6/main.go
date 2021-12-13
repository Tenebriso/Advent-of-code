package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func read(fn string) []int {
	var numbers []int
	file, err := os.Open(fn)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	scanner.Scan()
	line := strings.Split(scanner.Text(), ",")
	for _, i := range line {
		val, err := strconv.Atoi(i)
		if err != nil {
			log.Fatal(err)
		}
		numbers = append(numbers, val)
	}
	return numbers
}

func passDay(freq *[9]int) {
	aux := (*freq)[0]
	for idx := 0; idx < 8; idx++ {
		(*freq)[idx] = (*freq)[idx+1]
	}
	(*freq)[8] = aux
	(*freq)[6] += aux
}

func sum(v [9]int) int {
	var ret int
	for _, i := range v {
		ret += i
	}
	return ret
}

func solve(numbers []int, days int) int {
	var freq [9]int
	for _, val := range numbers {
		freq[val]++
	}
	for i := 0; i < days; i++ {
		passDay(&freq)
	}
	return sum(freq)
}

func main() {
	fn := "input.txt"
	// part 1
	fmt.Println(solve(read(fn), 80))
	// part 2
	fmt.Println(solve(read(fn), 256))
}
