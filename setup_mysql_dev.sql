-- Creates database eviot_dev_db
CREATE DATABASE IF NOT EXISTS eviot_dev_db;
USE eviot_dev_db;
CREATE USER IF NOT EXISTS 'eviot_dev'@'localhost';
SET PASSWORD FOR 'eviot_dev'@'localhost' = 'eviot_dev_pwd';
GRANT ALL PRIVILEGES ON eviot_dev_db.* TO 'eviot_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'eviot_dev'@'localhost';
