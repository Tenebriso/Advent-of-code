import java.io.FileNotFoundException;
import java.util.HashSet;
import java.util.Scanner;
import java.io.File;

public class Day1 {
    public static int part1(String input) throws FileNotFoundException {
        HashSet<Integer> numbers = new HashSet<Integer>();
        Scanner scanner = new Scanner(new File(input));
        while (scanner.hasNextInt()) {
            int current_number = scanner.nextInt();
            if (numbers.contains(2020 - current_number)) {
                return current_number * (2020 - current_number);
            } else {
                numbers.add(current_number);
            }
        }
        return -1;
    }

    public static int two_sum(HashSet<Integer> numbers, int sum) {
        for (int current_number: numbers) {
            if (numbers.contains(sum - current_number)) {
                return current_number * (sum - current_number);
            }
        }
        return -1;
    }

    public static HashSet<Integer> read_numbers(String input) throws FileNotFoundException {
        HashSet<Integer> numbers = new HashSet<Integer>();
        Scanner scanner = new Scanner(new File(input));
        while (scanner.hasNextInt()) {
            numbers.add(scanner.nextInt());
        }
        return numbers;
    }

    public static int part2(String input) throws FileNotFoundException {
        HashSet<Integer> numbers = read_numbers(input);
        for (int x : numbers) {
            int partial_sum = two_sum(numbers, 2020- x);
            if (partial_sum != -1) {
                return partial_sum * x;
            }
        }
        return -1;
    }


    public static void main(String[] args) {
        String input = "input1.txt";
        // part 1
        try {
            System.out.println(part1(input));
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        // part 2
        try {
            System.out.println(part2(input));
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }
}
