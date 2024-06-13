-- Write a script that creates an index on the given table
-- and the first letter of name

CREATE INDEX idx_name_first ON names(LEFT(name, 1));
