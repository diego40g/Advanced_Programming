/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package university;

import javax.ws.rs.core.Context;
import javax.ws.rs.core.UriInfo;
import javax.ws.rs.Consumes;
import javax.ws.rs.Produces;
import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.PUT;
import javax.ws.rs.core.MediaType;
import java.sql.*;
import java.util.ArrayList;
import java.util.List;
/**
 * REST Web Service
 *
 * @author Pancho
 */
@Path("student")
public class StudentResource {

    @Context
    private UriInfo context;

    /**
     * Creates a new instance of StudentResource
     */
    public StudentResource() {
        
    }

    /**
     * Retrieves representation of an instance of university.StudentResource
     * @return an instance of java.lang.String
     */
    @GET
    @Produces(MediaType.TEXT_PLAIN)
    public String getXml() {
        //TODO return proper representation object
       // throw new UnsupportedOperationException();
        String cadenaDatos="";
        try{
        Class.forName("org.postgresql.Driver");
        } catch (ClassNotFoundException e){
            e.getMessage();
        }
        //Definicion lista de datos
        
        List<StudentClass> result = new ArrayList<>();
        //Sentencia SQL
        String SQL_SELECT = "Select * from usuarios";

        // auto close connection and preparedStatement
        try (Connection conn = DriverManager.getConnection(
                "jdbc:postgresql://127.0.0.1:5432/usuario", "postgres", "1234abcd");
             PreparedStatement preparedStatement = conn.prepareStatement(SQL_SELECT)) {

            ResultSet resultSet = preparedStatement.executeQuery();

            while (resultSet.next()) {

                long id = resultSet.getLong("idUsuario");
                String name = resultSet.getString("Nombre");
                String phone = resultSet.getString("Apellido");

                StudentClass obj = new StudentClass();
                obj.setStudent_id(id);
                obj.setName(name);
                obj.setPhone(phone);

                result.add(obj);
                cadenaDatos= cadenaDatos + "\n\nID: " + id + "\tNombre: " + name +"\tApellido: " + phone ;
            }
            result.forEach(x -> System.out.println(x));

        } catch (SQLException e) {
            System.err.format("SQL State: %s\n%s", e.getSQLState(), e.getMessage());
        } catch (Exception e) {
            e.printStackTrace();
        }
       return cadenaDatos; 
    }

    /**
     * PUT method for updating or creating an instance of StudentResource
     * @param content representation for the resource
     */
    @PUT
    @Consumes(MediaType.APPLICATION_XML)
    public void putXml(String content) {
    }
}
