package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

type board struct {
	rows [5][5]int
	complete bool
	// efective check
	positions map[int]pos
}

type pos struct {
	row int
	col int
}

func callBingo(number int, boards *[]board, wonBoards *int) int {
	ret := -1
	for idx, b := range *boards {
		if val, ok := b.positions[number]; ok {
			(*boards)[idx].rows[val.row][val.col] = -1
			if checkRow((*boards)[idx], val.row) || checkCol((*boards)[idx], val.col) {
				if !(*boards)[idx].complete {
					ret = idx
					(*wonBoards)++
					(*boards)[idx].complete = true
				}
			}
		}
	}
	return ret
}

func checkRow(b board, row int) bool {
	for i := 0; i < 5; i++ {
		if b.rows[row][i] != -1 {
			return false
		}
	}
	return true
}

func checkCol(b board, col int) bool {
	for i := 0; i < 5; i++ {
		if b.rows[i][col] != -1 {
			return false
		}
	}
	return true
}


func read(fn string) ([]int, []board){
	file, err := os.Open(fn)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	// read bingo numbers
	var numbers []int
	scanner.Scan()
	lines := strings.Split(scanner.Text(), ",")
	for _, val := range lines {
		number, err := strconv.Atoi(val)
		if err != nil {
			log.Fatal(err)
		}
		numbers = append(numbers, number)
	}
	// read boards
	var boards []board
	var b *board = nil
	var idxRow int
	for scanner.Scan() {
		line := strings.TrimSpace(scanner.Text())
		// new board
		if line == "" {
			idxRow = 0
			// not first board
			if b != nil {
				boards = append(boards, *b)
			}
			b = &board{}
			(*b).positions = make(map[int]pos)
		// same board
		} else {
			vals := strings.Fields(line)
			for idx, number := range vals {
				val, err := strconv.Atoi(number)
				if err != nil {
					log.Fatal(err)
				}
				(*b).rows[idxRow][idx] = val
				(*b).positions[val] = pos{row: idxRow, col: idx}
			}
			idxRow++
		}
	}
	return numbers, boards

}

func calculateSum(b board) int {
	sum := 0
	for i := 0; i < 5; i++ {
		for j := 0; j < 5; j++ {
			if b.rows[i][j] != -1 {
				sum += b.rows[i][j]
			}
		}
	}
	return sum
}

func solve(fn string, part int) int {
	numbers, boards := read(fn)
	wonBoards := 0
	for _, number := range numbers {
		complete := callBingo(number, &boards, &wonBoards)
		if complete != -1 {
			if part == 1 {
				return calculateSum(boards[complete]) * number
			} else {
				// if all boards are completed, this was the
				// last one
				if wonBoards == len(boards) {
					return calculateSum(boards[complete]) * number
				}
			}
		}
	}
	return 0
}

func main() {
	fn := "input.txt"
	// part 1
	fmt.Println(solve(fn, 1))
	// part 2
	fmt.Println(solve(fn, 2))
}
