
DROP DATABASE IF EXISTS `covid` ;

-- -----------------------------------------------------
-- Schema covid
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `covid` DEFAULT CHARACTER SET utf8 ;
USE `covid` ;

-- -----------------------------------------------------
-- Table `covid`.`etinias`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `covid`.`etinias` ;

CREATE TABLE IF NOT EXISTS `covid`.`etinias` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `value` VARCHAR(150) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `covid`.`generos`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `covid`.`generos` ;

CREATE TABLE IF NOT EXISTS `covid`.`generos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `value` VARCHAR(150) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `covid`.`pacientes`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `covid`.`pacientes` ;

CREATE TABLE IF NOT EXISTS `covid`.`pacientes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(150) NOT NULL,
  `cpf` VARCHAR(11) NOT NULL,
  `data_nasc` DATE NULL,
  `id_etinia` INT NULL,
  `id_genero` INT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_paciente_etinia_idx` (`id_etinia` ASC) VISIBLE,
  INDEX `fk_paciente_genero_idx` (`id_genero` ASC) VISIBLE,
  CONSTRAINT `fk_paciente_etinia`
    FOREIGN KEY (`id_etinia`)
    REFERENCES `covid`.`etinias` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_paciente_genero`
    FOREIGN KEY (`id_genero`)
    REFERENCES `covid`.`generos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `covid`.`adms_saude`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `covid`.`adms_saude` ;

CREATE TABLE IF NOT EXISTS `covid`.`adms_saude` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(150) NOT NULL,
  `crm` VARCHAR(20) NULL,
  `cpf` VARCHAR(11) NULL,
  `is_supervisor` TINYINT NOT NULL,
  `senha` VARCHAR(150) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `covid`.`atendimentos_iniciais`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `covid`.`atendimentos_iniciais` ;

CREATE TABLE IF NOT EXISTS `covid`.`atendimentos_iniciais` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `endereco` VARCHAR(255) NULL,
  `qnt_comodos` INT NULL,
  `is_agua_encanada` TINYINT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `covid`.`tentativas`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `covid`.`tentativas` ;

CREATE TABLE IF NOT EXISTS `covid`.`tentativas` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `value` VARCHAR(150) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `covid`.`atendimentos`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `covid`.`atendimentos` ;

CREATE TABLE IF NOT EXISTS `covid`.`atendimentos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `is_primeiro` TINYINT NOT NULL,
  `data` DATETIME NOT NULL,
  `id_inicial` INT NULL,
  `id_atendimento_inicial` INT NULL,
  `id_paciente` INT NOT NULL,
  `id_tentativa` INT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_atendimento_atendimento_inicial_idx` (`id_atendimento_inicial` ASC) VISIBLE,
  INDEX `fk_agendamento_paciente_idx` (`id_paciente` ASC) VISIBLE,
  INDEX `fk_atendimento_tentativa_idx` (`id_tentativa` ASC) VISIBLE,
  CONSTRAINT `fk_atendimento_atendimento_inicia`
    FOREIGN KEY (`id_atendimento_inicial`)
    REFERENCES `covid`.`atendimentos_iniciais` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_atendimento_paciente`
    FOREIGN KEY (`id_paciente`)
    REFERENCES `covid`.`pacientes` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_atendimento_tentativa`
    FOREIGN KEY (`id_tentativa`)
    REFERENCES `covid`.`tentativas` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `covid`.`agendamentos`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `covid`.`agendamentos` ;

CREATE TABLE IF NOT EXISTS `covid`.`agendamentos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `id_adm_saude` INT NOT NULL,
  `id_atendimento` INT NULL,
  `id_paciente` INT NOT NULL,
  `data` DATETIME NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_id_adm_saude_idx` (`id_adm_saude` ASC) VISIBLE,
  INDEX `fk_id_atendimento_idx` (`id_atendimento` ASC) VISIBLE,
  INDEX `fk_id_paciente_agendamento_idx` (`id_paciente` ASC) VISIBLE,
  CONSTRAINT `fk_id_adm_saude_agendamento`
    FOREIGN KEY (`id_adm_saude`)
    REFERENCES `covid`.`adms_saude` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_id_atendimento_agendamento`
    FOREIGN KEY (`id_atendimento`)
    REFERENCES `covid`.`atendimentos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_id_paciente_agendamento`
    FOREIGN KEY (`id_paciente`)
    REFERENCES `covid`.`pacientes` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `covid`.`doencas_cronicas`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `covid`.`doencas_cronicas` ;

CREATE TABLE IF NOT EXISTS `covid`.`doencas_cronicas` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `value` VARCHAR(150) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `covid`.`parentescos`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `covid`.`parentescos` ;

CREATE TABLE IF NOT EXISTS `covid`.`parentescos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `value` VARCHAR(150) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `covid`.`beneficios_sociais`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `covid`.`beneficios_sociais` ;

CREATE TABLE IF NOT EXISTS `covid`.`beneficios_sociais` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `value` VARCHAR(150) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `covid`.`motivos_sair`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `covid`.`motivos_sair` ;

CREATE TABLE IF NOT EXISTS `covid`.`motivos_sair` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `value` VARCHAR(150) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `covid`.`sintomas`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `covid`.`sintomas` ;

CREATE TABLE IF NOT EXISTS `covid`.`sintomas` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `value` VARCHAR(150) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `covid`.`indicadores`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `covid`.`indicadores` ;

CREATE TABLE IF NOT EXISTS `covid`.`indicadores` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `value` VARCHAR(150) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `covid`.`orientacoes_finais`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `covid`.`orientacoes_finais` ;

CREATE TABLE IF NOT EXISTS `covid`.`orientacoes_finais` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `value` VARCHAR(150) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `covid`.`estrategias_saude_familiar`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `covid`.`estrategias_saude_familiar` ;

CREATE TABLE IF NOT EXISTS `covid`.`estrategias_saude_familiar` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `value` VARCHAR(150) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `covid`.`medicamentos`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `covid`.`medicamentos` ;

CREATE TABLE IF NOT EXISTS `covid`.`medicamentos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `value` VARCHAR(150) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `covid`.`atendimentos_beneficios_sociais`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `covid`.`atendimentos_beneficios_sociais` ;

CREATE TABLE IF NOT EXISTS `covid`.`atendimentos_beneficios_sociais` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `id_atendimento` INT NOT NULL,
  `id_beneficio_social` INT NULL,
  `outros_beneficios_sociais` VARCHAR(150) NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_atendimento_beneficio_social_atendimento_idx` (`id_atendimento` ASC) VISIBLE,
  INDEX `fk_atendimento_beneficio_social_beneficio_social_idx` (`id_beneficio_social` ASC) VISIBLE,
  CONSTRAINT `fk_atendimento_beneficio_social_atendimento`
    FOREIGN KEY (`id_atendimento`)
    REFERENCES `covid`.`atendimentos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_atendimento_beneficio_social_beneficio_social`
    FOREIGN KEY (`id_beneficio_social`)
    REFERENCES `covid`.`beneficios_sociais` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `covid`.`atendimentos_motivos_sair`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `covid`.`atendimentos_motivos_sair` ;

CREATE TABLE IF NOT EXISTS `covid`.`atendimentos_motivos_sair` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `id_atendimento` INT NOT NULL,
  `id_motivo_sair` INT NULL,
  `outros_motivos_sair` VARCHAR(150) NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_atendimento_motivo_sair_atendimento_idx` (`id_atendimento` ASC) VISIBLE,
  INDEX `fk_atendimento_motivo_sair_motivo_sair_idx` (`id_motivo_sair` ASC) VISIBLE,
  CONSTRAINT `fk_atendimento_motivo_sair_atendimento`
    FOREIGN KEY (`id_atendimento`)
    REFERENCES `covid`.`atendimentos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_atendimento_motivo_sair_motivo_sair`
    FOREIGN KEY (`id_motivo_sair`)
    REFERENCES `covid`.`motivos_sair` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `covid`.`atendimentos_sintomas`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `covid`.`atendimentos_sintomas` ;

CREATE TABLE IF NOT EXISTS `covid`.`atendimentos_sintomas` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `id_atendimento` INT NOT NULL,
  `id_sintoma` INT NULL,
  `id_parentesco` INT NULL,
  `id_medicamento` INT NULL,
  `id_indicador` INT NULL,
  `outros_sintomas` VARCHAR(150) NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_atendimento_sintoma_atendimento_idx` (`id_atendimento` ASC) VISIBLE,
  INDEX `fk_atendimento_sintoma_sintoma_idx` (`id_sintoma` ASC) VISIBLE,
  INDEX `fk_atendimento_sintoma_parentesco_idx` (`id_parentesco` ASC) VISIBLE,
  INDEX `fk_atendimento_sintoma_medicamento_idx` (`id_medicamento` ASC) VISIBLE,
  INDEX `fk_atendimento_sintoma_indicador_idx` (`id_indicador` ASC) VISIBLE,
  CONSTRAINT `fk_atendimento_sintoma_atendimento`
    FOREIGN KEY (`id_atendimento`)
    REFERENCES `covid`.`atendimentos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_atendimento_sintoma_sintoma`
    FOREIGN KEY (`id_sintoma`)
    REFERENCES `covid`.`sintomas` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_atendimento_sintoma_parentesco`
    FOREIGN KEY (`id_parentesco`)
    REFERENCES `covid`.`parentescos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_atendimento_sintoma_medicamento`
    FOREIGN KEY (`id_medicamento`)
    REFERENCES `covid`.`medicamentos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_atendimento_sintoma_indicador`
    FOREIGN KEY (`id_indicador`)
    REFERENCES `covid`.`indicadores` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `covid`.`atendimentos_doencas_cronicas`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `covid`.`atendimentos_doencas_cronicas` ;

CREATE TABLE IF NOT EXISTS `covid`.`atendimentos_doencas_cronicas` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `id_atendimento` INT NOT NULL,
  `id_doenca_cronica` INT NULL,
  `id_medicamento` INT NULL,
  `id_indicador` INT NULL,
  `id_parentesco` INT NULL,
  `outros_medicamentos` VARCHAR(150) NULL,
  `outros_indicadores` VARCHAR(150) NULL,
  `outras_doencas_cronicas` VARCHAR(150) NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_atendimento_medicamento_indicador_atendimento_idx` (`id_atendimento` ASC) VISIBLE,
  INDEX `fk_atendimento_medicamento_indicador_medicamento_idx` (`id_medicamento` ASC) VISIBLE,
  INDEX `fk_atendimento_medicamento_indicador_indicador_idx` (`id_indicador` ASC) VISIBLE,
  INDEX `fk_atendimento_medicamento_indicador_parentesco_idx` (`id_parentesco` ASC) VISIBLE,
  INDEX `fk_atendimento_medicamento_indicador_doenca_cronica_idx` (`id_doenca_cronica` ASC) VISIBLE,
  CONSTRAINT `fk_atendimento_doenca_cronica_atendimento`
    FOREIGN KEY (`id_atendimento`)
    REFERENCES `covid`.`atendimentos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_atendimento_doenca_cronica_medicamento`
    FOREIGN KEY (`id_medicamento`)
    REFERENCES `covid`.`medicamentos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_atendimento_doenca_cronica_indicador`
    FOREIGN KEY (`id_indicador`)
    REFERENCES `covid`.`indicadores` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_atendimento_doenca_cronica_parentesco`
    FOREIGN KEY (`id_parentesco`)
    REFERENCES `covid`.`parentescos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_atendimento_doenca_cronica_doenca_cronica`
    FOREIGN KEY (`id_doenca_cronica`)
    REFERENCES `covid`.`doencas_cronicas` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `covid`.`atendimentos_orientacoes_finais`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `covid`.`atendimentos_orientacoes_finais` ;

CREATE TABLE IF NOT EXISTS `covid`.`atendimentos_orientacoes_finais` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `id_atendimento` INT NOT NULL,
  `id_orientacao_final` INT NULL,
  `comentario` VARCHAR(255) NULL,
  `outras_orientacoes_finais` VARCHAR(150) NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_antedimento_orientacao_final_atendimento_idx` (`id_atendimento` ASC) VISIBLE,
  INDEX `fk_antedimento_orientacao_final__idx` (`id_orientacao_final` ASC) VISIBLE,
  CONSTRAINT `fk_antedimento_orientacao_final_atendimento`
    FOREIGN KEY (`id_atendimento`)
    REFERENCES `covid`.`atendimentos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_antedimento_orientacao_final_`
    FOREIGN KEY (`id_orientacao_final`)
    REFERENCES `covid`.`orientacoes_finais` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `covid`.`atendimentos_estrategias_saudes_familiar`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `covid`.`atendimentos_estrategias_saudes_familiar` ;

CREATE TABLE IF NOT EXISTS `covid`.`atendimentos_estrategias_saudes_familiar` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `id_atendimento` INT NOT NULL,
  `id_estrategia_saude_familiar` INT NULL,
  `outras_estrategias_saude_familiar` VARCHAR(150) NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_atendimento_estrategia_saude_familiar_atendimento_idx` (`id_atendimento` ASC) VISIBLE,
  INDEX `fk_atendimento_estrategia_saude_familiar_estrategia_saude_f_idx` (`id_estrategia_saude_familiar` ASC) VISIBLE,
  CONSTRAINT `fk_atendimento_esf_atendimento`
    FOREIGN KEY (`id_atendimento`)
    REFERENCES `covid`.`atendimentos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_atendimento_esf_estrategia_saude_familiar`
    FOREIGN KEY (`id_estrategia_saude_familiar`)
    REFERENCES `covid`.`estrategias_saude_familiar` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `covid`.`tempos_contato_acompanhamento`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `covid`.`tempos_contato_acompanhamento` ;

CREATE TABLE IF NOT EXISTS `covid`.`tempos_contato_acompanhamento` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `intervalo_contato` INT NULL,
  `tempo_maximo_acompanhamento` INT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;

select * from adms_saude;