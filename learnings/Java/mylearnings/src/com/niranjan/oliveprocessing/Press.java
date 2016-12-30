package com.niranjan.oliveprocessing;
import com.niranjan.oliveprocessing.model.*;
import java.util.List;
/**
 * Created by Niran0303 on 12/30/2016.
 */
public interface Press {
    public double getOil(List<Olive> oil);
    public void setOil(double currentOil);
}
