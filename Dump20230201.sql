CREATE DATABASE  IF NOT EXISTS `esquema_recetas` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `esquema_recetas`;
-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: esquema_recetas
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `recetas`
--

DROP TABLE IF EXISTS `recetas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `recetas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `description` text,
  `instruction` text,
  `date_cooked` date DEFAULT NULL,
  `under` varchar(5) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `usuario_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_recetas_usuarios_idx` (`usuario_id`),
  CONSTRAINT `fk_recetas_usuarios` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recetas`
--

LOCK TABLES `recetas` WRITE;
/*!40000 ALTER TABLE `recetas` DISABLE KEYS */;
INSERT INTO `recetas` VALUES (12,'Asado','qq','qqq','2023-01-31','Si','2023-01-31 09:00:18','2023-01-31 09:00:18',1),(13,'Mbejuu','Almidon, queso, grasa','Mezclar.','2023-01-31','No','2023-01-31 09:00:53','2023-01-31 09:00:53',1),(14,'Empanada','sdf','fsdfa','2023-01-29','No','2023-01-31 09:01:12','2023-01-31 09:01:12',1),(15,'Mbejuu','ww','ww','2023-01-31','Si','2023-01-31 09:01:47','2023-01-31 09:01:47',1),(16,'empa','jjja','jaja','2022-10-10','Si','2023-01-31 09:02:20','2023-01-31 09:02:20',1),(17,'SuperBurguer','carne, queso, tomatee','Calentar y cocinar ','2023-01-25','No','2023-01-31 09:44:17','2023-01-31 09:44:17',1),(18,'asdfsdafasdf','fadfdsafdsfa','fasdfasdfasf','1200-10-10','Si','2023-01-31 16:06:36','2023-01-31 16:06:36',1);
/*!40000 ALTER TABLE `recetas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(45) DEFAULT NULL,
  `last_name` varchar(45) DEFAULT NULL,
  `email` varchar(55) DEFAULT NULL,
  `password` varchar(500) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (1,'BENITO','ALMADA','bnito86@hotmail.com','$2b$12$TnV9n21T4ONve9UZg9acjeOeuWIBBAJ6/texsMmVv0qSFmJqfbiSO',NULL,NULL),(2,'Benito Agustín','Almada Barrios','bnito86@gmail.com','$2b$12$kokTV6z3jbFPOXxPFYCppuv4bMXZ0qy17apG.SoYQLvA8Sk/vfS0i',NULL,NULL),(4,'Raul','Perez','roa@gmail.com','$2b$12$M9yjkp39.Q9LMX40GeajvecdXfvyilBkkUeMrjzMupz6sN4p4hik.',NULL,NULL);
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-02-01 19:47:16
