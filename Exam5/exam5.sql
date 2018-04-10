-- MySQL dump 10.13  Distrib 5.7.21, for Linux (x86_64)
--
-- Host: localhost    Database: exam5
-- ------------------------------------------------------
-- Server version	5.7.21-0ubuntu0.16.04.1

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
-- Current Database: `exam5`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `exam5` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `exam5`;

--
-- Table structure for table `exam`
--

DROP TABLE IF EXISTS `exam`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `exam` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(511) DEFAULT NULL,
  `paperId` int(11) DEFAULT NULL,
  `degree` varchar(10) DEFAULT NULL,
  `startTime` datetime DEFAULT NULL,
  `endTime` datetime DEFAULT NULL,
  `ctime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `title` (`title`),
  UNIQUE KEY `paperId` (`paperId`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exam`
--

LOCK TABLES `exam` WRITE;
/*!40000 ALTER TABLE `exam` DISABLE KEYS */;
INSERT INTO `exam` VALUES (1,'1',1,'简单','2018-03-05 16:16:53','2018-03-07 16:16:56','2018-03-05 16:16:59');
/*!40000 ALTER TABLE `exam` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `history`
--

DROP TABLE IF EXISTS `history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `history` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `studyId` int(11) DEFAULT NULL,
  `studyName` int(11) DEFAULT NULL,
  `examId` int(11) DEFAULT NULL,
  `examTitle` int(11) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `score` varchar(10) DEFAULT NULL,
  `questionAanswer` varchar(511) DEFAULT NULL,
  `questionBanswer` varchar(511) DEFAULT NULL,
  `questionCanswer` varchar(511) DEFAULT NULL,
  `questionDanswer` varchar(511) DEFAULT NULL,
  `questionEanswer` varchar(511) DEFAULT NULL,
  `questionAscore` varchar(10) DEFAULT NULL,
  `questionBscore` varchar(10) DEFAULT NULL,
  `questionCscore` varchar(10) DEFAULT NULL,
  `questionDscore` varchar(10) DEFAULT NULL,
  `questionEscore` varchar(10) DEFAULT NULL,
  `ctime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `studyId` (`studyId`),
  UNIQUE KEY `studyName` (`studyName`),
  UNIQUE KEY `examId` (`examId`),
  UNIQUE KEY `examTitle` (`examTitle`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `history`
--

LOCK TABLES `history` WRITE;
/*!40000 ALTER TABLE `history` DISABLE KEYS */;
/*!40000 ALTER TABLE `history` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `paper`
--

DROP TABLE IF EXISTS `paper`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `paper` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(511) DEFAULT NULL,
  `questionAlist` varchar(100) DEFAULT NULL,
  `questionBlist` varchar(100) DEFAULT NULL,
  `questionClist` varchar(100) DEFAULT NULL,
  `questionDlist` varchar(100) DEFAULT NULL,
  `questionElist` varchar(100) DEFAULT NULL,
  `degree` varchar(10) DEFAULT NULL,
  `questionAscore` varchar(10) DEFAULT NULL,
  `questionBscore` varchar(10) DEFAULT NULL,
  `questionCscore` varchar(10) DEFAULT NULL,
  `questionDscore` varchar(10) DEFAULT NULL,
  `questionEscore` varchar(10) DEFAULT NULL,
  `ctime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `title` (`title`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `paper`
--

LOCK TABLES `paper` WRITE;
/*!40000 ALTER TABLE `paper` DISABLE KEYS */;
INSERT INTO `paper` VALUES (1,'测试卷','[2,3,4,5,6]','[7,8,9,10,11]','[12,13,14]','[17,18]','[24,25]','简单','5','6','5','5','10','2018-03-05 15:16:06');
/*!40000 ALTER TABLE `paper` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `question`
--

DROP TABLE IF EXISTS `question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `question` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(511) DEFAULT NULL,
  `qType` varchar(10) DEFAULT NULL,
  `degree` varchar(10) DEFAULT NULL,
  `options` varchar(511) DEFAULT NULL,
  `answer` varchar(64) DEFAULT NULL,
  `ctime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `title` (`title`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `question`
--

LOCK TABLES `question` WRITE;
/*!40000 ALTER TABLE `question` DISABLE KEYS */;
INSERT INTO `question` VALUES (2,'单选题一','单选题','简单','[{\"A\":\"选项一\"},{\"B\":\"选项一\"},{\"C\":\"选项一\"},{\"D\":\"选项一\"}]','A','2018-03-05 14:59:22'),(3,'单选题二','单选题','简单','[{\"A\":\"选项二\"},{\"B\":\"选项二\"},{\"C\":\"选项二\"},{\"D\":\"选项二\"}]','A','2018-03-05 14:59:22'),(4,'单选题三','单选题','简单','[{\"A\":\"选项三\"},{\"B\":\"选项三\"},{\"C\":\"选项三\"},{\"D\":\"选项三\"}]','A','2018-03-05 14:59:22'),(5,'单选题四','单选题','简单','[{\"A\":\"选项四\"},{\"B\":\"选项四\"},{\"C\":\"选项四\"},{\"D\":\"选项四\"}]','A','2018-03-05 14:59:22'),(6,'单选题五','单选题','简单','[{\"A\":\"选项五\"},{\"B\":\"选项五\"},{\"C\":\"选项五\"},{\"D\":\"选项五\"}]','A','2018-03-05 14:59:22'),(7,'多选题一','多选题','简单','[{\"A\":\"选项一\"},{\"B\":\"选项一\"},{\"C\":\"选项一\"},{\"D\":\"选项一\"}]','A','2018-03-05 14:59:22'),(8,'多选题二','多选题','简单','[{\"A\":\"选项二\"},{\"B\":\"选项二\"},{\"C\":\"选项二\"},{\"D\":\"选项二\"}]','A','2018-03-05 14:59:22'),(9,'多选题三','多选题','简单','[{\"A\":\"选项三\"},{\"B\":\"选项三\"},{\"C\":\"选项三\"},{\"D\":\"选项三\"}]','A','2018-03-05 14:59:22'),(10,'多选题四','多选题','简单','[{\"A\":\"选项四\"},{\"B\":\"选项四\"},{\"C\":\"选项四\"},{\"D\":\"选项四\"}]','A','2018-03-05 14:59:22'),(11,'多选题五','多选题','简单','[{\"A\":\"选项五\"},{\"B\":\"选项五\"},{\"C\":\"选项五\"},{\"D\":\"选项五\"}]','A','2018-03-05 14:59:22'),(12,'填空题一','填空题','简单','[]','A','2018-03-05 14:59:22'),(13,'填空题二','填空题','简单','[]','A','2018-03-05 14:59:22'),(14,'填空题三','填空题','简单','[]','A','2018-03-05 14:59:22'),(15,'填空题四','填空题','简单','[]','A','2018-03-05 14:59:22'),(16,'填空题五','填空题','简单','[]','A','2018-03-05 14:59:22'),(17,'判断题一','判断题','简单','[]','A','2018-03-05 14:59:22'),(18,'判断题二','判断题','简单','[]','A','2018-03-05 14:59:22'),(19,'判断题三','判断题','简单','[]','A','2018-03-05 14:59:22'),(20,'判断题四','判断题','简单','[]','A','2018-03-05 14:59:22'),(21,'判断题五','判断题','简单','[]','A','2018-03-05 14:59:22'),(22,'简答题一','简答题','简单','[]','A','2018-03-05 14:59:22'),(23,'简答题二','简答题','简单','[]','A','2018-03-05 14:59:22'),(24,'简答题三','简答题','简单','[]','A','2018-03-05 14:59:22'),(25,'简答题四','简答题','简单','[]','A','2018-03-05 14:59:22'),(26,'简答题五','简答题','简单','[]','A','2018-03-05 14:59:22');
/*!40000 ALTER TABLE `question` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `token`
--

DROP TABLE IF EXISTS `token`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `token` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userId` int(11) DEFAULT NULL,
  `accessToken` varchar(32) DEFAULT NULL,
  `ctime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `userId` (`userId`),
  UNIQUE KEY `accessToken` (`accessToken`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `token`
--

LOCK TABLES `token` WRITE;
/*!40000 ALTER TABLE `token` DISABLE KEYS */;
INSERT INTO `token` VALUES (1,1,'64ad7c2d53fcacd7','2018-03-05 16:19:31');
/*!40000 ALTER TABLE `token` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `studyId` varchar(32) DEFAULT NULL,
  `studyName` varchar(64) DEFAULT NULL,
  `password` varchar(64) DEFAULT NULL,
  `loginName` varchar(32) NOT NULL,
  `ctime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `studyId` (`studyId`),
  UNIQUE KEY `studyName` (`studyName`),
  UNIQUE KEY `password` (`password`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'1','123','123456','test',NULL);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-04-10 16:30:41
