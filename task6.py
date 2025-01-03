import pytest

# Simple function to calculate the perimeter of a rectangle
def perimeter(length, breadth):
    # Check if either length or breadth is missing
    if length is None or breadth is None:
        raise Exception("Undefined")  # Raise an error if any of the inputs are missing
    
    # Check if the inputs are numbers
    if not isinstance(length, (int, float)) or not isinstance(breadth, (int, float)):
        raise Exception("Not a number")  # Raise an error if inputs are not numbers
    
    # Check if the inputs are negative
    if length < 0 or breadth < 0:
        raise Exception("Dimension cannot be negative")  # Raise an error if dimensions are negative
    
    # If everything is okay, return the perimeter
    return 2 * (length + breadth)



# Test case where the perimeter is valid
def test_perimeter_valid():
    result = perimeter(4, 5)  # Valid inputs
    assert result == 18  # 2 * (4 + 5) = 18

# Test case where length is missing
def test_perimeter_missing_length():
    with pytest.raises(Exception) as exc:
        perimeter(None, 5)  # Missing length
    assert str(exc.value) == "Undefined"  # Check if the correct error message is shown

# Test case where breadth is missing
def test_perimeter_missing_breadth():
    with pytest.raises(Exception) as exc:
        perimeter(4, None)  # Missing breadth
    assert str(exc.value) == "Undefined"  # Check if the correct error message is shown

# Test case where length is not a number (e.g., a string)
def test_perimeter_invalid_length():
    with pytest.raises(Exception) as exc:
        perimeter('4', 5)  # Invalid length (string instead of a number)
    assert str(exc.value) == "Not a number"  # Check if the correct error message is shown

# Test case where breadth is not a number (e.g., a string)
def test_perimeter_invalid_breadth():
    with pytest.raises(Exception) as exc:
        perimeter(4, '5')  # Invalid breadth (string instead of a number)
    assert str(exc.value) == "Not a number"  # Check if the correct error message is shown

# Test case where length is negative
def test_perimeter_negative_length():
    with pytest.raises(Exception) as exc:
        perimeter(-4, 5)  # Negative length
    assert str(exc.value) == "Dimension cannot be negative"  # Check if the correct error message is shown

# Test case where breadth is negative
def test_perimeter_negative_breadth():
    with pytest.raises(Exception) as exc:
        perimeter(4, -5)  # Negative breadth
    assert str(exc.value) == "Dimension cannot be negative"  # Check if the correct error message is shown


#How to run the code:

#if not installed
#pip install pytest