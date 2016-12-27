package com.niranjan.recursion;

/**
 * Created by Niran0303 on 12/26/2016.
 */
public class Fibonnaci {

    int fibovalue(int i){
        if(i<2) return 1;
        else {
             return fibovalue(i-1)+fibovalue(i-2);
        }

    }
}
