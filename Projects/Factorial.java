import java.util.*;

public class Factorial {
    
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);     
        System.out.println("Enter number for factorial");  
        int n= sc.nextInt();
        int res = fac(n);
        System.out.println("The result of factorial is " + res);  
        
    }

    public static int fac(int i) {
        if(i <0) {
            System.out.println("i must not be below 0");
            return 0;
        } 
        else {
            if(i<=1) {
                return 1;
            } else return i*fac(i-1);
        }
    }

}
