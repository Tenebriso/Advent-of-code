import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.Scanner;

public class Day5 {

    private static int get_place(String seat_code) {
        int l = 0, r = (1 << seat_code.length()) - 1;
        for (int i = 0; i < seat_code.length(); i++) {
            if (seat_code.charAt(i) == 'F' || seat_code.charAt(i) == 'L')
                r = (r + l) / 2;
            else
                l = (r + l) / 2 + 1;
        }
        return l;
    }

    public static int part1(String input) throws FileNotFoundException {
        int max = 0;
        Scanner scanner = new Scanner(new File(input));
        while (scanner.hasNextLine()) {
            String line = scanner.nextLine();
            int seat_id = get_place(line.substring(0, 7)) * 8 + get_place(line.substring(7));
            if (max < seat_id) {
                max = seat_id;
            }
        }
        return max;
    }

    public static int part2(String input) throws FileNotFoundException {
        Scanner scanner = new Scanner(new File(input));
        ArrayList<Integer> seats = new ArrayList<>();
        while (scanner.hasNextLine()) {
            String line = scanner.nextLine();
            int seat_id = get_place(line.substring(0, 7)) * 8 + get_place(line.substring(7));
            seats.add(seat_id);
        }
        seats.sort(Comparator.naturalOrder());
        for (int i = 0; i < seats.size() - 1; i++) {
            for (int j = i + 1; j < seats.size(); j++) {
                if (seats.get(j) - seats.get(i) == 2 && !seats.contains(seats.get(i) + 1))
                    return seats.get(i) + 1;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        String input = "input5.txt";
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