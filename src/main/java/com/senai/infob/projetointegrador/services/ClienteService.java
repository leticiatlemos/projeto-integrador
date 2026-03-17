package com.senai.infob.projetointegrador.services;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.senai.infob.projetointegrador.models.Cliente;
import com.senai.infob.projetointegrador.repositories.ClienteRepository;

@Service
public class ClienteService {
    @Autowired
    public ClienteRepository clienteRepository;

    public Long count() {
        return clienteRepository.count();
    }

    public Cliente find(Integer id) {
        return clienteRepository.findById(id).get();
    }

    public List<Cliente> allList() {
        return clienteRepository.findAll();
    }

    public Cliente save(Cliente cliente) {
        return clienteRepository.save(cliente);
    }

    public Cliente update(Cliente cliente, Integer id) {
        Cliente con = find(id);
        if (con != null) {
            cliente.setId(id);
            return clienteRepository.save(cliente);
        }
        return null;
    }

    public boolean delete(Integer id) {
        Cliente cliente = clienteRepository.findById(id).get();
        if (cliente != null) {
            clienteRepository.deleteById(id);
            return true;
        }
        return false;
    }
}