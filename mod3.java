import java.util.Scanner;
public class mod3 {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    int start = scanner.nextInt();
    int end = scanner.nextInt();
    int count = 0;

    for (int i = start; i <= end; i++) {
      if (i % 3 == 0) {
        int total = 0;
        int j = i;
        while (j > 0) {
          total += j % 10;
          j /= 10;
        }
        if (total % 2 == 0) {
          count++;
        }
      }
    }
    System.out.println(count);
  }
}

