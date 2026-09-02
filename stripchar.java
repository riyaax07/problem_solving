import java.util.Scanner;
public class stripchar {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String str = sc.nextLine();
        int n = sc.nextInt();
        int m = sc.nextInt();

        System.out.println(str.substring(n, m));
    }
}

