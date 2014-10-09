-- MySQL dump 10.13  Distrib 5.6.21, for Win32 (x86)
--
-- Host: localhost    Database: lsh
-- ------------------------------------------------------
-- Server version	5.6.21

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
-- Table structure for table `movie4`
--

DROP TABLE IF EXISTS `movie4`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `movie4` (
  `name` varchar(64) CHARACTER SET utf8 DEFAULT NULL,
  `director` varchar(64) CHARACTER SET utf8 DEFAULT NULL,
  `actor` varchar(256) CHARACTER SET utf8 DEFAULT NULL,
  `location` varchar(128) CHARACTER SET utf8 DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=gbk;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movie4`
--

LOCK TABLES `movie4` WRITE;
/*!40000 ALTER TABLE `movie4` DISABLE KEYS */;
INSERT INTO `movie4` VALUES ('罪恶之城2','罗伯特·罗德里格兹','米基·洛克','http://img3.douban.com/view/movie_poster_cover/spst/public/p2193680612.jpg'),('彗星来的那一夜','詹姆斯·沃德·布柯特','艾米丽·芭尔多尼','http://img3.douban.com/view/movie_poster_cover/spst/public/p2179310921.jpg'),('海雾','沈成宝','金允石','http://img5.douban.com/view/movie_poster_cover/spst/public/p2190930188.jpg'),('上帝帮助女孩','Stuart Murdoch','汉娜·穆雷','http://img5.douban.com/view/movie_poster_cover/spst/public/p2172148817.jpg'),('神的病历簿2','深川荣洋','樱井翔','http://img3.douban.com/view/movie_poster_cover/spst/public/p2153428101.jpg'),('行过死荫之地','斯科特·弗兰克','连姆·尼森','http://img3.douban.com/view/movie_poster_cover/spst/public/p2185337913.jpg'),('超体','吕克·贝松','斯嘉丽·约翰逊','http://img3.douban.com/view/movie_poster_cover/spst/public/p2201909284.jpg'),('歌曲改变人生','约翰·卡尼','詹姆斯·柯登','http://img5.douban.com/view/movie_poster_cover/spst/public/p2180002996.jpg'),('弗兰克','伦尼·阿伯拉罕森','迈克尔·法斯宾德','http://img5.douban.com/view/movie_poster_cover/spst/public/p2195768476.jpg'),('摩纳哥王妃','奥利维耶·达昂','妮可·基德曼','http://img3.douban.com/view/movie_poster_cover/spst/public/p2185958530.jpg'),('落魄大厨','乔恩·费儒','乔恩·费儒','http://img3.douban.com/view/movie_poster_cover/spst/public/p2199407040.jpg'),('龙虎少年队2','菲尔·罗德','乔纳·希尔','http://img3.douban.com/view/movie_poster_cover/spst/public/p2177364785.jpg'),('空中营救','佐米·希尔拉','连姆·尼森','http://img3.douban.com/view/movie_poster_cover/spst/public/p2199638985.jpg'),('星运里的错','约什·布恩','谢琳·伍德蕾','http://img3.douban.com/view/movie_poster_cover/spst/public/p2197059721.jpg'),('道熙呀','郑朱莉','裴斗娜','http://img3.douban.com/view/movie_poster_cover/spst/public/p2180405730.jpg'),('白雪公主杀人事件','中村义洋','井上真央','http://img3.douban.com/view/movie_poster_cover/spst/public/p2176900061.jpg'),('辩护人','杨宇锡','宋康昊','http://img3.douban.com/view/movie_poster_cover/spst/public/p2158166535.jpg'),('少年时代','理查德·林克莱特','埃拉·科尔特兰','http://img5.douban.com/view/movie_poster_cover/spst/public/p2187391526.jpg'),('她','斯派克·琼斯','杰昆·菲尼克斯','http://img5.douban.com/view/movie_poster_cover/spst/public/p2166850749.jpg'),('闺蜜','黄真真','陈意涵','http://img5.douban.com/view/movie_poster_cover/spst/public/p2188986448.jpg'),('明日边缘','道格·里曼','汤姆·克鲁斯','http://img5.douban.com/view/movie_poster_cover/spst/public/p2185073849.jpg'),('绣春刀','路阳','张震','http://img3.douban.com/view/movie_poster_cover/spst/public/p2194066391.jpg'),('一代宗师','王家卫','梁朝伟','http://img5.douban.com/view/movie_poster_cover/spst/public/p2202375207.jpg'),('后会无期','韩寒','冯绍峰','http://img3.douban.com/view/movie_poster_cover/spst/public/p2192267510.jpg'),('驯龙高手2','迪恩·德布洛斯','杰伊·巴鲁切尔','http://img5.douban.com/view/movie_poster_cover/spst/public/p2192713707.jpg');
/*!40000 ALTER TABLE `movie4` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-10-08 21:33:44
