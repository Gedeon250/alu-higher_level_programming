-- Adjust privileges for user_0d_1
-- Revoke extra privileges that are not needed
REVOKE AUDIT_ABORT_EXEMPT, AUTHENTICATION_POLICY_ADMIN, FIREWALL_EXEMPT, PASSWORDLESS_USER_ADMIN, SENSITIVE_VARIABLES_OBSERVER 
FROM 'user_0d_1'@'localhost';

-- Grant missing privileges if any
GRANT SYSTEM_USER, SYSTEM_VARIABLES_ADMIN, BACKUP_ADMIN TO 'user_0d_1'@'localhost';

-- Verify the changes
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- Adjust privileges for user_0d_2
-- Grant only SELECT and INSERT privileges for user_0d_2
REVOKE ALL PRIVILEGES, GRANT OPTION FROM 'user_0d_2'@'localhost';
GRANT SELECT, INSERT ON user_2_db.* TO 'user_0d_2'@'localhost';

-- Verify the changes
SHOW GRANTS FOR 'user_0d_2'@'localhost';
