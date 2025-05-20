import java.util.Random;

public class RandomBinaryGenerator {
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
