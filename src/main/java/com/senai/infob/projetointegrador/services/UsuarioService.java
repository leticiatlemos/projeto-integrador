package com.senai.infob.projetointegrador.services;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.senai.infob.projetointegrador.models.Usuario;
import com.senai.infob.projetointegrador.repositories.UsuarioRepository;

@Service
public class UsuarioService {
    @Autowired
    public UsuarioRepository UsuarioRepository;

    public Long count() {
        return UsuarioRepository.count();
    }

    public Usuario find(Integer id) {
        return UsuarioRepository.findById(id).get();
    }

    public List<Usuario> allList() {
        return UsuarioRepository.findAll();
    }

    public Usuario save(Usuario Usuario) {
        return UsuarioRepository.save(Usuario);
    }

    public Usuario update(Usuario Usuario, Integer id) {
        Usuario con = find(id);
        if (con != null) {
            Usuario.setId(id);
            return UsuarioRepository.save(Usuario);
        }
        return null;
    }

    public boolean delete(Integer id) {
        Usuario Usuario = UsuarioRepository.findById(id).get();
        if (Usuario != null) {
            UsuarioRepository.deleteById(id);
            return true;
        }
        return false;
    }
}