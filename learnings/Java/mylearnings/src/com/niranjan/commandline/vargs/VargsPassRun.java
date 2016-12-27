package com.niranjan.commandline.vargs;

/**
 * Created by Niran0303 on 12/26/2016.
 */
public class VargsPassRun{
    public static void main(String args[]){
        VargsPass v=new VargsPass();
        int arg1[]={1,2,3};
        v.arrimp(arg1);
        v.varargsimp(1,2,3);
        v.varagswithnormal("Three arguements",1,2,3);
    }
}
