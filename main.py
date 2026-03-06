from fastapi import FastAPI, status

app = FastAPI()


@app.get("/", status_code=200)
def read_root():
    """Health check endpoint"""
    return {"status": "healthy"}

# A function to add two numbers.
@app.get("/add/{a}/{b}", status_code=200)
def add(a: float, b: float):
    """
    Add two numbers together.
    
    Parameters:
    - a: First number
    - b: Second number
    
    Returns:
    - JSON object with the result
    """
    return {"result": a + b}

# A function to subtract two numbers. 
@app.get("/sub/{a}/{b}", status_code=200)
def sub(a: float, b: float):
    """
    Subtract two numbers.
    
    Parameters:
    - a: First number
    - b: Second number
    
    Returns:
    - JSON object with the result
    """
    return {"result": a - b}

