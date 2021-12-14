package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"sort"
	"strings"
)

var stringToInt = map[string]int{"abcefg": 0, "cf": 1, "acdeg": 2,
				"acdfg": 3, "bcdf": 4, "abdfg": 5,
				"abdefg": 6, "acf": 7, "abcdefg": 8,
				"abcdfg": 9}

func countUnique(line []string) int {
	var count int
	for _, signal := range line {
		if len(signal) == 2 || len(signal) == 3 || len(signal) == 4 || len(signal) == 7 {
			count++
		}
	}
	return count
}

func decodeSignal(line []string, code map[rune]rune) int {
	power := 1000
	ret := 0
	for _, signal := range line {
		var decoded []string
		for _, letter := range signal {
			decoded = append(decoded, string(code[letter]))
		}
		sort.Strings(decoded)
		ret += stringToInt[strings.Join(decoded, "")] * power
		power = power / 10
	}
	return ret
}

func findByLength(line []string, length int) string {
	for _, i := range line {
		if len(i) == length {
			return i
		}
	}
	return ""
}

func countLetterFreq(line []string) map[rune]int {
	freq := make(map[rune]int)
	for _, signal := range line {
		for _, letter := range signal {
			if _, ok := freq[letter]; ok {
				freq[letter]++
			} else {
				freq[letter] = 1
			}
		}
	}
	return freq
}

func findLetter(line []string, mapping map[rune]rune, reverseMapping map[rune]rune, toFind rune, found string, length int) {
	helper := findByLength(line, length)
	var known string
	for _, letter := range found {
		known += string(mapping[letter])
	}
	for _, letter := range helper {
		if !strings.Contains(known, string(letter)) {
			mapping[toFind] = letter
			reverseMapping[letter] = toFind
			return
		}
	}
}


func decodeLetters(line []string) map[rune]rune {
	mapping := make(map[rune]rune)  // letter to bogus letter
	reverseMapping := make(map[rune]rune)  // bogus letter to letter
	freq := countLetterFreq(line)
	for key, val := range freq {
		switch val {
		case 4:
			mapping['e'] = key
			reverseMapping[key] = 'e'
		case 6:
			mapping['b'] = key
			reverseMapping[key] = 'b'
		case 9:
			mapping['f'] = key
			reverseMapping[key] = 'f'
		}
	}
	known := "f"
	findLetter(line, mapping, reverseMapping, 'c', known, 2)
	known += "c"
	findLetter(line, mapping, reverseMapping, 'a', known, 3)
	known += "b"
	findLetter(line, mapping, reverseMapping, 'd', known, 4)
	known += "ade"
	findLetter(line, mapping, reverseMapping, 'g', known, 7)
	return reverseMapping
}

func solve(fn string, part int) int {
	var ret int
	file, err := os.Open(fn)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := strings.Split(scanner.Text(), "|")
		if part == 1 {
			ret += countUnique(strings.Split(strings.TrimSpace(line[1]), " "))
		} else if part == 2 {
			letterMapping := decodeLetters(strings.Split(strings.TrimSpace(line[0]), " "))
			ret += decodeSignal(strings.Split(strings.TrimSpace(line[1]), " "), letterMapping)
		}
	}
	return ret
}

func main() {
	fn := "input.txt"
	// part 1
	fmt.Println(solve(fn, 1))
	// part 2
	fmt.Println(solve(fn, 2))
}
