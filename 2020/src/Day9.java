import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class Day9 {

    int preamble;
    LinkedHashMap<Long, Boolean> cache;
    String input;
    ArrayList<Long> numbers;

    public Day9(int preamble, String input) {
        this.preamble = preamble;
        this.cache = new LinkedHashMap<>(preamble){private static final int MAX_ENTRIES = 25;
        protected boolean removeEldestEntry(Map.Entry eldest) {
            return size() > MAX_ENTRIES;
        }};
        this.input = input;
        this.numbers = new ArrayList<>();
    }

    private boolean can_add(long number) {
        for (long check : this.cache.keySet()) {
            if (this.cache.get(number - check) != null)
                return true;
        }
        return false;
    }

    private boolean add(long number) {
        // preamble
        if (cache.size() < preamble) {
            cache.put(number, true);
            numbers.add(number);
            return true;
        }
        // non-preamble
        if (can_add(number)) {
            if (cache.get(number) != null)
                cache.remove(number);
            cache.put(number, true);
            numbers.add(number);
            return true;
        }
        return false;
    }

    public long find_invalid() throws FileNotFoundException {
        Scanner scanner = new Scanner(new File(input));
        while (scanner.hasNextLong()) {
            long next = scanner.nextLong();
            if (!add(next))
                return next;
        }
        return -1;
    }

    private long find_sum(long number) {
        for (int i = 0; i < numbers.size() - 1; i++) {
            long sum = numbers.get(i);
            for (int j = i + 1; j < numbers.size(); j++) {
                if (sum == number) {
                    List<Long> sublist = numbers.subList(i, j);
                    return Collections.min(sublist) + Collections.max(sublist);
                }
                else if (sum < number)
                    sum += numbers.get(j);
                else
                    break;
            }
        }
        return -1;
    }

    public static long part1(String input, int preamble) throws FileNotFoundException {
        Day9 day9 = new Day9(preamble, input);
        return day9.find_invalid();
    }

    public static long part2(String input, int preamble) throws FileNotFoundException {
        Day9 day9 = new Day9(preamble, input);
        long invalid = day9.find_invalid();
        return day9.find_sum(invalid);
    }

    public static void main(String[] args) {
        String input = "input9.txt";
        try {
            System.out.println(part1(input, 25));
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        try {
            System.out.println(part2(input, 25));
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }
}
