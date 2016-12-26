package com.niranjan.pyramid;

/**
 * Created by Niran0303 on 12/25/2016.
 */
public class Pyramid {
    public static void main(String args[]){
        int i=4;
        //decreasing pyramid
        System.out.println("decreasing pyramid");
        for(int a=0;a<i;a++){
            for(int b=a;b<i;b++) {
                System.out.print(".");
            }
            System.out.println();
        }
        System.out.println("increasing pyramid");
        //increasing pyramid
        for(int a=0;a<i;a++){
            for(int b=i-a-1;b<i;b++)
                System.out.print(".");
            System.out.println();
        }
        //real pyramid
        System.out.println("real pyramid");
        for(int a=0;a<i;a++){
            for(int b=0;b<i+a;b++){
                if(b+a<i-1){
                    System.out.print(" ");
                }
                else{
                    System.out.print(".");
                }
            }
            System.out.println();
        }
        System.out.println("inverted pyramid");
        for(int a=i;a<=i&&a>0;a--){
            for(int b=0;b<2*a;b++){
                if(b+a>=i && b+a<3*i-1){
                    System.out.print(".");
                }
                else{
                    System.out.print(" ");
                }
            }
            System.out.println();
        }
    }
}
