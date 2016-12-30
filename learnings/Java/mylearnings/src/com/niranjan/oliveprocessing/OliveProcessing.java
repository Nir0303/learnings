package com.niranjan.oliveprocessing;

import com.niranjan.oliveprocessing.model.Olive;
import java.math.BigDecimal;
import java.util.List;
/**
 * Created by Niran0303 on 12/30/2016.
 */
public class OliveProcessing implements Press {
    private double currentOil;
     public double getOil(List<Olive> olives){
        BigDecimal totalOil=new BigDecimal(Double.toString(currentOil));

        for(Olive i:olives){
            String msg=i.getName()+" originated from "+i.getOrigin();
            System.out.println(msg);
            BigDecimal value=new BigDecimal(Double.toString(i.crush()));
            totalOil=totalOil.add(value);

        }
            return totalOil.doubleValue();
    }
    public void setOil(double currentOil){
        this.currentOil=currentOil;
    }
    public void setOil(){
        this.currentOil=0.0;
    }
}
