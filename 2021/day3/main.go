package main

import(
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func countBits(ones *[12]int, zeroes *[12]int, line string) {
	for pos, char := range(line) {
		if char == '1' {
			(*ones)[pos]++
		} else {
			(*zeroes)[pos]++
		}
	}
}

func binaryToInt(binary string) int64 {
	i, err := strconv.ParseInt(binary, 2, 0)
	if err != nil {
		log.Fatal(err)
	}
	return i
}

func buildGammaEpsilon(ones [12]int, zeroes [12]int) (int64, int64) {
	var gamma, epsilon strings.Builder

	for i := 0; i < 12; i++ {
		if zeroes[i] < ones[i] {
			gamma.WriteString("1")
			epsilon.WriteString("0")
		} else {
			gamma.WriteString("0")
			epsilon.WriteString("1")
		}
	}
	return binaryToInt(gamma.String()), binaryToInt(epsilon.String())
}

func solve(fn string) int64 {
	file, err := os.Open(fn)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)

	var ones, zeroes [12]int
	for scanner.Scan() {
		line := scanner.Text()
		countBits(&ones, &zeroes, line)
	}
	gint, eint := buildGammaEpsilon(ones, zeroes)
	return gint * eint
}

func main() {
	fn := "input.txt"
	// part 1
	fmt.Println(solve(fn))
}
