class Http:
    StatusOk = 200
    StatusBadRequest = 400
    StatusUnauthorized = 401
    StatusForbidden = 403
    StatusNotFound = 404
    StatusInternalServerError = 500
    StatusNotImplemented = 501
    StatusBadGateway = 502
    StatusServiceUnavailable = 503
    StatusGatewayTimeout = 504
    StatusHTTPVersionNotSupported = 505
    StatusVariantAlsoNegotiates = 506
    StatusInsufficientStorage = 507
    StatusLoopDetected = 508
    StatusNotExtended = 510

class Message:
    Signup = "Signup successful"
    Signin = "Signin successful"
    CatchError = "Catch error"
    AlreadyExist = "User already exist"
    UserNotExist = "User not exist"
    Login = "Login successful"
    NotMatch = "Username or password not matching"
    CREATED = "Created successfully"
    NOT_ALLOWED = "Not allowed"
    NAME_TAKEN = "Name already taken"
    UPDATED = "Updated successfully"
    NOT_PRESENT = "Not present in the database"
    ALL_FETCHED = "All fetched"
    DELETED = "Deleted Successfully"