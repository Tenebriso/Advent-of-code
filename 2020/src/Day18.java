import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class Day18 {

    private static int get_paranthesis(int index, String line) {
        String chars = "";
        ArrayList<Character> paranthesis = new ArrayList<>();
        paranthesis.add(line.charAt(index));
        for (int i = index; i < line.length(); i++) {
            if (line.charAt(i) == '(')
                paranthesis.add('(');
            else if (line.charAt(i) == ')')
                paranthesis.remove(paranthesis.size() - 1);
            else
                chars += line.charAt(i);
            if (paranthesis.isEmpty())
                return i;
        }
        return chars;
    }

    private static int calculate_op(String line) {
        int i;
        for (i = 0; i < line.length(); i++) {
            int digit1, digit2;
            char op;
            if (line.charAt(i) == '(') {

            }
        }
        return 0;
    }

    public static int part1(String input) throws FileNotFoundException {
        Scanner scanner = new Scanner(new File(input));
        int sum = 0;
        while (scanner.hasNextLine()) {
            String line = scanner.nextLine();
            sum += calculate_op(line);
        }

        return sum;
    }

    public static void main(String args[]) {
        String input = "input18.txt";

    }
}
