import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;

public class Day14 {

    private static long setKthBit(long n, long k) {
        return ((1L << k) | n);
    }

    private static long clerKthBit(long n, long k) {
        return (~(1L << k) & n);
    }

    private static long sum_values(HashMap<Long, Long> pos_to_nb) {
        long sum = 0;
        for (long pos : pos_to_nb.keySet())
            sum += pos_to_nb.get(pos);
        return sum;
    }

    private static Long apply_mask(String mask, Long nb) {
        for (int i = mask.length() - 1; i >= 0; i--) {
            if (mask.charAt(i) == 'X')
                continue;
            else if (mask.charAt(i) == '0')
                    nb = clerKthBit(nb, mask.length() - 1 - i);
            else
                    nb = setKthBit(nb, mask.length() - 1 - i);
        }
        return nb;
    }

    private static long part1(String input) throws FileNotFoundException {
        Scanner scanner = new Scanner(new File(input));
        String[] line;
        HashMap<Long, Long> pos_to_nb = new HashMap<>();
        String mask = null;
        while (scanner.hasNextLine()) {
            line = scanner.nextLine().split("=");
            if (line[0].trim().equals("mask")) {
                mask = line[1].trim();
            } else {
                Long pos = Long.parseLong(line[0].replaceAll("[^0-9?!\\.]",""));
                Long nb = Long.parseLong(line[1].trim());
                pos_to_nb.put(pos, apply_mask(mask, nb));
            }
        }
        return sum_values(pos_to_nb);
    }

    private static String get_floating_mask(String mask, Long pos) {
        StringBuilder pos_mask = new StringBuilder();
        for (int i = mask.length()-1; i >= 0; i--)
            if (mask.charAt(i) == '0') {
                pos_mask.insert(0, (pos >> (mask.length() - 1 - i)) & 1);
            }
            else {
                pos_mask.insert(0, mask.charAt(i));
        }
        return pos_mask.toString();
    }

    private static ArrayList<String> generate_all_masks(String mask) {
        ArrayList<String> masks = new ArrayList<>();
        int i = mask.indexOf('X');
        if (i == -1) {
            masks.add(mask);
        } else {
            masks.addAll(generate_all_masks(mask.substring(0, i) + '0' + mask.substring(i + 1)));
            masks.addAll(generate_all_masks(mask.substring(0, i) + '1' + mask.substring(i + 1)));
        }
        return masks;
    }

    private static long part2(String input)throws FileNotFoundException {
        Scanner scanner = new Scanner(new File(input));
        String[] line;
        HashMap<Long, Long> pos_to_nb = new HashMap<>();
        ArrayList<String> masks = null;
        String mask = null;
        while (scanner.hasNextLine()) {
            line = scanner.nextLine().split("=");
            if (line[0].trim().equals("mask")) {
                mask = line[1].trim();

            } else {
                Long pos = Long.parseLong(line[0].replaceAll("[^0-9?!\\.]",""));
                Long nb = Long.parseLong(line[1].trim());
                masks = generate_all_masks(get_floating_mask(mask, pos));
                for (String pos_mask : masks)
                    pos_to_nb.put(apply_mask(pos_mask, pos), nb);
            }
        }
        return sum_values(pos_to_nb);
    }


    public static void main(String[] args) {
        String input = "input14.txt";
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
