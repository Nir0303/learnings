package com.niranjan.multidimension;

/**
 * Created by Niran0303 on 12/25/2016.
 */
public class MultiDimensionalArray {
    public static void main(String args[]){
        int class1[][]=new int[4][];
        class1[0]=new int[5];
        class1[1]=new int[3];
        class1[2]=new int[2];
        class1[3]=new int[1];
        for(int[] i:class1){
            for(int j:i){
                System.out.print(j);
            }
            System.out.println();

        }
    }
}
