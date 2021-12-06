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

func countBitsPerPos(oxDiag map[string]bool, idx int) (int, int){
	var zeroes, ones int
	for val := range oxDiag {
		if val[idx] == '1' {
			ones++
		} else {
			zeroes++
		}
	}
	return zeroes, ones
}

func oxygenCO2(diag map[string]bool, measure string) int64 {
	oxDiag := make(map[string]bool)
	for key := range diag {
		oxDiag[key] = false
	}
	idx := 0
	for len(oxDiag) > 1 && idx < 12{
		zeroes, ones := countBitsPerPos(oxDiag, idx)
		for key := range oxDiag {
			if measure == "oxygen" {
				if (zeroes <= ones && key[idx] != '1') || (zeroes > ones && key[idx] != '0') {
					delete(oxDiag, key)
				}
			} else {
				if (zeroes <= ones && key[idx] != '0') || (zeroes > ones && key[idx] != '1') {
					delete(oxDiag, key)
				}
			}
		}
		idx++
	}
	for key := range oxDiag {
		return binaryToInt(key)
	}
	return 0
}

func solve(fn string, part int) int64 {
	file, err := os.Open(fn)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)

	var ones, zeroes [12]int
	diag := make(map[string]bool)

	for scanner.Scan() {
		line := scanner.Text()
		diag[line] = false
		countBits(&ones, &zeroes, line)
	}

	var gint, eint int64
	if part == 1 {
		gint, eint = buildGammaEpsilon(ones, zeroes)
	} else {

		gint, eint = oxygenCO2(diag, "oxygen"), oxygenCO2(diag, "co2")
	}
	return gint * eint
}

func main() {
	fn := "input.txt"
	// part 1
	fmt.Println(solve(fn, 1))
	// part 2
	fmt.Println(solve(fn, 2))
}
