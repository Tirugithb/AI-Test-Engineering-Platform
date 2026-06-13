CREATE VIEW ActiveInsurancePolicies AS
SELECT 
    p.PolicyID AS PolicyID,
    p.PolicyNumber AS PolicyNumber,
    p.PolicyHolderName AS PolicyHolderName,
    p.StartDate AS PolicyStartDate,
    p.EndDate AS PolicyEndDate,
    p.PremiumAmount AS MonthlyPremium,
    p.PolicyType AS PolicyType,
    p.CoverageAmount AS CoverageAmount,
    p.Status AS PolicyStatus
FROM 
    InsurancePolicies p
WHERE 
    p.Status = 'Active'
    AND p.EndDate >= CURRENT_DATE
    AND p.StartDate <= CURRENT_DATE;