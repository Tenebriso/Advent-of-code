import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Day6 {

    private static Set<Character> get_group_answers(Scanner scanner) {
        Set<Character> group_answers = new HashSet<Character>();
        String current_line = scanner.nextLine();
        while (!current_line.trim().isEmpty() && scanner.hasNextLine()) {
            for (int i = 0; i < current_line.length(); i++)
                group_answers.add(current_line.charAt(i));
            current_line = scanner.nextLine();
        }
        if (!current_line.isEmpty()) {
            for (int i = 0; i < current_line.length(); i++)
                group_answers.add(current_line.charAt(i));
        }
        return group_answers;
    }

    public static int part1(String input) throws FileNotFoundException {
        int count = 0;
        Scanner scanner = new Scanner(new File(input));
        while (scanner.hasNextLine()) {
            count += get_group_answers(scanner).size();
        }
        return count;
    }

    private static int group_common_answers(Scanner scanner) {
        Set<Character> common_answers = new HashSet<Character>();
        String current_line = scanner.nextLine();
        int step = 0;
        while (!current_line.trim().isEmpty() && scanner.hasNextLine()) {
            Set<Character> group_answers = new HashSet<Character>();
            for (int i = 0; i < current_line.length(); i++)
                group_answers.add(current_line.charAt(i));
            if (step == 0)
                common_answers.addAll(group_answers);
            else
                common_answers.retainAll(group_answers);
            current_line = scanner.nextLine();
            step++;
        }
        if (!current_line.isEmpty()) {
            Set<Character> group_answers = new HashSet<Character>();
            for (int i = 0; i < current_line.length(); i++)
                group_answers.add(current_line.charAt(i));
            if (step == 0)
                common_answers.addAll(group_answers);
            else
                common_answers.retainAll(group_answers);
        }

        return common_answers.size();
    }

    public static int part2(String input) throws FileNotFoundException {
        int count = 0;
        Scanner scanner = new Scanner(new File(input));
        while (scanner.hasNextLine()) {
            count += group_common_answers(scanner);
        }
        return count;
    }

    public static void main(String[] args) {
        String input = "input6.txt";
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
