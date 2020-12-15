import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashMap;
import java.util.Scanner;

public class Day15 {

    private static int get_nth_number(int n, HashMap<Integer, Integer> spoken_numbers) {
        int turn = spoken_numbers.size() + 1, new_number = 0;
        while (turn < n) {
            if (!spoken_numbers.containsKey(new_number)) {
                spoken_numbers.put(new_number, turn);
                new_number = 0;
            } else {
                int diff = turn - spoken_numbers.get(new_number);
                spoken_numbers.put(new_number, turn);
                new_number = diff;
            }
            turn++;
        }
        return new_number;
    }

    public static HashMap<Integer, Integer> read_numbers(String input ) throws FileNotFoundException {
        HashMap<Integer, Integer> spoken_numbers = new HashMap<>();
        Scanner scanner = new Scanner(new File(input));
        String[] line = scanner.nextLine().split(",");
        int turn = 1, new_number = -1;
        for (String number : line) {
            new_number = Integer.parseInt(number);
            spoken_numbers.put(new_number, turn);
            turn++;
        }
        return spoken_numbers;
    }

    public static void main(String[] args) {
        String input = "input15.txt";
        try {
            System.out.println(get_nth_number(2020, read_numbers(input)));
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        try {
            System.out.println(get_nth_number(30000000, read_numbers(input)));
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }
}
