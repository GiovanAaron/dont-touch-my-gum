

def calculate_alpha(y):
    # Known points
    y1, alpha1 = 350, 0
    y2, alpha2 = 230, 255
    
    # Calculate the slope (m)
    m = (alpha2 - alpha1) / (y2 - y1)
    
    # Calculate the y-intercept (b)
    b = alpha1 - m * y1
    
    # Calculate the alpha value based on y-coordinate
    alpha = m * y + b
    
    # Ensure the alpha is within the range [0, 255]
    alpha = max(0, min(255, alpha))
    
    return int(alpha)

