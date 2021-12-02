package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

type position struct {
	depth int
	forward int
	aim int
}

func movePartOne(direction string, val int, pos *position) {
	switch direction {
	case "forward":
		(*pos).forward += val
	case "down":
		(*pos).depth += val
	case "up":
		(*pos).depth -= val
	}
}

func movePartTwo(direction string, val int, pos *position) {
	switch direction {
	case "forward":
		(*pos).forward += val
		(*pos).depth += (*pos).aim * val
	case "down":
		(*pos).aim += val
	case "up":
		(*pos).aim -= val
	}
}

func solve(fn string, part int) int {
	file, err := os.Open(fn)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)

	pos := position{}

	for scanner.Scan() {
		line := strings.Split(scanner.Text(), " ")
		val, err := strconv.Atoi(line[1])
		if err != nil {
			log.Fatal(err)
		}
		if part == 1 {
			movePartOne(line[0], val, &pos)
		} else if part == 2 {
			movePartTwo(line[0], val, &pos)
		}
	}

	return pos.depth * pos.forward
}

func main() {
	fn := "input.txt"
	// part 1
	fmt.Println(solve(fn, 1))
	//part 2
	fmt.Println(solve(fn, 2))
}
