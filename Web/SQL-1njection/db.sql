CREATE USER 'player'@'localhost' IDENTIFIED BY 'PixieblimpNinjayacht';

CREATE USER 'admin_user'@'localhost' IDENTIFIED BY 'RougequeenWhalehorse';

CREATE DATABASE secure_login;

CREATE TABLE `secure_login`.`members` (
    `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `first_name` VARCHAR(30) NOT NULL,
    `last_name` VARCHAR(30) NOT NULL,
    `team_id` int(11) NOT NULL,
    `email` VARCHAR(50) NOT NULL,
    `password` CHAR(128) NOT NULL,
    `salt` CHAR(128) NOT NULL
) ENGINE = InnoDB;

CREATE TABLE `secure_login`.`login_attempts` (
    `user_id` int(11) NOT NULL,
    `time` VARCHAR(30) NOT NULL,
    `unlock_time` VARCHAR(30) NOT NULL
) ENGINE = InnoDB;

CREATE TABLE `secure_login`.`cookies` (
    `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `cookie_verification` VARCHAR(128) NOT NULL,
    `user_id` INT NOT NULL,
    `email` VARCHAR(50) NOT NULL,
    `ip` VARCHAR(15) NOT NULL,
    `epoch` int(11) NOT NULL,
    `login_string` VARCHAR(128) NOT NULL
) ENGINE = InnoDB;

CREATE TABLE `secure_login`.`admins` (
    `user_id` int(11) NOT NULL
) ENGINE = InnoDB;

GRANT SELECT ON `secure_login`.`members` TO 'player'@'localhost';

INSERT INTO `secure_login`.`members` VALUES(1, 'test', 'user', 1, 'test_user@demo.com', '26C669CD0814AC40E5328752B21C4AA6450D16295E4EEC30356A06A911C23983AAEBE12D5DA38EEEBFC1B213BE650498DF8419194D5A26C7E0A50AF156853C79', '26C669CD0814AC40E5328752B21C4AA6450D16295E4EEC30356A06A911C23983AAEBE12D5DA38EEEBFC1B213BE650498DF8419194D5A26C7E0A50AF156853C79');

GRANT SELECT ON `hashtagctf`.`teams` TO 'player'@'localhost';

