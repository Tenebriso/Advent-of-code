import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Scanner;

class Interval {
    public int a;
    public int b;

    public Interval(int a, int b) {
        this.a = a;
        this.b = b;
    }

    public Interval intersection(Interval other) {
        Interval inter = new Interval(Math.min(other.a, a), Math.max(other.b, b));
        // included
        if ((other.a >= a && other.b <= b) ||
                (other.a <= a && other.b >= b))
            return inter;
        // overlap
        if ((other.b >= a && other.b <= b) ||
                (b >= other.a && b <= other.b))
            return inter;
        // continue
        if (a - other.b == 1 || other.a - b == 1)
            return inter;
        return null;
    }

    public boolean in_interval(int n) {
        return (n >= a && n <= b);
    }

    public String toString() {
        return a + "-" + b;
    }
}

public class Day16 {

    private static HashMap<String, ArrayList<Interval>> read_rules(Scanner scanner) {
        String line = scanner.nextLine().trim();
        HashMap<String, ArrayList<Interval>> intervals = new HashMap<>();
        do {
            String[] fields = line.split(" ");
            String field_name = line.split(":")[0];
            intervals.put(field_name, new ArrayList<Interval>());
            Interval other_interval = new Interval(
                    Integer.parseInt(fields[fields.length - 1].trim().split("-")[0]),
                    Integer.parseInt(fields[fields.length - 1].trim().split("-")[1]));
            intervals.get(field_name).add(other_interval);
            other_interval = new Interval(
                    Integer.parseInt(fields[fields.length - 3].trim().split("-")[0]),
                    Integer.parseInt(fields[fields.length - 3].trim().split("-")[1]));
            intervals.get(field_name).add(other_interval);
            line = scanner.nextLine().trim();
        } while (!line.isEmpty() && scanner.hasNextLine());
        return intervals;
    }

    public static ArrayList<Interval> combine_rules(ArrayList<Interval> intervals) {
        int n = intervals.size();
        boolean ok;
        do {
            ok = false;
            for (int i = 0; i < n; i++) {
                for (int j = n - 1; j > i; j--) {
                    Interval intersection = intervals.get(i).intersection(intervals.get(j));
                    if (intersection != null) {
                        n--;
                        intervals.set(i, intersection);
                        ok = true;
                    }
                }
            }
        } while (ok);
        return new ArrayList<Interval>(intervals.subList(0, n));
    }

    private static int[] read_your_ticket(Scanner scanner) {
        scanner.nextLine();
        String[] fields = scanner.nextLine().trim().split(",");
        int[] numbers = new int[fields.length];
        for (int i = 0; i < fields.length; i++)
            numbers[i] = Integer.parseInt(fields[i]);
        scanner.nextLine();
        return numbers;
    }

    private static boolean number_is_valid(int number, ArrayList<Interval> intervals) {
        for (Interval interval : intervals) {
            if (interval.in_interval(number))
                return true;
        }
        return false;
    }

    public static int part1(String input) throws FileNotFoundException {
        Scanner scanner = new Scanner(new File(input));
        int sum = 0;
        ArrayList<Interval> intervals = new ArrayList<>();
        for (ArrayList<Interval> interval : read_rules(scanner).values()) {
            intervals.addAll(interval);
        }
        intervals = combine_rules(intervals);
        read_your_ticket(scanner);
        scanner.nextLine();
        while (scanner.hasNextLine()) {
            String[] line = scanner.nextLine().trim().split(",");
            for (String i : line) {
                int number = Integer.parseInt(i);
                if (!number_is_valid(number, intervals))
                        sum += number;
                }
        }
        return sum;
    }

    private static boolean ticket_is_valid(String[] line, HashMap<String, ArrayList<Interval>> rules) {
        ArrayList<Interval> intervals = new ArrayList<>();
        for (ArrayList<Interval> interval : rules.values()) {
            intervals.addAll(interval);
        }
        for (String i: line) {
            if (!number_is_valid(Integer.parseInt(i), intervals))
                return false;
        }
        return true;
    }

    private static HashMap<Integer, HashSet<String>> read_first_ticket(Scanner scanner, HashMap<String, ArrayList<Interval>> rules) {
        String[] line = scanner.nextLine().trim().split(",");
        HashMap<Integer, HashSet<String>> pos_to_rules = new HashMap<>();
        // first valid ticket
        while (!ticket_is_valid(line, rules))
            line = scanner.nextLine().trim().split(",");
        for (int i = 0; i < line.length; i++) {
            int number = Integer.parseInt(line[i]);
            for (String rule : rules.keySet()) {
                if (number_is_valid(number, rules.get(rule))) {
                    if (!pos_to_rules.containsKey(i))
                        pos_to_rules.put(i, new HashSet<>());
                    pos_to_rules.get(i).add(rule);
                }
            }
        }
        return pos_to_rules;
    }

    private static HashMap<Integer, HashSet<String>> intersect_fields(HashMap<Integer, HashSet<String>> pos_to_rules) {
        HashSet<Integer> seen = new HashSet<>();
        do {
            HashMap<Integer, HashSet<String>> rules_to_remove = new HashMap<>();
            for (Integer pos : pos_to_rules.keySet()) {
                if (pos_to_rules.get(pos).size() == 1 && !seen.contains(pos)) {
                    seen.add(pos);
                    for (int j = 0; j < pos_to_rules.size(); j++)
                        if (j != pos) {
                            if (!rules_to_remove.containsKey(j))
                                rules_to_remove.put(j, new HashSet<>());
                            rules_to_remove.get(j).addAll(pos_to_rules.get(pos));
                        }
                }
            }
            // for each field, remove rules used by other fields
            for (Integer pos: rules_to_remove.keySet()) {
                if (rules_to_remove.get(pos).size() == 0)
                    continue;
                pos_to_rules.get(pos).removeAll(rules_to_remove.get(pos));
            }
        } while (seen.size() < pos_to_rules.size());
        return pos_to_rules;
    }

    private static HashMap<Integer, HashSet<String>> removable_fields(String[] line, HashMap<Integer,
            HashSet<String>> pos_to_rules, HashMap<String, ArrayList<Interval>> rules) {
        HashMap<Integer, HashSet<String>> rules_to_remove = new HashMap<>();
        for (int i = 0; i < line.length; i++) {
            rules_to_remove.put(i, new HashSet<>());
            int number = Integer.parseInt(line[i]);
            for (String rule : pos_to_rules.get(i)) {
                if (!number_is_valid(number, rules.get(rule))) {
                    rules_to_remove.get(i).add(rule);
                }
            }
        }
        return rules_to_remove;
    }

    private static long prod_departure(HashMap<Integer, HashSet<String>> pos_to_rules, int[] my_ticket) {
        long prod = 1;
        for (Integer pos : pos_to_rules.keySet()) {
            for (String rule : pos_to_rules.get(pos)) {
                if (rule.startsWith("departure"))
                    prod *= my_ticket[pos];
            }
        }
        return prod;
    }

    public static long part2(String input) throws FileNotFoundException {
        // read rules
        Scanner scanner = new Scanner(new File(input));
        HashMap<String, ArrayList<Interval>> rules = read_rules(scanner);
        // read my ticket
        int[] my_ticket = read_your_ticket(scanner);
        // read newline
        scanner.nextLine();
        // read the first ticket
        HashMap<Integer, HashSet<String>> pos_to_rules = read_first_ticket(scanner, rules);
        // read the rest of the tickets
        while (scanner.hasNextLine()) {
            String[] line = scanner.nextLine().trim().split(",");
            if (!ticket_is_valid(line, rules))
                continue;
            HashMap<Integer, HashSet<String>> rules_to_remove = removable_fields(line, pos_to_rules, rules);
            for (Integer pos : rules_to_remove.keySet())
                    pos_to_rules.get(pos).removeAll(rules_to_remove.get(pos));
        }
        // intersect tickets' fields
        pos_to_rules = intersect_fields(pos_to_rules);

        return prod_departure(pos_to_rules, my_ticket);
    }

    public static void main(String[] args) {
        String input = "input16.txt";
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
