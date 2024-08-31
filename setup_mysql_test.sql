-- Creates database eviot_test_db
CREATE DATABASE IF NOT EXISTS eviot_test_db;
USE eviot_test_db;
CREATE USER IF NOT EXISTS 'eviot_test'@'localhost';
SET PASSWORD FOR 'eviot_test'@'localhost' = 'eviot_test_pwd';
GRANT ALL PRIVILEGES ON eviot_test_db.* TO 'eviot_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'eviot_test'@'localhost';
