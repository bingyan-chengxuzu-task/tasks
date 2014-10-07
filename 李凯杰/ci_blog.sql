/*
hongwenwu
MySQL Data Transfer
Source Host: localhost
Source Database: ci_blog
Target Host: localhost
Target Database: blog
Date: 2011-3-24 17:30:30
*/

SET FOREIGN_KEY_CHECKS=0;
CREATE DATABASE ci_blog;
USE ci_blog;
-- ----------------------------
-- Table structure for comments
-- ----------------------------
CREATE TABLE `comments` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `entry_id` INT(11) DEFAULT NULL,
  `body` TEXT,
  `author` VARCHAR(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MYISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for entries
-- ----------------------------
CREATE TABLE `entries` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(128) DEFAULT NULL,
  `body` TEXT,
  PRIMARY KEY (`id`)
) ENGINE=MYISAM DEFAULT CHARSET=utf8;

