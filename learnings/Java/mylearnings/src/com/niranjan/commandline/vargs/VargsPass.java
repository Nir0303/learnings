package com.niranjan.commandline.vargs;

/**
 * Created by Niran0303 on 12/26/2016.
 */
public class VargsPass {
    void arrimp(int[] a){
        for(int i=0;i<a.length;i++){
            System.out.println("Arguement at "+i+" "+a[i]);
        }
    }
    void varargsimp(int...a){
        for(int i:a){
            System.out.println("Value is "+i);
        }
    }
    void varagswithnormal(String msg,int...a){
        for(int i:a){
            System.out.println(msg+" is "+i);
        }
    }
}

