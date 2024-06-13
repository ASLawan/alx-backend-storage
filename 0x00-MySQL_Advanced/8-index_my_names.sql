-- Write a script that creates an index on the given table
-- and the first letter of name

ALTER TABLE names
ADD COLUMN first_letter CHAR(1) GENERATED ALWAYS AS (SUBSTRING(name, 1, 1)) STORED;

CREATE INDEX idx_name_first ON names (first_letter)
