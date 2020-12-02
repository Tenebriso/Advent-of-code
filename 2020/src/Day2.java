import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

class Password {
    int min;
    int max;
    char c;
    String password;

    public Password(int min, int max, char c, String password) {
        this.min = min;
        this.max = max;
        this.c = c;
        this.password = password;
    }

    private int countOccurances() {
        int count = 0;
        for (int i = 0; i < password.length(); i++)
            if (password.charAt(i) == c) count++;
        return count;
    }

    public boolean isValid() {
        int occurences = countOccurances();
        if (occurences >= min && occurences <= max) {
            return true;
        }
        return false;
    }

    public boolean isValidNew() {
        // only first pos
        if (password.charAt(min - 1) == this.c &&
            password.charAt(max - 1) != this.c) {
            return true;
        // only second pos
        } else if (password.charAt(min - 1) != this.c &&
                password.charAt(max - 1) == this.c) {
            return true;
        }
        return false;
    }
}

public class Day2 {

    private static Password parse_line(String line) {
        String[] split = line.split(" ");
        String[] numbers = split[0].split("-");
        int min = Integer.parseInt(numbers[0]);
        int max = Integer.parseInt(numbers[1]);
        char c = split[1].charAt(0);
        String password = split[2];
        return new Password(min, max, c, password);
    }

    public static int part1(String input) throws FileNotFoundException {
        Scanner scanner = new Scanner(new File(input));
        int count = 0;
        while (scanner.hasNextLine()) {
            String current_line = scanner.nextLine();
            Password current_pass = parse_line(current_line);
            if (current_pass.isValid()) {
                count++;
            }
        }
        return count;
    }

    public static int part2(String input) throws FileNotFoundException {
        Scanner scanner = new Scanner(new File(input));
        int count = 0;
        while (scanner.hasNextLine()) {
            String current_line = scanner.nextLine();
            Password current_pass = parse_line(current_line);
            if (current_pass.isValidNew()) {
                count++;
            }
        }
        return count;
    }

    public static void main(String[] args) {
        String input = "input2.txt";
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
