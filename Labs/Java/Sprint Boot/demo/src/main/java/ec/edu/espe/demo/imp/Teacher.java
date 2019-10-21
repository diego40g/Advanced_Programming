package ec.edu.espe.demo.imp;

import org.springframework.stereotype.Component;

import ec.edu.espe.demo.util.IPerson;


@Component("Teacher")
public class Teacher implements IPerson{

    @Override
    public String hello(){
        return "Hello, I'm TEACHER";
    }
}