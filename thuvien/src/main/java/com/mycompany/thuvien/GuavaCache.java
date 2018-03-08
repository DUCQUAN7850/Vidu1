/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mycompany.thuvien;

import com.google.common.cache.CacheBuilder;
import com.google.common.cache.CacheLoader;
import com.google.common.cache.LoadingCache;
import java.util.Scanner;
import java.util.concurrent.TimeUnit;

/**
 *
 * @author DUC QUAN
 */
public class GuavaCache {
    private static LoadingCache<Integer, String> cache;
    static {
        cache = CacheBuilder.newBuilder()
           .maximumSize(100)
           .expireAfterWrite(10, TimeUnit.MINUTES)
           .build(
                new CacheLoader<Integer, String>() {
                    @Override
                    public String load(Integer id) throws Exception {
                            return getStringById(id);
                    }
                }
        );
    }
    public static LoadingCache<Integer, String> getLoadingCache() {
	return cache;
    }
    public static String getStringById(int id) {
        return "";
    }
}
