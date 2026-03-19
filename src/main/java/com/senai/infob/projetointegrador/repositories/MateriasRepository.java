package com.senai.infob.projetointegrador.repositories;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.senai.infob.projetointegrador.models.Materias;

@Repository
public interface MateriasRepository extends JpaRepository<Materias, Integer> {

}