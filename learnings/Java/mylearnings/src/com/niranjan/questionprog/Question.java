package com.niranjan.questionprog;


/**
 * Created by Niran0303 on 12/28/2016.
 */

import java.util.Random;
public class Question implements SharedConstants {
    Random rand= new Random();
    int ask(){
        int prob = (int) (rand.nextDouble() * 100);
        int i=1/0;
        //System.out.println(prob);
        if(prob<30){
            return NO;
        }
        else if(prob<50){
            return YES;
        }
        else if(prob<60){
            return MAYBE;
        }
        else if(prob<75){
            return LATER;
        }
        else if(prob<98){
            return SOON;
        }
        else{
            return NEVER;
        }
    }
}
