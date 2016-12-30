package com.niranjan.oliveprocessing;

import com.niranjan.oliveprocessing.model.Olive;
import java.util.List;
/**
 * Created by Niran0303 on 12/30/2016.
 */
public class OliveProcessing {
    protected double getOil(List<Olive> olives){
        double totalOil=0.0;
        for(Olive i:olives){
            System.out.println(i.getName());
            totalOil+=i.crush();
        }
            return totalOil;
    }
}
