import numpy as np
import scipy.stats as stats

# Example data for predicted (y_pred) and actual (y_real) values
y_pred = np.array([1, 2, 3, 4, 5])
y_real = np.array([1, 2, 3, 4, 5])


def f_test(y_pred, y_real):
    # Calculate Mean Squared Error (MSE)
    mse = np.mean((y_pred - y_real) ** 2)

    # Calculate R-squared (Coefficient of Determination)
    mean_y_real = np.mean(y_real)
    ss_total = np.sum((y_real - mean_y_real) ** 2)
    ss_residual = np.sum((y_real - y_pred) ** 2)
    r_squared = 1 - (ss_residual / ss_total)

    # Degrees of freedom
    n = len(y_real)
    p = 1  # number of predictors (intercept)
    df_regression = p
    df_residual = n - p - 1  # n - p - 1 for simple linear regression
    df_total = n - 1

    # Calculate F-statistic
    if ss_residual == 0:
        f_value = np.inf  # If ss_residual is zero, F-statistic is infinity
    else:
        f_value = (ss_total - ss_residual) / p / (ss_residual / df_residual)

    # Calculate p-value
    if np.isinf(f_value):
        p_value = 0.0  # If F-statistic is infinity, p-value is effectively zero
    else:
        p_value = stats.f.sf(f_value, p, df_residual)

    # Print the results
    print("Mean Squared Error (MSE):", mse)
    print("R-squared (R²):", r_squared)
    print("F-statistic:", f_value)
    print("p-value:", p_value)
    print("Degrees of freedom (Regression, Residual, Total):", df_regression, df_residual, df_total)
