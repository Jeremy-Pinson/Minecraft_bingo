/*
## Jérémy Pinson
## Bingo Race Minecraft
## 04/2022
*/

CREATE DATABASE minecraft_bingo;

USE minecraft_bingo;
CREATE TABLE chalenges ( chalenge_id int AUTO_INCREMENT primary key,
                         chalenge_name VARCHAR(20) NOT NULL, 
                         chalenge_png_location VARCHAR(40) NOT NULL,
                         chalenge_description VARCHAR(240)
                        );