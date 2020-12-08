import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Scanner;

public class Day8 {
    int acc;
    int current_i;
    HashSet<Integer> seen;
    ArrayList<String> ops;

    public Day8() {
        acc = 0;
        seen = new HashSet<>();
        current_i = -1;
        ops = new ArrayList<String>();
    }

    private void read_input(Scanner scanner) {
        String line = null;
        line = scanner.nextLine();
        ops.add(line);
        current_i++;
    }

    private int exec_op(Scanner scanner) {
        // sanity check
        if (ops.isEmpty()) {
            read_input(scanner);
        }
        // operation to execute is at index current_i in ops
        String[] op = ops.get(current_i).trim().split(" ");
        // found loop
        if (this.seen.contains(current_i)) {
            return this.acc;
        }
        this.seen.add(current_i);
        // acc
        if (op[0].equals("acc")) {
            this.acc += Integer.parseInt(op[1]);
        }
        if (op[0].equals("jmp")) {
            // jmp +: move current_i and read new input if necessary
            if (Integer.parseInt(op[1]) > 0) {
                int jump = Integer.parseInt(op[1]);
                for (int i = 0; i < jump; i++) {
                    if (current_i + 1 >= ops.size()) {
                        if (!scanner.hasNextLine())
                            return this.acc;
                        read_input(scanner);
                    } else {
                        current_i += 1;
                    }
                }
            // jmp -: move current_i
            } else {
                current_i += Integer.parseInt(op[1]);
            }
            return exec_op(scanner);
        }
        // move to the next instruction or read the next one if any left
        if (current_i + 1 < ops.size()) {
            current_i++;
        } else {
            if (!scanner.hasNextLine())
                return acc;
            read_input(scanner);
        }
        return exec_op(scanner);
    }

    public static int part1(String input) throws FileNotFoundException {
        Day8 day8 = new Day8();
        return day8.exec_op(new Scanner(new File(input)));
    }

    public static int part2(String input) throws FileNotFoundException {
        Day8 day8 = new Day8();
        Scanner scanner = new Scanner(new File(input));
        // first run is looping, populate seen & ops
        int i = day8.exec_op(scanner);
        int current_op = 0;
        ArrayList<String> aux = (ArrayList<String>) day8.ops.clone();
        while (scanner.hasNextLine() && current_op < day8.ops.size()) {
            // reset vars
            day8 = new Day8();
            day8.current_i = 0;
            day8.ops = (ArrayList<String>) aux.clone();
            // change jmp to nop or nop to jmp
            for (int j = current_op; j < day8.ops.size(); j++) {
                String[] op = day8.ops.get(j).trim().split(" ");
                if (op[0].equals("nop")) {
                    day8.ops.set(j, "jmp" + " " + op[1]);
                    break;
                } else if (op[0].equals("jmp")) {
                    day8.ops.set(j, "nop" + " " + op[1]);
                    break;
                } else {
                    current_op++;
                }
            }
            current_op++;
            i = day8.exec_op(scanner);
        }
        return i;
    }

    public static void main(String[] args) {
        String input = "input8.txt";
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
