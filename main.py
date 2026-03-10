import math
from fastapi import FastAPI, status, HTTPException


app = FastAPI()


@app.get("/", status_code=200)
def read_root():
    """Health check endpoint"""
    return {"status": "healthy"}


# A function to add two numbers.
@app.get("/add/{a}/{b}", status_code=200)
def add(a: str, b: str):
    """
    Add two numbers together.
    
    Parameters:
    - a: First number
    - b: Second number
    
    Returns:
    - JSON object with the result
    """
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Both 'a' and 'b' must be valid numbers.")
    return {"result": a + b}

# A function to subtract two numbers. 
@app.get("/subtract/{a}/{b}", status_code=200)
def sub(a: str, b: str):
    """
    Subtract two numbers.
    
    Parameters:
    - a: First number
    - b: Second number
    
    Returns:
    - JSON object with the result
    """
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Both 'a' and 'b' must be valid numbers.")
    return {"result": a - b}

# A function to multiply two numbers. 
@app.get("/multiply/{a}/{b}", status_code=200)
def mult(a: str, b: str):
    """
    Multiply two numbers.
    
    Parameters:
    - a: First number
    - b: Second number
    
    Returns:
    - JSON object with the result
    """
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Both 'a' and 'b' must be valid numbers.")
    return {"result": a * b}


# A function to divide two numbers.
@app.get("/divide/{a}/{b}", status_code=200)
def div(a: str, b: str):
    """
    Divide two numbers.
    
    Parameters:
    - a: First number
    - b: Second number
    
    Returns:
    - JSON object with the result
    """
    try:
        num_a = float(a)
        num_b = float(b)

        if num_b == 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail="Division for zero is not allowed. Please provide a non-zero value for 'b'."
            )
            
        return {"result": num_a / num_b}

    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, 
            detail="Both 'a' and 'b' must be valid numbers."
        )


# A function to find the square root of a number. 
@app.get("/sqrt/{a}")
def get_sqrt(a: str):
    try:
        num_a = float(a)
        if num_a < 0:
            raise HTTPException(status_code=400, detail="Cannot take square root of negative.")
        return {"result": math.sqrt(num_a)}
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, 
            detail="Input 'a' must be a valid number."
        )

# Percentage
@app.get("/percentage/{a}/{b}")
def get_percentage(a: str, b: str):
    try:
        num_a = float(a)
        num_b = float(b)
        if num_b == 0:
            raise HTTPException(status_code=400, detail="Total 'b' cannot be zero.")
        return {"result": (num_a / num_b) * 100}
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, 
            detail="Both 'a' and 'b' must be valid numbers."
        )

# Power
@app.get("/power/{a}/{b}")
def get_power(a: str, b: str):
    try:
        num_a = float(a)
        num_b = float(b)
        return {"result": math.pow(num_a, num_b)}
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, 
            detail="Both 'a' and 'b' must be valid numbers."
        )