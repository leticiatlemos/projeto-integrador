package com.senai.infob.projetointegrador.repositories;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.senai.infob.projetointegrador.models.Calendario;

@Repository
public interface CalendarioRepository extends JpaRepository<Calendario, Integer> {

}