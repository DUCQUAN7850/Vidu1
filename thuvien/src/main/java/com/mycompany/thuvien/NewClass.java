/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mycompany.thuvien;

import com.google.common.cache.LoadingCache;
import java.util.Scanner;
import java.util.concurrent.ExecutionException;
import static jdk.nashorn.internal.objects.NativeFunction.function;

/**
 *
 * @author DUC QUAN
 */
public class NewClass {
    public static String KQ(int k){
        String s="";
        for(int i=1;i<k;i++){
            s=s+i+" ";
        }
        return s;
    }
    public static void main(String[] args) throws ExecutionException {
        LoadingCache<Integer, String> c = GuavaCache.getLoadingCache();
        Scanner in=new Scanner(System.in);
            long lancuoi=System.currentTimeMillis();
        while(true){
            System.out.println("Nhap so: ");
            int k=in.nextInt();
            long lantiep=System.currentTimeMillis();
            c.put(k, KQ(k));
            if(lantiep-lancuoi>=10000){
                System.out.println("Da qua 10s, cache bi xoa!");
                c.invalidateAll();
            }
            System.out.println(c.get(k));
            System.out.println("Size= "+c.size());
            lancuoi=System.currentTimeMillis();
            if(k==-1)break;
        }
    }
}
