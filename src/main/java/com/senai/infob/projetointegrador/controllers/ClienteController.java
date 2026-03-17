package com.senai.infob.prova.controllers;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.senai.infob.prova.models.Cliente;
import com.senai.infob.prova.services.ClienteService;

@RestController
@RequestMapping("/cliente")
public class ClienteController {
    @Autowired
    public ClienteService clienteService;

    @GetMapping("/count")
    public Long count() {
        return clienteService.count();
    }

    @GetMapping("/find")
    public Cliente find(@RequestParam Integer id) {
        return clienteService.find(id);
    }

    @GetMapping("/allList")
    public List<Cliente> allList() {
        return clienteService.allList();
    }
    
    @PostMapping("/save")
    public Cliente postMethodName(@RequestBody Cliente cliente) {
        return clienteService.save(cliente);
    }
    
    @PutMapping("/update/{id}")
    public Cliente update(@PathVariable Integer id, @RequestBody Cliente cliente) {
        return clienteService.update(cliente, id);
    }

    @DeleteMapping("/delete/{id}")
    public String delete(@PathVariable Integer id) {
        boolean deleted = clienteService.delete(id);
        if (deleted) {
            return "Cliente removida com sucesso.";
        }
        return "Falha ao remover a cliente.";
    }

}