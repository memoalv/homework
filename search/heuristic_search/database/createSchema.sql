CREATE DATABASE `london_tube`;

USE `london_tube`;

CREATE TABLE `stations`(
	`id` int UNSIGNED AUTO_INCREMENT NOT NULL,
	`latitude` decimal(6, 6),
	`longitude` decimal(6, 6),
	`name` varchar(35),
	`display_name` varchar(50),
	`zone` int,
	`total_lines` int,
	`rail` TINYINT,
	PRIMARY KEY(`id`)
);

CREATE TABLE `lines`(
	`id` int UNSIGNED AUTO_INCREMENT NOT NULL,
	`name` varchar(35),
	`colour` varchar(25),
	`stripe` varchar(25),
	PRIMARY KEY(`id`)
);

CREATE TABLE `lineDefinition`(
	`station1` int UNSIGNED NOT NULL,
	`station2` int UNSIGNED NOT NULL,
	`line` int UNSIGNED NOT NULL,
	FOREIGN KEY (`station1`) REFERENCES `stations`(`id`),
	FOREIGN KEY (`station2`) REFERENCES `stations`(`id`),
	FOREIGN KEY (line) REFERENCES `lines`(`id`)
);