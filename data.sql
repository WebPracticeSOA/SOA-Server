-- MySQL dump 10.13  Distrib 5.7.29, for Win64 (x86_64)
--
-- Host: localhost    Database: exampledb6
-- ------------------------------------------------------
-- Server version	5.7.29

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `spittle`
--

DROP TABLE IF EXISTS `spittle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `spittle` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `spitter` int(11) NOT NULL,
  `message` varchar(2000) NOT NULL,
  `postedTime` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `spitter` (`spitter`),
  CONSTRAINT `spittle_ibfk_1` FOREIGN KEY (`spitter`) REFERENCES `spitter` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `spittle`
--

LOCK TABLES `spittle` WRITE;
/*!40000 ALTER TABLE `spittle` DISABLE KEYS */;
INSERT INTO `spittle` VALUES (1,1,'This is a test spittle message','2012-06-09 22:00:00'),(2,1,'This is another test spittle message','2012-06-09 22:10:00'),(3,1,'This is a third test spittle message','2012-07-04 23:30:00'),(4,2,'Hello from Chuck!','2012-03-25 12:15:00'),(5,4,'Hello from Art!','2012-03-25 12:15:00'),(6,4,'Hello again from Art!','2012-03-25 12:25:00'),(7,4,'Hola from Arthur!','2012-03-25 12:35:00'),(8,4,'Buenos Dias from Art!','2012-03-25 12:45:00'),(9,4,'Ni Hao from Art!','2012-03-25 12:55:00'),(10,4,'Guten Tag from Art!','2012-03-25 13:05:00'),(11,4,'Konnichi wa from Art!','2012-03-25 13:15:00'),(12,4,'Buon giorno from Art!','2012-03-25 13:25:00'),(13,4,'Bonjour from Art!','2012-03-25 13:35:00'),(14,4,'Aloha from Art!','2012-03-25 13:45:00'),(15,4,'God dag from Art!','2012-03-25 13:55:00');
/*!40000 ALTER TABLE `spittle` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-10-27 10:16:05
