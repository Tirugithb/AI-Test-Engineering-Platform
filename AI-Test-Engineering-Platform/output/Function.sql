CREATE FUNCTION ValidateUserLogin (
    p_username VARCHAR(50),
    p_password VARCHAR(50)
) RETURNS BOOLEAN
BEGIN
    DECLARE user_count INT;
    DECLARE account_locked BOOLEAN;

    -- Input Validation
    IF p_username IS NULL OR p_password IS NULL THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Username and password must not be null';
    END IF;

    -- Business Rule Validation
    SELECT COUNT(*), account_is_locked INTO user_count, account_locked 
    FROM users 
    WHERE username = p_username 
    GROUP BY username;

    IF user_count = 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Invalid username or password';
    END IF;

    IF account_locked THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Account is locked. Please contact support';
    END IF;

    -- Authentication Validation
    IF NOT EXISTS (SELECT 1 FROM users WHERE username = p_username AND password = SHA2(p_password, 256)) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Invalid username or password';
    END IF;

    -- Session Validation and Login Tracking
    UPDATE users 
    SET last_login = NOW(),
        failed_attempts = 0
    WHERE username = p_username;

    RETURN TRUE;
END;