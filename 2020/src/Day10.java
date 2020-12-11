import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class Day10 {

    private static PriorityQueue<Integer> read_input(String input) throws FileNotFoundException {
        PriorityQueue<Integer> numbers = new PriorityQueue<>();
        Scanner scanner = new Scanner(new File(input));
        while (scanner.hasNextInt())
            numbers.add(scanner.nextInt());
        return numbers;
    }

    private static HashMap<Integer, Integer> build_differences(PriorityQueue<Integer> numbers) {
        HashMap<Integer, Integer> differences = new HashMap<>();
        int number, difference, current = 0;
        while (!numbers.isEmpty()) {
            number = numbers.poll();
            difference = number - current;
            if (difference > 3)
                return null;
            if (!differences.containsKey(difference))
                differences.put(difference, 1);
            else
                differences.put(difference, differences.get(difference) + 1);
            current = number;
        }
        // add your adapter
        if (!differences.containsKey(3))
            differences.put(3, 1);
        else
            differences.put(3, differences.get(3) + 1);
        return differences;
    }

    private static long all_combinations(PriorityQueue<Integer> numbers) {
        LinkedHashMap<Integer, Long> all_paths = new LinkedHashMap<>();
        int max = Collections.max(numbers) + 3;
        numbers.add(max);
        all_paths.put(0, Long.valueOf(1));
        while (!numbers.isEmpty())
            all_paths.put(numbers.poll(), Long.valueOf(0));
        for (int number : all_paths.keySet()) {
            for (int i = 1; i <= 3; i++) {
                int possible_neighbor = number + i;
                if (all_paths.containsKey(possible_neighbor))
                    all_paths.put(possible_neighbor, all_paths.get(number) + all_paths.get(possible_neighbor));
            }
        }
        return all_paths.get(max);
    }

    public static int part1(String input) throws FileNotFoundException {
        PriorityQueue<Integer> numbers = read_input(input);
        HashMap<Integer, Integer> differences = build_differences(numbers);
        return differences.get(1) * differences.get(3);
    }

    public static long part2(String input) throws FileNotFoundException {
        PriorityQueue<Integer> numbers = read_input(input);
        return all_combinations(numbers);
    }

    public static void main(String[] args) {
        String input = "input10.txt";
        try {
            System.out.println(part1(input));
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        try {
            System.out.println(part2(input));
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }
}
