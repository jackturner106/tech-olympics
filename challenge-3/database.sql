-- given the following table definitions, write a query to find the percentage of users who returned to log in within 7 days of their first login
create table logins (
    user_id INT NOT NULL,
    login_date DATE NOT NULL,
    PRIMARY KEY (user_id, login_date)
);

SELECT
  (100.0 * COUNT(DISTINCT l1.user_id) / COUNT(DISTINCT l0.user_id)) AS percent_returned_within_7_days
FROM (
    SELECT user_id, MIN(login_date) AS first_login
    FROM logins
    GROUP BY user_id
) l0
LEFT JOIN logins l1
  ON l0.user_id = l1.user_id
  AND l1.login_date > l0.first_login
  AND l1.login_date <= DATE_ADD(l0.first_login, INTERVAL 7 DAY)
WHERE l1.login_date IS NOT NULL;
