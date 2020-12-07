import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class Day7 {

    private static HashMap<String, ArrayList<String>> get_bags(String input) throws FileNotFoundException {
        Scanner scanner = new Scanner(new File(input));
        HashMap<String, ArrayList<String>> bags = new HashMap<>();
        Set<String> seen = new HashSet<String>();
        while (scanner.hasNextLine()) {
            String[] line = scanner.nextLine().split("contain");
            String parent = line[0].split(" ")[0] + " " + line[0].split(" ")[1];
            if (line[1].contains("no")) {
                continue;
            }
            String[] children = line[1].split(",");
            for (String child : children) {
                String node = child.trim().split(" ")[1] + " " + child.trim().split(" ")[2];
                if (!bags.containsKey(node)) {
                    bags.put(node, new ArrayList<String>());
                }
                bags.get(node).add(parent);
            }
        }
        return bags;
    }

    private static int depth(HashMap<String, ArrayList<String>> bags, String node) {
        int depth = 0;
        ArrayList<String> queue = new ArrayList<>();
        Set<String> seen = new HashSet<>();
        seen.add(node);
        queue.add(node);
        while (!queue.isEmpty()) {
            node = queue.remove(0);
            // no bags can contain this bag
            if (!bags.containsKey(node)) {
                continue;
            }
            // count all the bags that can contain this bag that we haven't counted already
            for (String neighbor : bags.get(node)) {
                if (!seen.contains(neighbor)) {
                    depth += 1;
                    queue.add(neighbor);
                    seen.add(neighbor);
                }
            }
        }
        return depth;
    }

    public static int part1(String input) throws FileNotFoundException {
        return depth(get_bags(input), "shiny gold");
    }

    public static int part2(String input) throws FileNotFoundException {
        return count_bags(get_all_bags(input), "shiny gold") - 1;
    }

    private static HashMap<String, HashMap<String, Integer>> get_all_bags(String input) throws FileNotFoundException {
        Scanner scanner = new Scanner(new File(input));
        HashMap<String, HashMap<String, Integer>> bags = new HashMap<>();
        Set<String> seen = new HashSet<String>();
        while (scanner.hasNextLine()) {
            String[] line = scanner.nextLine().split("contain");
            String parent = line[0].split(" ")[0] + " " + line[0].split(" ")[1];
            bags.put(parent, new HashMap<>());
            if (line[1].contains("no")) {
                continue;
            }
            String[] children = line[1].split(",");
            for (String child : children) {
                String node = child.trim().split(" ")[1] + " " + child.trim().split(" ")[2];
                bags.get(parent).put(node, Integer.parseInt(child.trim().split(" ")[0]));
            }
        }
        return bags;
    }

    private static int count_bags(HashMap<String, HashMap<String, Integer>> bags, String node) {
        if (bags.get(node).isEmpty())
            return 1;
        int total = 1;
        for (String child : bags.get(node).keySet()) {
            total += bags.get(node).get(child) * count_bags(bags, child);
        }
        return total;
    }

    public static void main(String[] args) {
        String input = "input7.txt";
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
