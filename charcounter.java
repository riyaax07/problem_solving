import java.util.Scanner;

public class charcounter {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String str = sc.nextLine();
        int n = sc.nextInt();
        int m = sc.nextInt();

        int count = 0;

        for (int i = 0; i < str.length(); i++) {
            char ch = str.charAt(i);
            
            if (ch >= n && ch <= m) {
                count++;
            }
        }

        System.out.println(count);
        sc.close();
    }
}
