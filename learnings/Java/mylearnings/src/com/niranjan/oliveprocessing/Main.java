package com.niranjan.oliveprocessing;
import com.niranjan.oliveprocessing.model.Olive;
import java.util.ArrayList;
import java.util.List;
/**
 * Created by Niran0303 on 12/30/2016.
 */
public class Main {
    public static void main(String args[]){
        List<Olive> olives=new ArrayList<>();
        Olive olive1=new Olive();
        olives.add(olive1);
        Olive olive2=new Olive();
        olives.add(olive2);
        Olive olive3=new Olive();
        olives.add(olive3);
        OliveProcessing processing = new OliveProcessing();
        double totalOil= processing.getOil(olives);
        System.out.println("Total oil crushed is "+totalOil);


    }
}
