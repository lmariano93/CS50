CREATE TABLE `users` (
    `id` INT UNSIGNED AUTO_INCREMENT,
    `first_name` VARCHAR(50) NOT NULL,
    `last_name` VARCHAR(50) NOT NULL,
    `username` VARCHAR(50) NOT NULL UNIQUE,
    `password` VARCHAR(128) NOT NULL,
    PRIMARY KEY (`id`)
);

CREATE TABLE `schools` (
    `id` UNSIGNED AUTO_INCREMENT,
    `name` VARCHAR(100) NOT NULL,
    `type` ENUM ('Primary', 'Secondary', 'Higher Education') NOT NULL,
    `address` VARCHAR(255) NOT NULL,
    `foundation` YEAR NOT NULL ,
    PRIMARY KEY(`id`)
);

CREATE TABLE `companies` (
    `id` UNSIGNED AUTO_INCREMENT,
    `name` VARCHAR(100) NOT NULL,
    `type` ENUM ('Technology', 'Education', 'Business') NOT NULL,
    `address` VARCHAR(255) NOT NULL,
    PRIMARY KEY(`id`)
);

CREATE TABLE `connections_people` (
    `id` INT UNSIGNED AUTO_INCREMENT,
    `user1_id` INT NOT NULL,
    `user2_id` INT NOT NULL,
    `datetime` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY(`id`),
    FOREIGN KEY (`user1_id`) REFERENCES `users`(`id`),
    FOREIGN KEY (`user2_id`) REFERENCES `users`(`id`)
);

CREATE TABLE `connections_schools` (
    `id` INT UNSIGNED AUTO_INCREMENT,
    `user_id` INT NOT NULL,
    `school_id` INT NOT NULL,
    `start_date` DATE NOT NULL,
    `end_date` DATE,
    `type_degree` VARCHAR(50) NOT NULL,
    PRIMARY KEY(`id`),
    FOREIGN KEY (`user_id`) REFERENCES `users`(`id`),
    FOREIGN KEY (`school_id`) REFERENCES `schools`(`id`)
);

CREATE TABLE `connections_companies` (
    `id` INT UNSIGNED AUTO_INCREMENT,
    `user_id` INT NOT NULL,
    `companie_id` INT NOT NULL,
    `start_date` DATE NOT NULL,
    `end_date` DATE,
    `title` VARCHAR(100) NOT NULL,
    PRIMARY KEY(`id`),
    FOREIGN KEY (`user_id`) REFERENCES `users`(`id`),
    FOREIGN KEY (`companie_id`) REFERENCES `companies`(`id`)
);
