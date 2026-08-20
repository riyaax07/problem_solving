import java.util.*;
public class removeelements{
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    System.out.print("Enter the number of elements: ");
    int n = sc.nextInt();
    while(n>0){
      int size = sc.nextInt();
      ArrayList<Integer> a = new ArrayList<>();

      for(int i=0; i<size; i++){
        a.add(sc.nextInt());
      }

      int count = Collections.frequency(a, 1);
      if (count <a.size()){
        a.remove(count);
      }
      System.out.println(a);
      n--;


    }
  }
}