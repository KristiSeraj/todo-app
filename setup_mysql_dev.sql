-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS todo_db;
CREATE USER IF NOT EXISTS 'todo_dev'@'localhost' IDENTIFIED BY 'todo_dev_pwd';
GRANT ALL PRIVILEGES ON `todo_db`.* TO 'todo_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'todo_dev'@'localhost';
FLUSH PRIVILEGES;
