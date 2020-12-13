import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

import static java.util.Map.entry;

class Navigation {
    private char direction;
    private Map<Character, Integer> direction_to_degrees;
    private Map<Integer, Character> degrees_to_direction;
    public Map<Integer, Integer> position;

    public Navigation() {
        direction = 'E';
        position = new HashMap<>() {{
            put(0, 0);
            put(90, 0);
            put(180, 0);
            put(270, 0);
        }};
        direction_to_degrees = Map.ofEntries(entry('E', 0), entry('N', 90),
                entry('W', 180), entry('S', 270));
        degrees_to_direction = new HashMap<>();
        for (Map.Entry<Character, Integer> entry : direction_to_degrees.entrySet())
            degrees_to_direction.put(entry.getValue(), entry.getKey());
    }

    public void move(String instruction) {
        int distance = Integer.parseInt(instruction.substring(1));
        int new_degrees, opposite_direction;
        switch (instruction.charAt(0)) {
            case 'R':
                new_degrees = (direction_to_degrees.get(direction) + 360 - distance) % 360;
                direction = degrees_to_direction.get(new_degrees);
                break;
            case 'L':
                new_degrees = (direction_to_degrees.get(direction) + distance) % 360;
                direction = degrees_to_direction.get(new_degrees);
                break;
            default:
                // F or ENWS
                if (!direction_to_degrees.containsKey(instruction.charAt(0)))
                    new_degrees = direction_to_degrees.get(direction);
                else
                    new_degrees = direction_to_degrees.get(instruction.charAt(0));
                opposite_direction = (new_degrees + 180) % 360;
                distance -= position.get(opposite_direction);
                if (distance >= 0) {
                    position.put(new_degrees, position.get(new_degrees) + distance);
                    position.put(opposite_direction, 0);
                } else {
                    position.put(opposite_direction, Math.abs(distance));
                    position.put(new_degrees, 0);
                }
        }
    }
}

public class Day12 {

    private static int part1(String input) throws FileNotFoundException {
        Scanner scanner = new Scanner(new File(input));
        Navigation navi = new Navigation();
        int sum = 0;
        while (scanner.hasNextLine())
            navi.move(scanner.nextLine());
        for (int key : navi.position.keySet())
            sum += navi.position.get(key);
        return sum;
    }

    public static void main(String[] args) {
        String input = "input12.txt";
        try {
            System.out.println(part1(input));
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }
}
