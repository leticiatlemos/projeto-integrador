package com.senai.infob.projetointegrador.controllers;

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

import com.senai.infob.projetointegrador.models.Usuario;
import com.senai.infob.projetointegrador.services.UsuarioService;

@RestController
@RequestMapping("/Usuario")
public class UsuarioController {
    @Autowired
    public UsuarioService UsuarioService;

    @GetMapping("/count")
    public Long count() {
        return UsuarioService.count();
    }

    @GetMapping("/find")
    public Usuario find(@RequestParam Integer id) {
        return UsuarioService.find(id);
    }

    @GetMapping("/allList")
    public List<Usuario> allList() {
        return UsuarioService.allList();
    }
    
    @PostMapping("/save")
    public Usuario postMethodName(@RequestBody Usuario Usuario) {
        return UsuarioService.save(Usuario);
    }
    
    @PutMapping("/update/{id}")
    public Usuario update(@PathVariable Integer id, @RequestBody Usuario Usuario) {
        return UsuarioService.update(Usuario, id);
    }

    @DeleteMapping("/delete/{id}")
    public String delete(@PathVariable Integer id) {
        boolean deleted = UsuarioService.delete(id);
        if (deleted) {
            return "Usuario removida com sucesso.";
        }
        return "Falha ao remover a Usuario.";
    }

}