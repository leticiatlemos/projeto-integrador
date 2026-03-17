package com.senai.infob.projetointegrador.models;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.JoinTable;
import jakarta.persistence.ManyToMany;
import jakarta.persistence.Table;
import scala.collection.mutable.Set;

@Entity
@Table
public class Acessibilidade {
    @Id
    @GeneratedValue(strategy=GenerationType.IDENTITY)
    @Column(name="id")
    private Integer id;

    @Column(name="nome")
    private String nome;

    @Column (name="tipo")
    private String tipo;

    @Column(name="categoria")
    private String categoria;

        @ManyToMany
    @JoinTable(
        name = "usuario_acessibilidade",
        joinColumns = @JoinColumn(name = "acessibilidade_id", referencedColumnName = "id"),
        inverseJoinColumns = @JoinColumn(name = "usuario_id", referencedColumnName = "id")
    )
    private Set<Usuario> usuario;

        public Acessibilidade() {
        }

        public Acessibilidade(Integer id, String nome, String tipo, String categoria, Set<Usuario> usuario) {
            this.id = id;
            this.nome = nome;
            this.tipo = tipo;
            this.categoria = categoria;
            this.usuario = usuario;
        }

        public Integer getId() {
            return id;
        }

        public String getNome() {
            return nome;
        }

        public String getTipo() {
            return tipo;
        }

        public String getCategoria() {
            return categoria;
        }

        public Set<Usuario> getUsuario() {
            return usuario;
        }

        public void setId(Integer id) {
            this.id = id;
        }

        public void setNome(String nome) {
            this.nome = nome;
        }

        public void setTipo(String tipo) {
            this.tipo = tipo;
        }

        public void setCategoria(String categoria) {
            this.categoria = categoria;
        }

        public void setUsuario(Set<Usuario> usuario) {
            this.usuario = usuario;
        }


    
    
}