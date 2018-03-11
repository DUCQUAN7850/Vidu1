/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package a;

import javax.ws.rs.core.Context;
import javax.ws.rs.core.UriInfo;
import javax.ws.rs.Consumes;
import javax.ws.rs.DefaultValue;
import javax.ws.rs.Produces;
import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.PUT;
import javax.ws.rs.QueryParam;
import javax.ws.rs.core.MediaType;

/**
 * REST Web Service
 *
 * @author DUC QUAN
 */
@Path("generic")
public class GenericResource {

    @Context
    private UriInfo context;

    /**
     * Creates a new instance of GenericResource
     */
    public GenericResource() {
    }
    public boolean NTo(int k){
        for(int i=2;i<k;i++){
            if(k%i==0)return false;
        }
        return true;
    }
    /**
     * Retrieves representation of an instance of a.GenericResource
     * @return an instance of java.lang.String
     */
    @Path("/add")
    @GET
    @Produces(MediaType.APPLICATION_XML)
    public String add(@DefaultValue("0") @QueryParam("num1") double num1) {
        //TODO return proper representation object
        //throw new UnsupportedOperationException();
        String res="";
        for(int i=2;i<num1;i++){
            if(NTo(i)==true)
            res=res+i+" ";
        }
        return ""+res;
    }
    /**
     * PUT method for updating or creating an instance of GenericResource
     * @param content representation for the resource
     */
    @PUT
    @Consumes(MediaType.APPLICATION_XML)
    public void putXml(String content) {
    }
}
