public class RuleChecker {
    public static void main(String[] args) {
        if (args.length < 1) {
            System.out.println("0");
            return;
        }

        String output = args[0];
        int score = scoreOutput(output);
        System.out.println(score);
    }

    public static int scoreOutput(String output) {
        if (output == null || output.isEmpty()) return 0;

        // Example: Score based on output length
        if (output.length() < 5) return 3;
        if (output.length() < 10) return 7;
        return 10;
    }
}
