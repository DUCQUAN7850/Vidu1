/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mycompany.thuvien;

import com.google.common.cache.LoadingCache;
import static java.lang.System.in;
import java.util.Scanner;
import java.util.concurrent.ExecutionException;

/**
 *
 * @author DUC QUAN
 */
public class Cau4 {
    public static void main(String[] args) throws ExecutionException {
            Cau4 guavaTest = new Cau4();
//            try {
//                System.out.println(guavaTest.getStringGuava(1));
//            } catch (ExecutionException e) {
//            }
        
        LoadingCache<Integer, String> cache = GuavaCache.getLoadingCache();
        System.out.println(cache.get(1));
        System.out.println(cache.get(2));
        System.out.println("Cache Size:" + cache.size());
    }
 
//    private String getStringGuava(int id) throws ExecutionException {
//        
//        return cache.get(id);
//    }
}
