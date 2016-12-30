package com.hackerrank.java.basic;
import java.util.Scanner;
/**
 * Area of Parallelogram return error if Breadth or Height are non positive
 */
public class AreaParallelogram {
    static int B, H;
    static boolean flag = true;
    static{
        Scanner sc= new Scanner(System.in);
        B=sc.nextInt();
        H=sc.nextInt();
        try{
            if (B<=0||H<=0)
                throw new Exception("Breadth and height must be positive");
        }catch(Exception e){
            System.out.println(e);
            flag=false;
        }

    }
    public static void main(String[] args){
        if(flag){
            int area=B*H;
            System.out.print(area);
        }
       // System.out.println(flag);
    }//end of main

}

