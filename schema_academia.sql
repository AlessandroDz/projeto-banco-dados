CREATE DATABASE IF NOT EXISTS academia CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE academia;

CREATE TABLE IF NOT EXISTS instrutor (
  id_instrutor INT NOT NULL AUTO_INCREMENT,
  nome VARCHAR(120) NOT NULL,
  especialidade VARCHAR(100),
  telefone VARCHAR(20),
  email VARCHAR(100),
  PRIMARY KEY (id_instrutor)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS aluno (
  id_aluno INT NOT NULL AUTO_INCREMENT,
  nome VARCHAR(120) NOT NULL,
  cpf VARCHAR(14) NOT NULL UNIQUE,
  data_nascimento DATE NOT NULL,
  telefone VARCHAR(20),
  PRIMARY KEY (id_aluno)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS treino (
  id_treino INT NOT NULL AUTO_INCREMENT,
  id_aluno INT NOT NULL,
  id_instrutor INT NOT NULL,
  tipo VARCHAR(50),
  horario VARCHAR(10),
  dias_semana VARCHAR(50),
  frequencia INT DEFAULT 0,
  PRIMARY KEY (id_treino),
  CONSTRAINT fk_treino_aluno FOREIGN KEY (id_aluno) REFERENCES aluno(id_aluno) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT fk_treino_instrutor FOREIGN KEY (id_instrutor) REFERENCES instrutor(id_instrutor) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB;

-- Inserções (20 alunos)
INSERT INTO aluno (nome, cpf, data_nascimento, telefone) VALUES
('Ana Paula','123.456.789-00','1995-06-20','(11) 91234-5678'),
('Bruno Oliveira','987.654.321-00','1988-12-10','(11) 99876-5432'),
('Camila Santos','555.666.777-88','2000-03-15','(11) 95555-7777'),
('Diego Rocha','321.654.987-00','1997-09-29','(11) 91111-2222'),
('Eduarda Ramos','444.333.221-11','1999-11-05','(11) 92222-3333'),
('Felipe Martins','222.111.000-55','2001-07-08','(11) 93333-4444'),
('Gabriela Nunes','999.888.777-66','2002-02-28','(11) 94444-5555'),
('Henrique Dias','777.666.555-44','1994-04-14','(11) 95555-6666'),
('Isabela Moreira','888.777.666-55','2001-01-25','(11) 96666-7777'),
('João Pedro','666.555.444-33','1990-10-09','(11) 97777-8888'),
('Laura Mendes','555.444.333-22','1998-05-03','(11) 98888-9999'),
('Mateus Lima','333.222.111-00','1993-07-17','(11) 97777-1111'),
('Natália Freitas','999.000.111-22','1996-11-22','(11) 93333-2222'),
('Otávio Souza','888.999.111-33','1992-02-01','(11) 92222-4444'),
('Patrícia Carvalho','111.222.333-44','1989-06-12','(11) 91111-5555'),
('Ricardo Almeida','333.444.555-66','1995-09-09','(11) 97777-6666'),
('Sabrina Torres','777.888.999-00','1999-01-30','(11) 98888-7777'),
('Thiago Costa','666.777.888-99','2000-03-18','(11) 93333-5555'),
('Vanessa Prado','444.555.666-77','1997-04-27','(11) 95555-4444'),
('William Ramos','555.666.777-11','1991-08-13','(11) 94444-3333');

-- Inserções (8 instrutores)
INSERT INTO instrutor (nome, especialidade, telefone, email) VALUES
('Mariana Lopes','Musculação','(11) 98888-1111','mariana.lopes@labfit.com'),
('Carlos Silva','Crossfit','(11) 97777-2222','carlos.silva@labfit.com'),
('Fernanda Costa','Pilates','(11) 96666-3333','fernanda.costa@labfit.com'),
('Rafael Gomes','Alongamento','(11) 95555-4444','rafael.gomes@labfit.com'),
('Luciana Prado','Yoga','(11) 94444-5555','luciana.prado@labfit.com'),
('André Ferreira','Funcional','(11) 93333-6666','andre.ferreira@labfit.com'),
('Beatriz Melo','Zumba','(11) 92222-7777','beatriz.melo@labfit.com'),
('Gustavo Tavares','Spinning','(11) 91111-8888','gustavo.tavares@labfit.com');

-- Inserções (16 treinos)
INSERT INTO treino (id_aluno, id_instrutor, tipo, horario, dias_semana, frequencia) VALUES
(1, 1, 'Musculação', '08:00', 'Seg, Qua, Sex', 3),
(2, 2, 'Crossfit', '07:30', 'Ter, Qui, Sab', 3),
(3, 3, 'Pilates', '09:00', 'Seg, Qua, Sex', 3),
(4, 4, 'Alongamento', '10:00', 'Ter, Qui', 2),
(5, 5, 'Yoga', '11:00', 'Seg, Qua, Sex', 3),
(6, 6, 'Funcional', '18:00', 'Seg, Qua, Sex', 3),
(7, 7, 'Zumba', '19:00', 'Ter, Qui', 2),
(8, 8, 'Spinning', '20:00', 'Seg, Qua, Sex', 3),
(9, 1, 'Musculação', '17:00', 'Ter, Qui, Sab', 3),
(10, 2, 'Crossfit', '06:30', 'Seg, Qua, Sex', 3),
(11, 3, 'Yoga', '09:30', 'Seg, Qua', 2),
(12, 4, 'Pilates', '10:30', 'Ter, Qui', 2),
(13, 5, 'Zumba', '18:30', 'Seg, Qua, Sex', 3),
(14, 6, 'Spinning', '19:30', 'Ter, Qui, Sab', 3),
(15, 7, 'Funcional', '20:30', 'Seg, Qua', 2),
(16, 8, 'Alongamento', '21:00', 'Ter, Qui', 2);

COMMIT;
