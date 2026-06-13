CREATE PROCEDURE ProcessInsuranceClaim 
    @ClaimID INT,
    @PolicyID INT,
    @ClaimAmount DECIMAL(10, 2),
    @Description NVARCHAR(255),
    @UserRole NVARCHAR(50),
    @ReturnMessage NVARCHAR(255) OUTPUT
AS
BEGIN
    -- Declare variables
    DECLARE @PolicyStatus NVARCHAR(50),
            @ErrorCode INT,
            @ErrorMessage NVARCHAR(255),
            @CurrentDate DATETIME = GETDATE();
    
    -- Validate mandatory fields
    IF @ClaimID IS NULL OR @PolicyID IS NULL OR @ClaimAmount <= 0 OR @Description IS NULL
    BEGIN
        SET @ReturnMessage = 'Mandatory fields cannot be NULL or invalid.';
        RETURN;
    END

    -- Validate user role
    IF @UserRole NOT IN ('Adjuster', 'Reviewer')
    BEGIN
        SET @ReturnMessage = 'User does not have permission to process claims.';
        RETURN;
    END

    BEGIN TRY
        -- Check Policy Status
        SELECT @PolicyStatus = Status FROM Policies WHERE PolicyID = @PolicyID;

        IF @PolicyStatus IS NULL
        BEGIN
            SET @ReturnMessage = 'Policy not found.';
            RETURN;
        END

        IF @PolicyStatus <> 'Active'
        BEGIN
            SET @ReturnMessage = 'Claims can only be processed for active policies.';
            RETURN;
        END

        -- Insert Claim Record
        INSERT INTO Claims (ClaimID, PolicyID, ClaimAmount, Description, CreatedDate, Status)
        VALUES (@ClaimID, @PolicyID, @ClaimAmount, @Description, @CurrentDate, 'Pending');

        SET @ReturnMessage = 'Claim processed successfully.';
    END TRY
    BEGIN CATCH
        SET @ErrorCode = ERROR_NUMBER();
        SET @ErrorMessage = ERROR_MESSAGE();
        INSERT INTO ErrorLogs (ErrorCode, ErrorMessage, ErrorDate)
        VALUES (@ErrorCode, @ErrorMessage, @CurrentDate);
        
        SET @ReturnMessage = 'An error occurred while processing the claim.';
    END CATCH
END