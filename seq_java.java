import java.util.Random;


public class RandomBinaryGenerator {

    /**
     * generates and prints a 128-bit random binary sequence
     * method generates 4 random 32-bit integers, converts each to its
     * 32-bit binary representation, concatenates them, and prints the result
     *
     * @param args command-line arguments (not used)
     */
    public static void main(String[] args) {
        Random random = new Random();
        StringBuilder binarySequence = new StringBuilder();

        for (int i = 0; i < 4; i++) {
            binarySequence.append(String.format("%32s",
                Integer.toBinaryString(random.nextInt())).replace(' ', '0'));
        }

        System.out.println("128-bit binary sequence: " + binarySequence);
    }
}
