"""
This module defines a FastAPI app with a single /calculate endpoint
that performs basic arithmetic operations.
"""
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from operations.add import add
from operations.subtract import subtract
from operations.multiply import multiply
from operations.divide import divide
from operations.modulus import modulus
from operations.exponent import exponent #exponent

app = FastAPI()

# API endpoint
@app.post("/calculate")
async def calculate_numbers(request: Request):
    """
    Perform a calculation based on the provided operation and numbers.
    Example JSON:
    {
        "operation": "add",
        "numb1": 5,
        "numb2": 3
    }
    Returns:
        The result of the operation.
    """
    data = await request.json()

    if not all(k in data for k in ("operation", "numb1", "numb2")):
        raise HTTPException(status_code=400, detail="Missing keys in request body")
    operation = data["operation"].lower()
    x = data["numb1"]
    y = data["numb2"]

    try:
        operation = operation.lower()

        if operation == "add":
            result = add(x, y)
        elif operation == "subtract":
            result = subtract(x, y)
        elif operation == "multiply":
            result = multiply(x, y)
        elif operation == "divide":
            result = divide(x, y)
        elif operation == "modulus":
            result = modulus(x, y)
        elif operation == "exponent":
            result = exponent(x, y)
        else:
            return JSONResponse(status_code=400, content={"error": "Invalid operation"})

        return {"message" : f"Using the operation ({operation}) we get: {result}"}

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve)) from ve
