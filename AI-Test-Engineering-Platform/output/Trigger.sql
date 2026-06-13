CREATE TRIGGER trg_AuditInsuranceClaims
AFTER INSERT OR UPDATE OR DELETE ON InsuranceClaims
FOR EACH ROW
BEGIN
    DECLARE v_action VARCHAR(10);
    DECLARE v_user VARCHAR(50);
    DECLARE v_timestamp DATETIME;

    SET v_timestamp = NOW();
    SET v_user = CURRENT_USER();

    IF (TG_OP = 'INSERT') THEN
        SET v_action = 'INSERT';
        INSERT INTO AuditLog (ClaimID, Action, User, Timestamp, OldValue, NewValue)
        VALUES (NEW.ClaimID, v_action, v_user, v_timestamp, NULL, NEW.ClaimDetails);
    ELSEIF (TG_OP = 'UPDATE') THEN
        SET v_action = 'UPDATE';
        INSERT INTO AuditLog (ClaimID, Action, User, Timestamp, OldValue, NewValue)
        VALUES (NEW.ClaimID, v_action, v_user, v_timestamp, OLD.ClaimDetails, NEW.ClaimDetails);
    ELSEIF (TG_OP = 'DELETE') THEN
        SET v_action = 'DELETE';
        INSERT INTO AuditLog (ClaimID, Action, User, Timestamp, OldValue, NewValue)
        VALUES (OLD.ClaimID, v_action, v_user, v_timestamp, OLD.ClaimDetails, NULL);
    END IF;

    IF v_user NOT IN (SELECT Username FROM Users WHERE Role IN ('ClaimsAdjuster', 'Admin')) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Unauthorized action attempted by user: ' || v_user;
    END IF;

    IF NEW.ClaimDetails IS NULL THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Claim details cannot be null.';
    END IF;
END;