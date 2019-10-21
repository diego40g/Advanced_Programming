package ec.edu.espe.demo.imp;

import org.springframework.stereotype.Component;

import ec.edu.espe.demo.util.IPerson;

@Component("Student")
public class Student implements IPerson{

    @Override
    public String hello() {
        return "Hello, I'm Student";
    }

}