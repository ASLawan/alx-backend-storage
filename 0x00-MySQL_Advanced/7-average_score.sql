-- stored procedure to compute average scores for a student
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(
    IN p_user_id INT
)
BEGIN
    DECLARE avg_score DECIMAL(5,2);

    -- Compute the average score for the user
    SELECT AVG(score) INTO avg_score
    FROM corrections
    WHERE user_id = p_user_id;

    -- Check if the user already has an entry in the user_scores table
    IF EXISTS (SELECT 1 FROM users WHERE id = p_user_id) THEN
        -- Update the existing average score
        UPDATE users
        SET average_score = avg_score
        WHERE id = p_user_id;
    ELSE
        -- Insert a new record with the average score
        INSERT INTO users (id, average_score)
        VALUES (p_user_id, avg_score);
    END IF;
END //

DELIMITER ;
