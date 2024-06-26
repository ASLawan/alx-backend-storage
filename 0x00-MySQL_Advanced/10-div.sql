-- script implementing a function that carries out division
-- of two numbers

DELIMITER //

CREATE FUNCTION SafeDiv(
	a INT,
	b INT
) RETURNS DECIMAL(10, 2)

DETERMINISTIC

BEGIN
	DECLARE result DECIMAL(10, 2);

	IF b = 0 THEN
		SET result = 0;
	ELSE
		SET result = a / b;
	END IF;

	RETURN result;
END //

DELIMITER ;
