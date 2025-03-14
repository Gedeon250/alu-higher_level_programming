-- Reset privileges for user_0d_1
REVOKE ALL PRIVILEGES ON *.* FROM 'user_0d_1'@'localhost';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Reset privileges for user_0d_2
REVOKE ALL PRIVILEGES ON *.* FROM 'user_0d_2'@'localhost';
GRANT SELECT, INSERT ON user_2_db.* TO 'user_0d_2'@'localhost';

-- Apply changes
FLUSH PRIVILEGES;
