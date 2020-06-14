-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema covid-19
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema covid-19
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `covid-19` DEFAULT CHARACTER SET utf8 COLLATE utf8_bin ;
USE `covid-19` ;

-- -----------------------------------------------------
-- Table `covid-19`.`amostra_cole_notifica`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `covid-19`.`amostra_cole_notifica` (
  `idColeta_amostra` INT(11) NOT NULL,
  `amostra_id` INT(11) NOT NULL,
  `idNotificacao` INT(11) NOT NULL,
  PRIMARY KEY (`idColeta_amostra`, `amostra_id`, `idNotificacao`),
  INDEX `amostra_id` (`amostra_id` ASC) ,
  INDEX `idNotificacao` (`idNotificacao` ASC) ,
  CONSTRAINT `amostra_cole_notifica_ibfk_1`
    FOREIGN KEY (`idColeta_amostra`)
    REFERENCES `covid-19`.`coleta` (`idColeta_amostra`),
  CONSTRAINT `amostra_cole_notifica_ibfk_2`
    FOREIGN KEY (`amostra_id`)
    REFERENCES `covid-19`.`amostra` (`amostra_id`),
  CONSTRAINT `amostra_cole_notifica_ibfk_3`
    FOREIGN KEY (`idNotificacao`)
    REFERENCES `covid-19`.`notificacao` (`idNotificacao`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;


-- -----------------------------------------------------
-- Table `covid-19`.`classifica_notifica`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `covid-19`.`classifica_notifica` (
  `idNotificacao` INT(11) NULL DEFAULT NULL,
  `idClassificacao_final` INT(11) NULL DEFAULT NULL,
  INDEX `fk_notifica` (`idNotificacao` ASC) ,
  INDEX `fk_classifica` (`idClassificacao_final` ASC) ,
  CONSTRAINT `fk_classifica`
    FOREIGN KEY (`idClassificacao_final`)
    REFERENCES `covid-19`.`classificacao_final` (`idClassificacao_final`),
  CONSTRAINT `fk_notifica`
    FOREIGN KEY (`idNotificacao`)
    REFERENCES `covid-19`.`notificacao` (`idNotificacao`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;


-- -----------------------------------------------------
-- Table `covid-19`.`comorbidades_pacientes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `covid-19`.`comorbidades_pacientes` (
  `comorbidadeID` INT(11) NOT NULL,
  `PacienteId` INT(11) NOT NULL,
  PRIMARY KEY (`comorbidadeID`, `PacienteId`),
  INDEX `PacienteId` (`PacienteId` ASC) ,
  CONSTRAINT `comorbidades_pacientes_ibfk_1`
    FOREIGN KEY (`PacienteId`)
    REFERENCES `covid-19`.`pacientes` (`PacienteId`),
  CONSTRAINT `comorbidades_pacientes_ibfk_2`
    FOREIGN KEY (`comorbidadeID`)
    REFERENCES `covid-19`.`comorbidades` (`idComorbidades`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;


-- -----------------------------------------------------
-- Table `covid-19`.`isolament_domiciliar`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `covid-19`.`isolament_domiciliar` (
  `idisolament_domiciliar` INT(11) NOT NULL,
  `descricao` VARCHAR(150) NULL DEFAULT NULL COMMENT 'dorme no mesmo quarto, dorme na mesma cama, compartilha o mesmo banheiro, compartilha a casa toda, nenhuma das respostas',
  PRIMARY KEY (`idisolament_domiciliar`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;


-- -----------------------------------------------------
-- Table `covid-19`.`pac_end`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `covid-19`.`pac_end` (
  `end_id` INT(11) NOT NULL,
  `PacienteId` INT(11) NOT NULL,
  PRIMARY KEY (`end_id`, `PacienteId`),
  INDEX `fk_pac_end` (`PacienteId` ASC) ,
  CONSTRAINT `fk_end_pac`
    FOREIGN KEY (`end_id`)
    REFERENCES `covid-19`.`enderecos` (`end_id`),
  CONSTRAINT `fk_pac_end`
    FOREIGN KEY (`PacienteId`)
    REFERENCES `covid-19`.`pacientes` (`PacienteId`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;


-- -----------------------------------------------------
-- Table `covid-19`.`paciente_sintomas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `covid-19`.`paciente_sintomas` (
  `idsintomas` INT(11) NULL DEFAULT NULL,
  `PacienteId` INT(11) NULL DEFAULT NULL,
  INDEX `fk_pac` (`PacienteId` ASC) ,
  INDEX `fk_sint` (`idsintomas` ASC) ,
  CONSTRAINT `fk_pac`
    FOREIGN KEY (`PacienteId`)
    REFERENCES `covid-19`.`pacientes` (`PacienteId`),
  CONSTRAINT `fk_sint`
    FOREIGN KEY (`idsintomas`)
    REFERENCES `covid-19`.`sintomas` (`idsintomas`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;


-- -----------------------------------------------------
-- Table `covid-19`.`tele_atendimento_novos_sintomas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `covid-19`.`tele_atendimento_novos_sintomas` (
  `id_tele` INT(11) NOT NULL,
  `id_sintomas_novos` INT(11) NOT NULL,
  PRIMARY KEY (`id_tele`, `id_sintomas_novos`),
  INDEX `fk_sint_tele_idx` (`id_sintomas_novos` ASC) ,
  CONSTRAINT `fk_sint_tele`
    FOREIGN KEY (`id_sintomas_novos`)
    REFERENCES `covid-19`.`sintomas` (`idsintomas`),
  CONSTRAINT `fk_tele_sinto`
    FOREIGN KEY (`id_tele`)
    REFERENCES `covid-19`.`tele_atendimento` (`idteleatendimento`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;


CREATE TABLE IF NOT EXISTS `covid-19`.`adm_saude` (
  `idadm_saude` INT(11) NOT NULL,
  `nome` VARCHAR(150) NULL DEFAULT NULL,
  `CRM` VARCHAR(20) NULL DEFAULT NULL,
  PRIMARY KEY (`idadm_saude`),
  UNIQUE INDEX `CRM` (`CRM` ASC) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin
COMMENT = 'profissional de sa�de respons�vel pela notifica��o, ou teleatendimento';


-- -----------------------------------------------------
-- Table `covid-19`.`amostra`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `covid-19`.`amostra` (
  `amostra_id` INT(11) NOT NULL,
  `descricao` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`amostra_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;


-- -----------------------------------------------------
-- Table `covid-19`.`coleta`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `covid-19`.`coleta` (
  `idColeta_amostra` INT(11) NOT NULL,
  `descricao` VARCHAR(45) NULL DEFAULT NULL,
  `data_coleta` DATE NULL DEFAULT NULL,
  `id_amostra` INT(11) NULL DEFAULT NULL,
  PRIMARY KEY (`idColeta_amostra`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;


-- -----------------------------------------------------
-- Table `covid-19`.`evolucao_caso`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `covid-19`.`evolucao_caso` (
  `idevolucao` INT(11) NOT NULL,
  `descricao` VARCHAR(100) NULL DEFAULT NULL,
  PRIMARY KEY (`idevolucao`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;


-- -----------------------------------------------------
-- Table `covid-19`.`pacientes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `covid-19`.`pacientes` (
  `nome` VARCHAR(150) NULL AFTER `raca`,
  `cpf` INT NULL AFTER `nome`,
  `cpf_UNIQUE` (`cpf` ASC) VISIBLE;
  `PacienteId` INT(11) NOT NULL AUTO_INCREMENT,
  `sexo` VARCHAR(2) NOT NULL,
  `data_nasc` DATE NULL DEFAULT NULL,
  `raca` VARCHAR(35) NULL DEFAULT NULL,
  PRIMARY KEY (`PacienteId`))

ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;


-- -----------------------------------------------------
-- Table `covid-19`.`notificacao`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `covid-19`.`notificacao` (
  `idNotificacao` INT(11) NOT NULL,
  `idpac` INT(11) NOT NULL,
  `Datapreencimento` DATE NULL DEFAULT NULL,
  `Data_sintomas` DATE NULL DEFAULT NULL,
  `id_evolucao_caso` INT(11) NULL DEFAULT NULL,
  `adm_saude` INT(11) NULL DEFAULT NULL,
  PRIMARY KEY (`idNotificacao`, `idpac`),
  INDEX `notifica_pac_idx` (`idpac` ASC) ,
  INDEX `fk_notifica_evolucao_idx` (`id_evolucao_caso` ASC) ,
  INDEX `fk_adm_notifica_idx` (`adm_saude` ASC) ,
  CONSTRAINT `fk_adm_notifica`
    FOREIGN KEY (`adm_saude`)
    REFERENCES `covid-19`.`adm_saude` (`idadm_saude`),
  CONSTRAINT `fk_notifica_evolucao`
    FOREIGN KEY (`id_evolucao_caso`)
    REFERENCES `covid-19`.`evolucao_caso` (`idevolucao`),
  CONSTRAINT `notifica_pac`
    FOREIGN KEY (`idpac`)
    REFERENCES `covid-19`.`pacientes` (`PacienteId`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;


-- -----------------------------------------------------
-- Table `covid-19`.`classificacao_final`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `covid-19`.`classificacao_final` (
  `idClassificacao_final` INT(11) NOT NULL,
  `Descricao` VARCHAR(55) NULL DEFAULT NULL,
  PRIMARY KEY (`idClassificacao_final`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;


-- -----------------------------------------------------
-- Table `covid-19`.`comorbidades`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `covid-19`.`comorbidades` (
  `idComorbidades` INT(11) NOT NULL,
  `Descri��o` VARCHAR(150) NOT NULL,
  PRIMARY KEY (`idComorbidades`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;


-- -----------------------------------------------------
-- Table `covid-19`.`criterio_encerramento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `covid-19`.`criterio_encerramento` (
  `idCriterio_encerramento` INT(11) NOT NULL,
  `Descricao` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`idCriterio_encerramento`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;


-- -----------------------------------------------------
-- Table `covid-19`.`enderecos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `covid-19`.`enderecos` (
  `end_id` INT(11) NOT NULL AUTO_INCREMENT,
  `address` VARCHAR(50) NULL DEFAULT NULL,
  `bairro` VARCHAR(20) NULL DEFAULT NULL,
  `postal_code` VARCHAR(10) NULL DEFAULT NULL,
  `cidade` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`end_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;


-- -----------------------------------------------------
-- Table `covid-19`.`suporte_ventilatorio`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `covid-19`.`suporte_ventilatorio` (
  `idsuporte_Ventilatorio` INT(11) NOT NULL,
  `descricao` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`idsuporte_Ventilatorio`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;


-- -----------------------------------------------------
-- Table `covid-19`.`internacao`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `covid-19`.`internacao` (
  `idInternacao` INT(11) NOT NULL,
  `UnidadeSaude` VARCHAR(45) NULL DEFAULT NULL,
  `Data_entrada` DATE NULL DEFAULT NULL,
  `Data_saida` DATE NULL DEFAULT NULL,
  `CodPaciente` INT(11) NULL DEFAULT NULL,
  `UTI` VARCHAR(45) NULL DEFAULT NULL,
  `CodSuporteVentilatorio` INT(11) NULL DEFAULT NULL,
  `Criterio_encerramento` INT(11) NULL DEFAULT NULL,
  `obito` VARCHAR(45) NULL DEFAULT NULL,
  `adm_saude` INT(11) NULL DEFAULT NULL,
  PRIMARY KEY (`idInternacao`),
  INDEX `idpac_idx` (`CodPaciente` ASC) ,
  INDEX `idcriterio_idx` (`Criterio_encerramento` ASC) ,
  INDEX `idsuporte_idx` (`CodSuporteVentilatorio` ASC) ,
  INDEX `fk_adm_saude_idx` (`adm_saude` ASC) ,
  CONSTRAINT `fk_adm_saude`
    FOREIGN KEY (`adm_saude`)
    REFERENCES `covid-19`.`adm_saude` (`idadm_saude`),
  CONSTRAINT `idcriterio`
    FOREIGN KEY (`Criterio_encerramento`)
    REFERENCES `covid-19`.`criterio_encerramento` (`idCriterio_encerramento`),
  CONSTRAINT `idpac`
    FOREIGN KEY (`CodPaciente`)
    REFERENCES `covid-19`.`pacientes` (`PacienteId`),
  CONSTRAINT `idsuporte`
    FOREIGN KEY (`CodSuporteVentilatorio`)
    REFERENCES `covid-19`.`suporte_ventilatorio` (`idsuporte_Ventilatorio`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;


-- -----------------------------------------------------
-- Table `covid-19`.`isolament_domiciliar`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `covid-19`.`isolament_domiciliar` (
  `idisolament_domiciliar` INT(11) NOT NULL,
  `descricao` VARCHAR(150) NULL DEFAULT NULL COMMENT 'dorme no mesmo quarto, dorme na mesma cama, compartilha o mesmo banheiro, compartilha a casa toda, nenhuma das respostas',
  PRIMARY KEY (`idisolament_domiciliar`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;


-- -----------------------------------------------------
-- Table `covid-19`.`isolamento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `covid-19`.`isolamento` (
  `idisolamento` INT(11) NOT NULL,
  `descricao` VARCHAR(150) NULL DEFAULT NULL,
  PRIMARY KEY (`idisolamento`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;


-- -----------------------------------------------------
-- Table `covid-19`.`outros_moradores`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `covid-19`.`outros_moradores` (
  `id_outros_moradores` INT(11) NOT NULL,
  `id_paciente` INT(11) NULL DEFAULT NULL,
  `id_notifica` INT(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id_outros_moradores`),
  INDEX `fk_paciente_idx` (`id_paciente` ASC) ,
  INDEX `fk_notifica_idx` (`id_notifica` ASC) ,
  CONSTRAINT `fk_notifica_morador`
    FOREIGN KEY (`id_notifica`)
    REFERENCES `covid-19`.`notificacao` (`idNotificacao`),
  CONSTRAINT `fk_paciente`
    FOREIGN KEY (`id_paciente`)
    REFERENCES `covid-19`.`pacientes` (`PacienteId`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;


-- -----------------------------------------------------
-- Table `covid-19`.`sintomas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `covid-19`.`sintomas` (
  `idsintomas` INT(11) NOT NULL,
  `Descricao` VARCHAR(100) NULL DEFAULT NULL,
  PRIMARY KEY (`idsintomas`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;


-- -----------------------------------------------------
-- Table `covid-19`.`tele_atendimento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `covid-19`.`tele_atendimento` (
  `idteleatendimento` INT(11) NOT NULL,
  `adm_saude` INT(11) NULL DEFAULT NULL,
  `atendimento_realizado` VARCHAR(4) NULL DEFAULT NULL,
  `motivo_falha` VARCHAR(45) NULL DEFAULT NULL,
  `novos_sintomas` VARCHAR(4) NULL DEFAULT NULL,
  `medica�ao` VARCHAR(150) NULL DEFAULT NULL,
  `indica�ao medicacao` VARCHAR(45) NULL DEFAULT NULL,
  `teleatendimentocol` VARCHAR(45) NULL DEFAULT NULL,
  `tem_outros_moradores` VARCHAR(45) NULL DEFAULT NULL,
  `fazendo_isolamento` VARCHAR(45) NULL DEFAULT NULL,
  `tipo_isolamento` INT(11) NULL DEFAULT NULL,
  `tem_trabalho_externo` VARCHAR(45) NULL DEFAULT NULL,
  `tipo_trabalho` VARCHAR(45) NULL DEFAULT NULL,
  `dias_isolamento` INT(3) NULL DEFAULT NULL,
  `situacao_familiar` VARCHAR(45) NULL DEFAULT NULL COMMENT 'tipo de situa��o:  sai para trabalho essencial apenas, sai somente para atvidades essenciais , sai para atividades n�o essenciais 9exercicios, visitas familiares, etc)',
  `mora_sozinho` VARCHAR(4) NULL DEFAULT NULL,
  `tele_atendimentocol` VARCHAR(45) NULL DEFAULT NULL,
  `iso_domiciliar` INT(11) NULL DEFAULT NULL,
  `outro_morador_sintomas` VARCHAR(4) NULL DEFAULT NULL,
  `data_atendimento` DATE NULL DEFAULT NULL,
  `data_proximo_atendimento` DATE NULL DEFAULT NULL,
  PRIMARY KEY (`idteleatendimento`),
  INDEX `fk_adm_tele_idx` (`adm_saude` ASC) ,
  INDEX `fk_tipo_isola_idx` (`tipo_isolamento` ASC) ,
  INDEX `fk-isola_domi_idx` (`iso_domiciliar` ASC) ,
  CONSTRAINT `fk-isola_domi`
    FOREIGN KEY (`iso_domiciliar`)
    REFERENCES `covid-19`.`isolament_domiciliar` (`idisolament_domiciliar`),
  CONSTRAINT `fk_adm_tele`
    FOREIGN KEY (`adm_saude`)
    REFERENCES `covid-19`.`adm_saude` (`idadm_saude`),
  CONSTRAINT `fk_tipo_isola`
    FOREIGN KEY (`tipo_isolamento`)
    REFERENCES `covid-19`.`isolamento` (`idisolamento`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin
COMMENT = 'vinculada a tabela de notifica��o';


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
