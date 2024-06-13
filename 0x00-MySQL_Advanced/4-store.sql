-- create a trigger to reduce quantity after adding new order

DELIMITER //

CREATE TRIGGER decrease_qty_after_order
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
	UPDATE items
	SET quantity = quantity - NEW.number
	WHERE name = NEW.item_name;
END //

DELIMITER;
