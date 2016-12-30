package com.hackerrank.java.basic;

import java.util.Scanner;

/**
 * Series challenge
 * Sample Input

 2
 0 2 10
 5 3 5
 Sample Output

 2 6 14 30 62 126 254 510 1022 2046
 8 14 26 50 98
 */
public class Series {
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int t=in.nextInt();
        for(int i=0;i<t;i++){

            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
            int arr[]=new int[n];
            arr[0]=a+b;
            for(int j=0;j<n;j++){
                if(j>0){
                    int temp=arr[j-1];
                    arr[j]=temp;
                    arr[j]+=(Math.pow(2,j))*b;
                }
                System.out.print(arr[j]+" ");
            }
            System.out.println();
        }
        in.close();
    }
}
