CREATE DATABASE IF NOT EXISTS `ajaxdb`;
USE `ajaxdb`;

CREATE TABLE `member` (
	`user_id` INT(10) NOT NULL AUTO_INCREMENT,
	`user_name` VARCHAR(20) NOT NULL COLLATE 'utf8mb4_0900_ai_ci',
	`user_password` VARCHAR(128) NOT NULL COLLATE 'utf8mb4_0900_ai_ci',
	`user_email` VARCHAR(100) NOT NULL COLLATE 'utf8mb4_0900_ai_ci',
	`user_age` INT(10) NOT NULL,
	`user_avator` VARCHAR(50) NOT NULL COLLATE 'utf8mb4_0900_ai_ci',
	`last_update` DATETIME(6) NOT NULL,
	PRIMARY KEY (`user_id`) USING BTREE,
	UNIQUE INDEX `user_email` (`user_email`) USING BTREE
)
COLLATE='utf8mb4_0900_ai_ci'
ENGINE=InnoDB
;