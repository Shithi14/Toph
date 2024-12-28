import java.util.Scanner;
public class ascending{
    public static void main(String args[]){
        int n;
        Scanner sc=new Scanner (System.in);
        n=sc.nextInt();
        int arr[]=new int[n];
        for (int i=0;i<n;i++){
            arr[i]=sc.nextInt();

        }
        boolean answer=true;
        for(int i=0;i<n-1;i++){
           if( arr[i]>arr[i+1]){
            answer=false;
            break;
           }
        }
        if (answer){
            System.out.println("Yes");
        }
       else{
        System.out.println("No");
       }

    }

 }