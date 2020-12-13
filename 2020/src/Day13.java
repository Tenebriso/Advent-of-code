import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Day13 {

    private static int current;

    private static int[] read_buses(String input) throws FileNotFoundException {
        Scanner scanner = new Scanner(new File(input));
        current = Integer.parseInt(scanner.nextLine());
        String[] buses = scanner.nextLine().split(",");
        int[] buses_id = new int[buses.length];
        for (int i = 0; i < buses.length; i++) {
            int bus;
            try {
                bus = Integer.parseInt(buses[i]);
            } catch (NumberFormatException e) {
                bus = 0;
            }
            buses_id[i] = bus;
        }
        return buses_id;
    }

    private static int to_wait(int current, int bus) {
        return bus - current % bus;
    }

    public static int part1(String input) throws FileNotFoundException {
        int[] buses = read_buses(input);
        int min = current, bus_id = 0;
        for (int bus : buses) {
                if (bus == 0)
                    continue;
                int bus_wait = to_wait(current, bus);
                if (bus_wait < min) {
                    min = bus_wait;
                    bus_id = bus;
                }
        }
        return bus_id * to_wait(current, bus_id);
    }

    public static long part2(String input) throws FileNotFoundException {
        int[] buses = read_buses(input);
        long lcm = 1, timestamp = 0;
        for (int i = 0; i < buses.length; i++) {
            if (buses[i] == 0)
                continue;
            while ((timestamp + i) % buses[i] != 0) {
                timestamp += lcm;
            }
            lcm *= buses[i];
        }
        return timestamp;
    }

    public static void main(String[] args) {
        String input = "input13.txt";
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
