import java.util.Scanner;

public class pyramid {
    public static void main(String args[]) {
        int n;
        Scanner input = new Scanner(System.in);
        n = input.nextInt();
        
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n - i; j++) {
                System.out.print(" ");
            }
            for (int j = 1; j <= i; j++) {
                System.out.print("*");
                if (j < i) {
                    System.out.print(" ");
                }
            }
            System.out.println();
        }
    }
}
