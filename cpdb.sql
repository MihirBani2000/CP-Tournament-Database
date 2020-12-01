-- MySQL dump 10.13  Distrib 8.0.21, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: CPTOURNAMENT
-- ------------------------------------------------------
-- Server version	8.0.21

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


DROP Database IF EXISTS `CPTOURNAMENT`;
CREATE Database `CPTOURNAMENT`;
USE `CPTOURNAMENT`;


--
-- Table structure for table `CONTEST`
--

DROP TABLE IF EXISTS `CONTEST`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `CONTEST` (
  `ContestID` int NOT NULL,
  `StartTime` datetime NOT NULL,
  `Duration` time NOT NULL,
  PRIMARY KEY (`ContestID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CONTEST`
--

LOCK TABLES `CONTEST` WRITE;
/*!40000 ALTER TABLE `CONTEST` DISABLE KEYS */;
/*!40000 ALTER TABLE `CONTEST` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CONTESTANT`
--

DROP TABLE IF EXISTS `CONTESTANT`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `CONTESTANT` (
  `ProgrammerID` int NOT NULL,
  `CollegeYear` int DEFAULT NULL,
  `TNo` int,
  PRIMARY KEY (`ProgrammerID`),
  KEY `TNo` (`TNo`),
  CONSTRAINT `CONTESTANT_ibfk_1` FOREIGN KEY (`ProgrammerID`) REFERENCES `PROGRAMMER` (`ProgrammerID`)
    ON UPDATE CASCADE ON DELETE CASCADE,
  CONSTRAINT `CONTESTANT_ibfk_2` FOREIGN KEY (`TNo`) REFERENCES `TEAM` (`TNo`)
    ON UPDATE CASCADE ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CONTESTANT`
--

LOCK TABLES `CONTESTANT` WRITE;
/*!40000 ALTER TABLE `CONTESTANT` DISABLE KEYS */;
/*!40000 ALTER TABLE `CONTESTANT` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CONTESTLANGUAGES`
--

DROP TABLE IF EXISTS `CONTESTLANGUAGES`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `CONTESTLANGUAGES` (
  `ContestID` int NOT NULL,
  `AllowedLanguages` varchar(255) NOT NULL,
  PRIMARY KEY (`ContestID`,`AllowedLanguages`),
  CONSTRAINT `CONTESTLANGUAGES_ibfk_1` FOREIGN KEY (`ContestID`) REFERENCES `CONTEST` (`ContestID`)
    ON UPDATE CASCADE ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CONTESTLANGUAGES`
--

LOCK TABLES `CONTESTLANGUAGES` WRITE;
/*!40000 ALTER TABLE `CONTESTLANGUAGES` DISABLE KEYS */;
/*!40000 ALTER TABLE `CONTESTLANGUAGES` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PARTICIPATES`
--

DROP TABLE IF EXISTS `PARTICIPATES`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `PARTICIPATES` (
  `TNo` int NOT NULL,
  `ContestID` int NOT NULL,
  PRIMARY KEY (`TNo`,`ContestID`),
  KEY `ContestID` (`ContestID`),
  CONSTRAINT `PARTICIPATES_ibfk_1` FOREIGN KEY (`ContestID`) REFERENCES `CONTEST` (`ContestID`)
    ON UPDATE CASCADE ON DELETE CASCADE,
  CONSTRAINT `PARTICIPATES_ibfk_2` FOREIGN KEY (`TNo`) REFERENCES `TEAM` (`TNo`)
    ON UPDATE CASCADE ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PARTICIPATES`
--

LOCK TABLES `PARTICIPATES` WRITE;
/*!40000 ALTER TABLE `PARTICIPATES` DISABLE KEYS */;
/*!40000 ALTER TABLE `PARTICIPATES` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PROBLEM`
--

DROP TABLE IF EXISTS `PROBLEM`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `PROBLEM` (
  `ContestID` int NOT NULL,
  `ProblemName` varchar(255) NOT NULL,
  `Maxpoints` int NOT NULL,
  `Pstatement` text,
  `TestIO` text,
  `SampleIO` text,
  `IOFormat` varchar(2000) DEFAULT NULL,
  `Memory` int DEFAULT NULL,
  `Runtime` time DEFAULT NULL,
  PRIMARY KEY (`ContestID`,`ProblemName`),
  CONSTRAINT `PROBLEM_ibfk_1` FOREIGN KEY (`ContestID`) REFERENCES `CONTEST` (`ContestID`)
    ON UPDATE CASCADE ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PROBLEM`
--

LOCK TABLES `PROBLEM` WRITE;
/*!40000 ALTER TABLE `PROBLEM` DISABLE KEYS */;
/*!40000 ALTER TABLE `PROBLEM` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PROBLEMAUTHOR`
--

DROP TABLE IF EXISTS `PROBLEMAUTHOR`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `PROBLEMAUTHOR` (
  `ProgrammerID` int NOT NULL,
  `ContestID` int NOT NULL,
  `ProblemName` varchar(255) NOT NULL,
  PRIMARY KEY (`ProgrammerID`,`ContestID`,`ProblemName`),
  KEY `ContestID` (`ContestID`,`ProblemName`),
  CONSTRAINT `PROBLEMAUTHOR_ibfk_1` FOREIGN KEY (`ProgrammerID`) REFERENCES `PROBLEMSETTER` (`ProgrammerID`)
    ON UPDATE CASCADE ON DELETE CASCADE,
  CONSTRAINT `PROBLEMAUTHOR_ibfk_2` FOREIGN KEY (`ContestID`, `ProblemName`) REFERENCES `PROBLEM` (`ContestID`, `ProblemName`)
    ON UPDATE CASCADE ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PROBLEMAUTHOR`
--

LOCK TABLES `PROBLEMAUTHOR` WRITE;
/*!40000 ALTER TABLE `PROBLEMAUTHOR` DISABLE KEYS */;
/*!40000 ALTER TABLE `PROBLEMAUTHOR` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PROBLEMSETTER`
--

DROP TABLE IF EXISTS `PROBLEMSETTER`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `PROBLEMSETTER` (
  `ProgrammerID` int NOT NULL,
  `Numofproblems` int DEFAULT NULL,
  `Experience` int DEFAULT NULL,
  PRIMARY KEY (`ProgrammerID`),
  CONSTRAINT `PROBLEMSETTER_ibfk_1` FOREIGN KEY (`ProgrammerID`) REFERENCES `PROGRAMMER` (`ProgrammerID`)
    ON UPDATE CASCADE ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PROBLEMSETTER`
--

LOCK TABLES `PROBLEMSETTER` WRITE;
/*!40000 ALTER TABLE `PROBLEMSETTER` DISABLE KEYS */;
/*!40000 ALTER TABLE `PROBLEMSETTER` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PROBLEMTAGS`
--

DROP TABLE IF EXISTS `PROBLEMTAGS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `PROBLEMTAGS` (
  `ContestID` int NOT NULL,
  `ProblemName` varchar(255) NOT NULL,
  `Tags` varchar(255) NOT NULL,
  PRIMARY KEY (`ContestID`,`ProblemName`,`Tags`),
  CONSTRAINT `PROBLEMTAGS_ibfk_1` FOREIGN KEY (`ContestID`, `ProblemName`) 
    REFERENCES `PROBLEM` (`ContestID`, `ProblemName`)
      ON UPDATE CASCADE ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PROBLEMTAGS`
--

LOCK TABLES `PROBLEMTAGS` WRITE;
/*!40000 ALTER TABLE `PROBLEMTAGS` DISABLE KEYS */;
/*!40000 ALTER TABLE `PROBLEMTAGS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PROGRAMMER`
--

DROP TABLE IF EXISTS `PROGRAMMER`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `PROGRAMMER` (
  `ProgrammerID` int NOT NULL,
  `EmailID` varchar(255) NOT NULL,
  `Fname` varchar(255) NOT NULL,
  `Lname` varchar(255) NOT NULL,
  `Nationality` varchar(255) DEFAULT NULL,
  `Age` int DEFAULT NULL,
  `Is_graduate` int NOT NULL,
  PRIMARY KEY (`ProgrammerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PROGRAMMER`
--

LOCK TABLES `PROGRAMMER` WRITE;
/*!40000 ALTER TABLE `PROGRAMMER` DISABLE KEYS */;
/*!40000 ALTER TABLE `PROGRAMMER` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SUBMISSION`
--

DROP TABLE IF EXISTS `SUBMISSION`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `SUBMISSION` (
  `SubID` int NOT NULL AUTO_INCREMENT,
  `Language` varchar(255) NOT NULL,
  `SubTime` time NOT NULL,
  `VERDICT` varchar(255) NOT NULL,
  `POINTS` int NOT NULL,
  `MEMORY` int DEFAULT NULL,
  `RUNTIME` int DEFAULT NULL,
  PRIMARY KEY (`SubID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SUBMISSION`
--

LOCK TABLES `SUBMISSION` WRITE;
/*!40000 ALTER TABLE `SUBMISSION` DISABLE KEYS */;
/*!40000 ALTER TABLE `SUBMISSION` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SUBMITS`
--

DROP TABLE IF EXISTS `SUBMITS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `SUBMITS` (
  `TNo` int NOT NULL,
  `ContestID` int NOT NULL,
  `ProblemName` varchar(255) NOT NULL,
  `SubID` int NOT NULL,
  PRIMARY KEY (`TNo`,`ContestID`,`ProblemName`,`SubID`),
  KEY `ContestID` (`ContestID`,`ProblemName`),
  KEY `SubID` (`SubID`),
  CONSTRAINT `SUBMITS_ibfk_1` FOREIGN KEY (`TNo`) REFERENCES `TEAM` (`TNo`)
    ON UPDATE CASCADE ON DELETE CASCADE,
  CONSTRAINT `SUBMITS_ibfk_2` FOREIGN KEY (`ContestID`, `ProblemName`) 
    REFERENCES `PROBLEM` (`ContestID`, `ProblemName`)
      ON UPDATE CASCADE ON DELETE CASCADE,
  CONSTRAINT `SUBMITS_ibfk_3` FOREIGN KEY (`SubID`) REFERENCES `SUBMISSION` (`SubID`)
    ON UPDATE CASCADE ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SUBMITS`
--

LOCK TABLES `SUBMITS` WRITE;
/*!40000 ALTER TABLE `SUBMITS` DISABLE KEYS */;
/*!40000 ALTER TABLE `SUBMITS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SUBPROBLEM`
--

DROP TABLE IF EXISTS `SUBPROBLEM`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `SUBPROBLEM` (
  `ContestID` int NOT NULL,
  `ProblemName` varchar(255) NOT NULL,
  `ParentProblemName` varchar(255) NOT NULL,
  PRIMARY KEY (`ContestID`,`ProblemName`),
  CONSTRAINT `SUBPROBLEM_ibfk_1` FOREIGN KEY (`ContestID`, `ParentProblemName`) 
    REFERENCES `PROBLEM` (`ContestID`, `ProblemName`)
      ON UPDATE CASCADE ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SUBPROBLEM`
--

LOCK TABLES `SUBPROBLEM` WRITE;
/*!40000 ALTER TABLE `SUBPROBLEM` DISABLE KEYS */;
/*!40000 ALTER TABLE `SUBPROBLEM` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TEAM`
--

DROP TABLE IF EXISTS `TEAM`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `TEAM` (
  `TNo` int NOT NULL,
  `TName` varchar(255) NOT NULL,
  `CollegeName` varchar(255) DEFAULT NULL,
  `LeaderID` int UNIQUE DEFAULT NULL ,
  PRIMARY KEY (`TNo`),
  CONSTRAINT `TEAM_ibfk_1` FOREIGN KEY (`LeaderID`) REFERENCES `CONTESTANT` (`ProgrammerID`)
    ON UPDATE CASCADE ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
--
-- Dumping data for table `TEAM`
--

LOCK TABLES `TEAM` WRITE;
/*!40000 ALTER TABLE `TEAM` DISABLE KEYS */;
/*!40000 ALTER TABLE `TEAM` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
INSERT INTO CONTEST VALUES 
(1, '2020-01-01 18:00:00', '02:00:00'),
(2,'2019-08-01 15:00:00','02:00:00'),
(3,'2020-01-06 16:00:00', '02:00:00') ;

INSERT INTO CONTESTLANGUAGES VALUES 
(1, 'C++'), (1, 'C'), (1, 'Python'),
(2,'JAVA'), (2,'Python'), (2,'C++'), (2,'RUBY'),
(3,'C'), (3,'C#'), (3,'C++'), (3,'RUBY');

INSERT INTO PROGRAMMER VALUES
(1,'numberdedopls@gmail.com', 'Bhavyajeet' ,'Singh','India','20','0'),
(2,'sirplsgivemarks@gmail.com', 'Jaidev', 'Sriram','India',20,'0'),
(3,'maampls@gmail.com', 'Jyoti' , 'Sunkara','India','20','0'),
(4,'Charaswati@gmail.com', 'Ashish' , 'Gupta','India','19','0'),
(5,'ArnabGoswami@gmail.com','Rutvij', 'Menavlikar','India','19','0'),
(6,'BONDOP@gmail.com', 'Anvay' , 'Karmore','India','19','0'),
(7,'multiplexer@gmail.com', 'Tejas' , 'Chaudhari','India','19','0'),
(8,'sidthesloth@gmail.com', 'Jaywant' , 'Patel','India','12','0'),
(9,'randibaaz@gmail.com', 'Aditya' , 'Verma','India','19','0'),
(10,'tyrantmf@gmail.com', 'Xi' ,'Jinping','China','29','1'),
(11,'momowala@gmail.com', 'Kim','Jong-Un','North Korea','25','1'),
(12,'omshaantiom@jaishreeram.com', 'Dalai','Lama','Nepal','35','1'),
(13,'orangeblob@whodoesntliketheirdaughtersass.com', 'Donald','Trump','USA','69','1');

INSERT INTO TEAM VALUES
(1,'3NOOBS','IIIT Hyderabad',NULL),
(2,'HighHopes','IIIT Hyderabad',NULL),
(3,'Manforce', 'IIT Hyderabad',NULL);

INSERT INTO CONTESTANT VALUES
(1,3,1),(2,3,1),(3,3,1),
(4,2,2),(5,2,2),(6,2,2),
(7,2,3),(8,2,3),(9,2,3);

INSERT INTO PARTICIPATES VALUES
(1,1),(2,1),(3,1),(1,2),(2,2),(3,2),(2,3),(3,3);


INSERT INTO PROBLEM VALUES
(1,'A',500,'Problem statement for problem A contest 1','sample test','IOFORMAT','sample io',500,'00:30:00'),
(1,'B',750,'Problem statement for problem B contest 1','sample test','IOFORMAT','sample io',500,'00:40:00'),
(1,'C',1000,'Problem statement for problem C contest 1','sample test','IOFORMAT','sample io',500,'00:50:00'),
(1,'D',2000,'Problem statement for problem D contest 1','sample test','IOFORMAT','sample io',500,'00:10:00'),
(2,'A',500,'Problem statement for problem A contest 2','sample test','IOFORMAT','sample io',500,'00:30:00'),
(2,'B',750,'Problem statement for problem B contest 2','sample test','IOFORMAT','sample io',500,'00:40:00'),
(3,'A',500,'Problem statement for problem A contest 3','sample test','IOFORMAT','sample io',500,'00:10:00'),
(3,'B',750,'Problem statement for problem B contest 3','sample test','IOFORMAT','sample io',500,'00:20:00');


INSERT INTO SUBMISSION VALUES
(1,'C++','00:12:00','AC',500,125,1),(3,'C++','00:16:00','WA',0,125,1),(4,'C++','00:17:00','AC',750,125,1),
(2,'C++','00:15:00','AC',500,125,1),(6,'C++','00:20:00','AC',750,125,1),(7,'C++','01:40:00','AC',1000,125,2),
(5,'C','00:25:00','AC',500,125,1),
(8,'C++','00:21:00','AC',500,125,1),
(9,'C++','00:12:00','AC',500,125,1),(10,'C++','00:40:00','AC',700,125,1),
(11,'JAVA','01:10:00','AC',750,125,1),
(12,'C++','00:08:00','AC',500,125,1),
(13,'C++','00:12:00','AC',500,125,1),(14,'C++','00:30:00','RE',0,125,1),(15,'C++','00:45:00','AC',750,125,1),
(16,'RUBY','01:12:00','WA',0,125,1);

INSERT INTO SUBMITS VALUES
(1,1,'A',1),(1,1,'B',3),(1,1,'B',4),
(2,1,'A',2),(2,1,'B',6),(2,1,'C',7),
(3,1,'A',5),
(1,2,'A',8),
(2,2,'A',9),(2,2,'B',10),
(3,2,'B',11),
(1,3,'A',12),
(2,3,'A',13),(2,3,'B',14),(2,3,'B',15),
(3,3,'A',16);

INSERT INTO PROBLEMSETTER VALUES
(10,3,3),
(11,2,2),
(12,2,2),
(13,1,1);

INSERT INTO PROBLEMAUTHOR VALUES
(10,1,'A'),(10,2,'A'),(10,3,'A'),
(11,1,'B'),(11,2,'B'),
(12,1,'C'),(12,3,'B'),
(13,1,'D');

INSERT INTO PROBLEMTAGS VALUES
(1,'A','DP'),(1,'B','GREEDY'),(1,'C','GRAPHS'),(1,'D','FLOWS'),
(2,'A','MATH'),(2,'B','DSU'),
(3,'A','BINARY SEARCH'),(3,'B','BITMASK');

INSERT INTO SUBPROBLEM VALUES
(1,'C','B'),
(3,'B','A');
-- Dump completed on 2020-10-02  0:03:16