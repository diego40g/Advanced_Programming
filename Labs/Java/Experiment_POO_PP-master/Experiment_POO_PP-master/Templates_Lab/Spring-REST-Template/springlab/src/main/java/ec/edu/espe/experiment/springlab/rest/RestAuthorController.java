package ec.edu.espe.experiment.springlab.rest;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import ec.edu.espe.experiment.springlab.dao.IAuthorDAO;
import ec.edu.espe.experiment.springlab.dto.Author;

@RestController

@RequestMapping("api/author")
public class RestAuthorController{

    @Autowired
    private IAuthorDAO dao;

    @GetMapping
    public ResponseEntity<List<Author>> getAll() {
        List<Author> response = dao.getAll();
        if (response != null) {
            return ResponseEntity.status(HttpStatus.OK).body(response);
        } else {
            return ResponseEntity.status(HttpStatus.NOT_FOUND).body(response);
        }
    }

    @GetMapping(value = "/{id}")
    public ResponseEntity<Author> get(@PathVariable("id") Integer id) {
        Author response = dao.get(id);
        if (response != null) {
            return ResponseEntity.status(HttpStatus.OK).body(response);
        } else {
            return ResponseEntity.status(HttpStatus.NOT_FOUND).body(response);
        }
    }

    @PostMapping
    public ResponseEntity<Author> post(@RequestBody Author entity) {
        Author response = dao.post(entity);
        if (response != null) {
            return ResponseEntity.status(HttpStatus.CREATED).body(response);
        } else {
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(response);
        }
    }

}