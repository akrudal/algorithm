import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int N = scanner.nextInt();
        int K = scanner.nextInt();
        
        ArrayList<Integer> divisors = new ArrayList<>();
        
        if (K == 1) {
            System.out.println(1);
            return;
        }
        
        for (int i = 1; i <= N; i++) {
            if (N % i == 0) {
                divisors.add(i);
            }
        }
        
        if (divisors.size() >= K) {
            System.out.println(divisors.get(K - 1));
        } else {
            System.out.println(0);
        }
    }
}
