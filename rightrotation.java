import java.util.Scanner;
public class rightrotation {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    String str = sc.nextLine();
    int k = sc.nextInt();

    String rotatedStr = str.substring(str.length() - k) + str.substring(0, str.length() - k);
    System.out.println(rotatedStr);
    sc.close();
  }
}
