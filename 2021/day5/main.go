package main

import(
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

type point struct {
	x int
	y int
}

func getPointFromLine(line []string) point {
	p := point{}
	x, err := strconv.Atoi(strings.TrimSpace(line[0]))
	if err != nil {
		log.Fatal(err)
	}
	p.x = x
	y, err := strconv.Atoi(strings.TrimSpace(line[1]))
	if err != nil {
		log.Fatal(err)
	}
	p.y = y
	return p
}

func isHorizontal(p1 point, p2 point) bool {
	if p1.y == p2.y {
		return true
	}
	return false
}

func isVertical(p1 point, p2 point) bool {
	if p1.x == p2.x {
		return true
	}
	return false
}

func addPoint(p point, pointCount map[point]int) int {
	var counter int
	if _, ok := pointCount[p]; ok {
		pointCount[p]++
		if pointCount[p] == 2 {
			counter++
		}
	} else {
		pointCount[p] = 1
	}
	return counter
}

func countHorizontal(p1 point, p2 point, pointCount map[point]int) int {
	var m, n, counter int
	if p1.x > p2.x {
		m = p2.x
		n = p1.x
	} else {
		m = p1.x
		n = p2.x
	}
	for i:= m; i <= n; i++ {
		// p1.y == p2.y
		aux := point{x: i, y: p1.y}
		counter += addPoint(aux, pointCount)
	}
	return counter
}

func countVertical(p1 point, p2 point, pointCount map[point]int) int {
	var m, n, counter int
	if p1.y > p2.y {
		m = p2.y
		n = p1.y
	} else {
		m = p1.y
		n = p2.y
	}
	for i:= m; i <= n; i++ {
		// p1.x == p2.x
		aux := point{x: p1.x, y: i}
		counter += addPoint(aux, pointCount)
	}
	return counter
}


func countDiagonal(p1 point, p2 point, pointCount map[point]int) int {
	var m, n, d, c, counter int
	if p1.x > p2.x {
		m = p2.x
		n = p1.x
		d = (p1.y - p2.y) / (p1.x - p2.x)
		c = p2.y - d * p2.x
	} else {
		m = p1.x
		n = p2.x
		d = (p2.y - p1.y) / (p2.x - p1.x)
		c = p1.y - d * p1.x
	}
	// go over all x coordinates
	// and generate y from the equation of the line
	for i:= m; i <= n; i++ {
		aux := point{x: i, y: d * i + c}
		counter += addPoint(aux, pointCount)
	}
	return counter
}

func countTotal(p1 point, p2 point, pointCounter map[point]int, part int) int {
	if isHorizontal(p1, p2) {
		return countHorizontal(p1, p2, pointCounter)
	} else if isVertical(p1, p2) {
		return countVertical(p1, p2, pointCounter)
	} else if part != 1 {
		return countDiagonal(p1, p2, pointCounter)
	}
	return 0
}

func solve(fn string, part int) int {
	var count int
	file, err := os.Open(fn)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	// map points to how many lines pass through them
	pointCounter := make(map[point]int)
	for scanner.Scan() {
		line := strings.Split(scanner.Text(), "->")
		p1 := getPointFromLine(strings.Split(line[0], ","))
		p2 := getPointFromLine(strings.Split(line[1], ","))
		if part == 1 {
			count += countTotal(p1, p2, pointCounter, 1)
		} else if part == 2 {
			count += countTotal(p1, p2, pointCounter, 2)
		}
	}
	return count
}

func main() {
	fn := "input.txt"
	// part 1
	fmt.Println(solve(fn, 1))
	// part 2
	fmt.Println(solve(fn, 2))
}
