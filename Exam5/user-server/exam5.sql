/*
 Navicat MySQL Data Transfer

 Source Server         : l
 Source Server Type    : MySQL
 Source Server Version : 50721
 Source Host           : localhost:3306
 Source Schema         : exam5

 Target Server Type    : MySQL
 Target Server Version : 50721
 File Encoding         : 65001

 Date: 05/03/2018 20:56:08
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for exam
-- ----------------------------
DROP TABLE IF EXISTS `exam`;
CREATE TABLE `exam`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(511) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `paperId` int(11) NULL DEFAULT NULL,
  `degree` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `startTime` datetime(0) NULL DEFAULT NULL,
  `endTime` datetime(0) NULL DEFAULT NULL,
  `ctime` datetime(0) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `title`(`title`) USING BTREE,
  UNIQUE INDEX `paperId`(`paperId`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of exam
-- ----------------------------
INSERT INTO `exam` VALUES (1, '1', 1, '简单', '2018-03-05 16:16:53', '2018-03-07 16:16:56', '2018-03-05 16:16:59');

-- ----------------------------
-- Table structure for history
-- ----------------------------
DROP TABLE IF EXISTS `history`;
CREATE TABLE `history`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `studyId` int(11) NULL DEFAULT NULL,
  `studyName` int(11) NULL DEFAULT NULL,
  `examId` int(11) NULL DEFAULT NULL,
  `examTitle` int(11) NULL DEFAULT NULL,
  `status` int(11) NULL DEFAULT NULL,
  `score` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `questionAanswer` varchar(511) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `questionBanswer` varchar(511) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `questionCanswer` varchar(511) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `questionDanswer` varchar(511) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `questionEanswer` varchar(511) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `questionAscore` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `questionBscore` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `questionCscore` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `questionDscore` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `questionEscore` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `ctime` datetime(0) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `studyId`(`studyId`) USING BTREE,
  UNIQUE INDEX `studyName`(`studyName`) USING BTREE,
  UNIQUE INDEX `examId`(`examId`) USING BTREE,
  UNIQUE INDEX `examTitle`(`examTitle`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for paper
-- ----------------------------
DROP TABLE IF EXISTS `paper`;
CREATE TABLE `paper`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(511) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `questionAlist` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `questionBlist` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `questionClist` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `questionDlist` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `questionElist` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `degree` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `questionAscore` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `questionBscore` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `questionCscore` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `questionDscore` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `questionEscore` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `ctime` datetime(0) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `title`(`title`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of paper
-- ----------------------------
INSERT INTO `paper` VALUES (1, '测试卷', '[2,3,4,5,6]', '[7,8,9,10,11]', '[12,13,14]', '[17,18]', '[24,25]', '简单', '5', '6', '5', '5', '10', '2018-03-05 15:16:06');

-- ----------------------------
-- Table structure for question
-- ----------------------------
DROP TABLE IF EXISTS `question`;
CREATE TABLE `question`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(511) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `qType` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `degree` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `options` varchar(511) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `answer` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `ctime` datetime(0) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `title`(`title`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 30 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of question
-- ----------------------------
INSERT INTO `question` VALUES (2, '单选题一', '单选题', '简单', '[{\"A\":\"选项一\"},{\"B\":\"选项一\"},{\"C\":\"选项一\"},{\"D\":\"选项一\"}]', 'A', '2018-03-05 14:59:22');
INSERT INTO `question` VALUES (3, '单选题二', '单选题', '简单', '[{\"A\":\"选项二\"},{\"B\":\"选项二\"},{\"C\":\"选项二\"},{\"D\":\"选项二\"}]', 'A', '2018-03-05 14:59:22');
INSERT INTO `question` VALUES (4, '单选题三', '单选题', '简单', '[{\"A\":\"选项三\"},{\"B\":\"选项三\"},{\"C\":\"选项三\"},{\"D\":\"选项三\"}]', 'A', '2018-03-05 14:59:22');
INSERT INTO `question` VALUES (5, '单选题四', '单选题', '简单', '[{\"A\":\"选项四\"},{\"B\":\"选项四\"},{\"C\":\"选项四\"},{\"D\":\"选项四\"}]', 'A', '2018-03-05 14:59:22');
INSERT INTO `question` VALUES (6, '单选题五', '单选题', '简单', '[{\"A\":\"选项五\"},{\"B\":\"选项五\"},{\"C\":\"选项五\"},{\"D\":\"选项五\"}]', 'A', '2018-03-05 14:59:22');
INSERT INTO `question` VALUES (7, '多选题一', '多选题', '简单', '[{\"A\":\"选项一\"},{\"B\":\"选项一\"},{\"C\":\"选项一\"},{\"D\":\"选项一\"}]', 'A', '2018-03-05 14:59:22');
INSERT INTO `question` VALUES (8, '多选题二', '多选题', '简单', '[{\"A\":\"选项二\"},{\"B\":\"选项二\"},{\"C\":\"选项二\"},{\"D\":\"选项二\"}]', 'A', '2018-03-05 14:59:22');
INSERT INTO `question` VALUES (9, '多选题三', '多选题', '简单', '[{\"A\":\"选项三\"},{\"B\":\"选项三\"},{\"C\":\"选项三\"},{\"D\":\"选项三\"}]', 'A', '2018-03-05 14:59:22');
INSERT INTO `question` VALUES (10, '多选题四', '多选题', '简单', '[{\"A\":\"选项四\"},{\"B\":\"选项四\"},{\"C\":\"选项四\"},{\"D\":\"选项四\"}]', 'A', '2018-03-05 14:59:22');
INSERT INTO `question` VALUES (11, '多选题五', '多选题', '简单', '[{\"A\":\"选项五\"},{\"B\":\"选项五\"},{\"C\":\"选项五\"},{\"D\":\"选项五\"}]', 'A', '2018-03-05 14:59:22');
INSERT INTO `question` VALUES (12, '填空题一', '填空题', '简单', '[]', 'A', '2018-03-05 14:59:22');
INSERT INTO `question` VALUES (13, '填空题二', '填空题', '简单', '[]', 'A', '2018-03-05 14:59:22');
INSERT INTO `question` VALUES (14, '填空题三', '填空题', '简单', '[]', 'A', '2018-03-05 14:59:22');
INSERT INTO `question` VALUES (15, '填空题四', '填空题', '简单', '[]', 'A', '2018-03-05 14:59:22');
INSERT INTO `question` VALUES (16, '填空题五', '填空题', '简单', '[]', 'A', '2018-03-05 14:59:22');
INSERT INTO `question` VALUES (17, '判断题一', '判断题', '简单', '[]', 'A', '2018-03-05 14:59:22');
INSERT INTO `question` VALUES (18, '判断题二', '判断题', '简单', '[]', 'A', '2018-03-05 14:59:22');
INSERT INTO `question` VALUES (19, '判断题三', '判断题', '简单', '[]', 'A', '2018-03-05 14:59:22');
INSERT INTO `question` VALUES (20, '判断题四', '判断题', '简单', '[]', 'A', '2018-03-05 14:59:22');
INSERT INTO `question` VALUES (21, '判断题五', '判断题', '简单', '[]', 'A', '2018-03-05 14:59:22');
INSERT INTO `question` VALUES (22, '简答题一', '简答题', '简单', '[]', 'A', '2018-03-05 14:59:22');
INSERT INTO `question` VALUES (23, '简答题二', '简答题', '简单', '[]', 'A', '2018-03-05 14:59:22');
INSERT INTO `question` VALUES (24, '简答题三', '简答题', '简单', '[]', 'A', '2018-03-05 14:59:22');
INSERT INTO `question` VALUES (25, '简答题四', '简答题', '简单', '[]', 'A', '2018-03-05 14:59:22');
INSERT INTO `question` VALUES (26, '简答题五', '简答题', '简单', '[]', 'A', '2018-03-05 14:59:22');

-- ----------------------------
-- Table structure for token
-- ----------------------------
DROP TABLE IF EXISTS `token`;
CREATE TABLE `token`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userId` int(11) NULL DEFAULT NULL,
  `accessToken` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `ctime` datetime(0) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `userId`(`userId`) USING BTREE,
  UNIQUE INDEX `accessToken`(`accessToken`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of token
-- ----------------------------
INSERT INTO `token` VALUES (1, 1, '64ad7c2d53fcacd7', '2018-03-05 16:19:31');

-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `studyId` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `studyName` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `password` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `loginName` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `ctime` datetime(0) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `studyId`(`studyId`) USING BTREE,
  UNIQUE INDEX `studyName`(`studyName`) USING BTREE,
  UNIQUE INDEX `password`(`password`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of users
-- ----------------------------
INSERT INTO `users` VALUES (1, '1', '123', '123456', 'test', NULL);

SET FOREIGN_KEY_CHECKS = 1;
