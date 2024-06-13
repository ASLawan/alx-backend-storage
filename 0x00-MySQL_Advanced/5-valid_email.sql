-- script that resets valid_email attribute upon change
-- of email attribute

DELIMITER //

CREATE TRIGGER reset_valid_email_on_email_change
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
	IF OLD.email <> NEW.email THEN
		SET NEW.email = 0;
	END IF;
END //

DELIMITER ;
