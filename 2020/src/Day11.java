import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class Day11 {

    private static boolean changed = true;
    private static int occupied = 0;


    private static ArrayList<ArrayList<Character>> get_sits(String input) throws FileNotFoundException {
        Scanner scanner = new Scanner(new File(input));
        ArrayList<ArrayList<Character>> sits = new ArrayList<>();
        while (scanner.hasNextLine()) {
            String line = scanner.nextLine();
            sits.add(new ArrayList<>());
            for (int j = 0; j < line.length(); j++)
                sits.get(sits.size() - 1).add(line.charAt(j));
        }
        return sits;
    }

    private static int is_occupied(int i, int j, ArrayList<ArrayList<Character>> sits) {
        if (sits.get(i).get(j)  == '.' || sits.get(i).get(j) == 'L')
            return 0;
        return 1;
    }

    private static int count_occupied_neighbors(int i, int j, ArrayList<ArrayList<Character>> sits) {
        int occupied = 0;
        if (i < sits.size() - 1) {
            occupied += is_occupied(i + 1, j, sits);
            if (j < sits.get(i).size() - 1) {
                occupied += is_occupied(i + 1, j + 1, sits);
            }
            if (j > 0){
                occupied += is_occupied(i + 1, j - 1, sits);
            }
        }
        if (i > 0){
            occupied += is_occupied(i - 1, j, sits);
            if (j < sits.get(i).size() - 1) {
                occupied += is_occupied(i - 1, j + 1, sits);
            }
            if (j > 0) {
                occupied += is_occupied(i - 1, j - 1, sits);
            }
        }
        if (j > 0)
            occupied += is_occupied(i, j - 1, sits);
        if (j < sits.get(i).size() - 1)
            occupied += is_occupied(i, j + 1, sits);
        return occupied;
    }

    private static char new_status(int i, int j, ArrayList<ArrayList<Character>> sits) {
        if (sits.get(i).get(j) == '.')
            return '.';
        int occupied = count_occupied_neighbors(i, j, sits);
        if (sits.get(i).get(j) == 'L') {
            if (occupied == 0)
                return '#';
            else
                return 'L';
        }
        if (occupied >= 4)
            return 'L';
        return '#';
    }

    private static ArrayList<ArrayList<Character>> move(ArrayList<ArrayList<Character>> sits) {
        ArrayList<ArrayList<Character>> new_sits = new ArrayList<>();
        for (int i = 0; i < sits.size(); i++) {
            new_sits.add(new ArrayList<>());
            for (int j = 0; j < sits.get(0).size(); j++) {
                new_sits.get(i).add(new_status(i, j, sits));
                if (sits.get(i).get(j) != new_sits.get(i).get(j))
                    changed = true;
                if (new_sits.get(i).get(j) == '#')
                    occupied++;
            }
        }
        return new_sits;
    }

    public static int part1(String input) throws FileNotFoundException {
        ArrayList<ArrayList<Character>> sits = get_sits(input);
        ArrayList<ArrayList<Character>> new_moves = null;
        int i = 0;
        do {
            changed = false;
            occupied = 0;
            if (i % 2 == 1) {
                sits = move(new_moves);
            } else {
                new_moves = move(sits);
            }
            i++;
        } while (changed);
        return occupied;
    }

    public static void main(String[] args) {
        String input = "input11.txt";
        try {
            System.out.println(part1(input));
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }
}
