import java.util.Scanner;
public class singledigitsum {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    int n = scanner.nextInt();
    int k = scanner.nextInt();
    int total = n * k;
    
    while (String.valueOf(total).length() > 1) {
      int totalSum = 0;
      while (total > 0) {
        totalSum += total % 10;
        total /= 10;
      }
      total = totalSum;
    }
    
    System.out.println(total);
  }
}
