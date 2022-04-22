CREATE DATABASE Minecraft_Bingo;

USE Minecraft_Bingo;
CREATE TABLE chalenges ( chalenge_id int AUTO_INCREMENT primary key,
                         chalenge_name VARCHAR(20) NOT NULL, 
                         chalenge_png_location VARCHAR(40) NOT NULL,
                         chalenge_description VARCHAR(240)
                        );