import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int T = scanner.nextInt();
             
        for (int i = 0; i < T; i++) {
            int n = scanner.nextInt();
            int count = 0;
            
            while (n > 0) {
                if (n % 2 == 1) {
                    System.out.print(count + " ");
                }
                count++;
                n = n / 2;
            }
            System.out.println();
        }
        
        scanner.close();
    }
}