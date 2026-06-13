SELECT ClaimID, PolicyID, ClaimAmount, ClaimStatus 
FROM Claims 
WHERE ClaimStatus = 'Approved' 
AND ClaimAmount > 0;

SELECT ClaimID, PolicyID 
FROM Claims 
WHERE ClaimStatus = 'Rejected' 
AND ClaimAmount <= 0;

SELECT COUNT(*) AS TotalClaims 
FROM Claims 
WHERE ClaimStatus = 'Pending';

SELECT p.PolicyID, p.PremiumAmount, c.ClaimAmount 
FROM Policies p 
JOIN Claims c ON p.PolicyID = c.PolicyID 
WHERE p.PolicyStatus = 'Active' 
AND c.ClaimStatus = 'Approved';

SELECT PolicyID, SUM(ClaimAmount) AS TotalPaidClaims 
FROM Claims 
WHERE ClaimStatus = 'Approved' 
GROUP BY PolicyID;

SELECT * 
FROM Policies 
WHERE PolicyEffectiveDate < '2023-01-01' 
AND PolicyEndDate > CURRENT_DATE;

SELECT c.ClaimID, c.ClaimAmount, p.PolicyID 
FROM Claims c 
LEFT JOIN Policies p ON c.PolicyID = p.PolicyID 
WHERE p.PolicyID IS NULL 
AND c.ClaimAmount < 0;

SELECT DISTINCT ClaimID 
FROM Claims 
WHERE ClaimAmount IS NULL;

SELECT COUNT(*) AS InvalidClaims 
FROM Claims 
WHERE ClaimID IS NULL 
OR ClaimAmount < 0;

SELECT p.PolicyID 
FROM Policies p 
WHERE NOT EXISTS (
    SELECT * 
    FROM Claims c 
    WHERE c.PolicyID = p.PolicyID 
    AND c.ClaimStatus = 'Approved'
);

SELECT *
FROM Claims 
WHERE ClaimCreatedOn < '2023-01-01' 
AND ClaimAmount > 0
ORDER BY ClaimCreatedOn DESC;

SELECT p.PolicyID, COUNT(c.ClaimID) AS ClaimsCount 
FROM Policies p 
LEFT JOIN Claims c ON p.PolicyID = c.PolicyID 
WHERE p.PolicyStatus = 'Active' 
GROUP BY p.PolicyID 
HAVING COUNT(c.ClaimID) = 0;

SELECT ClaimID 
FROM Claims 
WHERE ClaimStatus NOT IN ('Approved', 'Rejected', 'Pending');

UPDATE Claims 
SET ClaimStatus = 'Pending' 
WHERE ClaimID IN (
    SELECT ClaimID 
    FROM Claims 
    WHERE ClaimAmount > 10000 
    AND ClaimStatus IS NULL
);

DELETE FROM Claims 
WHERE ClaimID IN (
    SELECT ClaimID 
    FROM Claims 
    WHERE ClaimsDate < DATE_SUB(CURDATE(), INTERVAL 5 YEAR)
);

SELECT * 
FROM Claims 
WHERE ClaimCreatedOn BETWEEN '2023-01-01' AND '2023-12-31' 
AND ClaimStatus IS NOT NULL; 

SELECT p.PolicyID, AVG(c.ClaimAmount) AS AverageClaim 
FROM Policies p 
JOIN Claims c ON p.PolicyID = c.PolicyID 
WHERE c.ClaimStatus = 'Approved' 
GROUP BY p.PolicyID; 

SELECT Status, COUNT(*) AS Count 
FROM Claims 
GROUP BY Status 
HAVING COUNT(*) > 5; 

SELECT PolicyID 
FROM Policies 
WHERE MandatoryField IS NULL;

SELECT COUNT(*) 
FROM Claims 
WHERE ClaimID IS NULL; 

SELECT * 
FROM Claims 
WHERE NOT EXISTS (
    SELECT * 
    FROM Policies 
    WHERE Policies.PolicyID = Claims.PolicyID 
); 

INSERT INTO Claims (PolicyID, ClaimAmount, ClaimStatus) 
VALUES (1, 5000, 'Pending') 
WHERE NOT EXISTS (
    SELECT 1 
    FROM Claims 
    WHERE PolicyID = 1 
    AND ClaimStatus = 'Pending'
); 

CREATE TRIGGER BeforeClaimInsert 
BEFORE INSERT ON Claims 
FOR EACH ROW 
BEGIN 
    IF NEW.ClaimAmount < 0 THEN 
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Claim Amount cannot be negative'; 
    END IF; 
END; 

CREATE PROCEDURE GetApprovedClaims(OUT approvedCount INT) 
BEGIN 
    SELECT COUNT(*) INTO approvedCount 
    FROM Claims 
    WHERE ClaimStatus = 'Approved';
END; 

CREATE VIEW ActivePolicies AS 
SELECT PolicyID, PolicyStatus 
FROM Policies 
WHERE PolicyStatus = 'Active'; 

SELECT * 
FROM ActivePolicies 
WHERE PolicyID IN (
    SELECT DISTINCT PolicyID 
    FROM Claims 
    WHERE ClaimStatus = 'Approved'
); 

SELECT DocumentID 
FROM DocumentRecords 
WHERE DocumentType = 'Claim' 
AND DocumentDate < CURRENT_DATE 
AND NOT EXISTS (
    SELECT 1 
    FROM Claims 
    WHERE DocumentID = DocumentRecords.DocumentID
);