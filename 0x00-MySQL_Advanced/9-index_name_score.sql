-- write script to create index from first letter and score

CREATE INDEX idx_name_first_score ON names(CONCAT(LEFT(name, 1), score));
