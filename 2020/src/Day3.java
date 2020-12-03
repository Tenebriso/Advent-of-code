import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

class Move {
    int i;
    int j;
    public Move(int i, int j) {
        this.i = i;
        this.j = j;
    }
}

public class Day3 {
    public static int part1(String input, int move_i, int move_j) throws FileNotFoundException {
        int i = 0, trees_count = 0, j = 0;
        Scanner scanner = new Scanner(new File(input));
        // I start from the first line
        scanner.nextLine();
        while (scanner.hasNextLine()) {
            String line;
            // move down move_j number of lines
            do {
                line = scanner.nextLine();
                j++;
            } while (j % move_j != 0 && scanner.hasNextLine());
            // move to the right
            i += move_i;
            if (line.charAt(i % line.length()) == '#') {
                trees_count += 1;
            }
        }
        return trees_count;
    }
    private static Move[] get_moves() {
        Move[] moves = new Move[5];
        moves[0] = new Move(1, 1);
        moves[1] = new Move(3, 1);
        moves[2] = new Move(5, 1);
        moves[3] = new Move(7, 1);
        moves[4] = new Move(1, 2);
        return moves;
    }

    public static long part2(String input, Move[] moves) throws FileNotFoundException {
        long prod = 1;
        for (Move move : moves) {
            int sum = part1(input, move.i, move.j);
            System.out.format("For %d, %d sum = %d\n", move.i, move.j, sum);
            prod *= sum;
        }
        return prod;
    }

    public static void main(String[] args) {
        String input = "input3.txt";
        try {
            System.out.println(part1(input, 3, 1));
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }

        try {
            System.out.println(part2(input, get_moves()));
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }
}
