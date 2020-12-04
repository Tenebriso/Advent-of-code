import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class Day4 {

    private static HashMap<String, String> get_line_fields(String line) {
        String[] fields = line.split(" ");
        HashMap<String, String> parsed_fields = new HashMap<>();
        for (String field : fields)
            parsed_fields.put(field.split(":")[0], field.split(":")[1]);

        return parsed_fields;
    }

    private static boolean is_valid_fields(Set<String> pass_fields) {
        HashSet<String> fields = new HashSet<>(Arrays.asList("byr", "iyr", "eyr",
                "hgt", "hcl", "ecl", "pid", "cid"));
        fields.removeAll(pass_fields);
        if (fields.size() == 0 || (fields.size() == 1 && fields.contains("cid")))
            return true;

        return false;
    }

    private static HashMap<String, String> get_pass_fields(Scanner scanner) {
        HashMap<String, String> pass_fields = new HashMap<>();
        String current_line = scanner.nextLine();
        while (!current_line.trim().isEmpty() && scanner.hasNextLine()) {
            pass_fields.putAll(get_line_fields(current_line));
            current_line = scanner.nextLine();
        }
        if (!current_line.isEmpty())
            pass_fields.putAll(get_line_fields(current_line));

        return pass_fields;
    }

    public static int part1(String input) throws FileNotFoundException {
        Scanner scanner = new Scanner(new File(input));
        int count = 0;
        while (scanner.hasNextLine()) {
            Set<String> pass_fields = get_pass_fields(scanner).keySet();
            if (is_valid_fields(pass_fields))
                count++;
        }
        return count;
    }

    private static boolean is_valid_data(HashMap<String, String> pass_data) {
        int byr = Integer.parseInt(pass_data.get("byr"));
        if (byr < 1920 || byr > 2002)
            return false;

        int iyr = Integer.parseInt(pass_data.get("iyr"));
        if (iyr < 2010 || iyr > 2020)
            return false;

        int eyr = Integer.parseInt(pass_data.get("eyr"));
        if (eyr < 2020 || eyr > 2030)
            return false;

        String full_hgt = pass_data.get("hgt");
        int hgt = Integer.parseInt(full_hgt.substring(0, full_hgt.length() - 2));
        full_hgt = full_hgt.substring(full_hgt.length() - 2, full_hgt.length());
        if (full_hgt.equals("cm")) {
            if (hgt < 150 || hgt > 193)
                return false;
        } else if (full_hgt.equals("in")) {
            if (hgt < 59 || hgt > 76)
                return false;
        } else {
            return false;
        }

        String hcl = pass_data.get("hcl");
        if (!hcl.matches("^#[0-9a-f]*$") || hcl.length() != 7)
            return false;

        String eye_color = "amb blu brn gry grn hzl oth";
        if (!eye_color.contains(pass_data.get("ecl")))
            return false;

        String pid = pass_data.get("pid");
        if (pid.length() != 9 || !pid.matches("^[0-9]*$"))
            return false;

        return true;
    }

    public static int part2(String input) throws FileNotFoundException {
        Scanner scanner = new Scanner(new File(input));
        int count = 0;
        while (scanner.hasNextLine()) {
            HashMap<String, String> pass_data = get_pass_fields(scanner);
            Set<String> pass_fields = pass_data.keySet();
            if (is_valid_fields(pass_fields)){
                if (is_valid_data(pass_data)) {
                    count++;
                }
            }
        }
        return count;
    }

    public static void main(String args[]) {
        String input = "input4.txt";
        // part1
        try {
            System.out.println(part1(input));
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        // part2
        try {
            System.out.println(part2(input));
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }
}
