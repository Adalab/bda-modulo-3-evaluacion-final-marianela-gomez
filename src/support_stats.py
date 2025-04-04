import pandas as pd
import numpy as np
import scipy.stats as stats
from scipy.stats import shapiro, poisson, chisquare, expon, kstest

def confidence_interval(var, distribution, confidence_level=0.95, error_nan_policy=None):
    '''
    Returns the confidence interval for a given variable at a specified confidence level.

    :param var: Data to be analyzed. Generally, a pandas DataFrame column or a Pandas Series.
    :param distribution: Type of distribution of the 'var' parameter. Options: 't' or 'norm'.
        See scipy.stats for details: https://docs.scipy.org/doc/scipy/reference/stats.html
    :param confidence_level: Confidence level per unit. Default is 0.95.
    :param error_nan_policy: Policy for handling NaN values. Options: 'propagate', 'omit', 'raise'. Default is None.
        See scipy.stats.sem for details: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.sem.html#sem
    '''

    avg = var.mean()

    if error_nan_policy is None:
        standard_error = stats.sem(var)
        print("Warning: If data contains NaN values, the confidence interval will be NaN.")

    elif error_nan_policy == "omit":
        standard_error = stats.sem(var, nan_policy="omit")
        print("Warning: If data contains NaN values, those values are excluded from the calculation.\n"
              "If the data is insufficient, the confidence interval will be NaN. Ensure you understand the implications.")

    elif error_nan_policy == "raise":
        try:
            standard_error = stats.sem(var, nan_policy="raise")
        except Exception as e:
            print(f"Error: {e}. The confidence interval could not be calculated. Please change the 'error_nan_policy' argument.")
            return None  # Return None to indicate failure

    else:
        print("Error: Invalid 'error_nan_policy' argument. Please use 'propagate', 'omit', or 'raise'.")
        return None  # Return None to indicate failure

    degrees_of_freedom = len(var) - 1

    if distribution == "t":
        critical_value = stats.t.ppf(1 - (1 - confidence_level) / 2, df=degrees_of_freedom)

    elif distribution == "norm":
        critical_value = stats.norm.ppf(1 - (1 - confidence_level) / 2)

    else:
        print("Error: Invalid distribution. Please enter 't' or 'norm'.\n"
              "For more details, see: https://docs.scipy.org/doc/scipy/reference/stats.html")
        return None  # Return None to indicate failure

    try:
        sup_lim = avg + critical_value * standard_error
        inf_lim = avg - critical_value * standard_error
        return (sup_lim, inf_lim)

    except Exception as e:
        print(f"Error: Confidence interval could not be computed. Error: {e}")
        return None # Return None to indicate failure

def hypothesis_test(*args):
    """
    Performs a hypothesis test to compare groups.
    1. First, it checks if the data is normally distributed using the Shapiro-Wilk or Kolmogorov-Smirnov test.
    2. If the data is normally distributed, it uses Bartlett's test to check for equal variances. If not, it uses Levene's test.
    3. If variances are equal, it uses Student's t-test; if not, it uses Welch's t-test.
    4. If the data is not normally distributed, it uses the Mann-Whitney U test (non-parametric alternative).

    Parameters:
    *args: lists or arrays containing the data for each group.

    Returns:
    dict with results of the normality, variance, and hypothesis tests.
    """

    # Check if there are at least two groups
    if len(args) < 2:
        raise ValueError("At least two data sets are needed to perform the test.")

    # Check normality in each group
    normality = []
    for group in args:
        if len(group) > 50:
            p_value_norm = stats.kstest(group, 'norm').pvalue  # Kolmogorov-Smirnov if n > 50
        else:
            p_value_norm = stats.shapiro(group).pvalue  # Shapiro-Wilk if n <= 50
        normality.append(p_value_norm > 0.05)

    data_normal = all(normality)  # True if all groups are normally distributed

    # Test for equality of variances
    if data_normal:
        p_value_variance = stats.bartlett(*args).pvalue  # Bartlett's test if data is normal
    else:
        p_value_variance = stats.levene(*args, center="median").pvalue  # Levene's test if not normal

    equal_variances = p_value_variance > 0.05

    # Apply the appropriate test
    if data_normal:
        if equal_variances:
            t_stat, p_value = stats.ttest_ind(*args, equal_var=True)
            test_used = "Student's t-test (equal variances)"
        else:
            t_stat, p_value = stats.ttest_ind(*args, equal_var=False)
            test_used = "Welch's t-test (unequal variances)"
    else:
        t_stat, p_value = stats.mannwhitneyu(*args)
        test_used = "Mann-Whitney U (non-parametric test)"

    # Significance level
    alpha = 0.05

    # Results
    result = {
        "Normality Test": normality,
        "Normal Data": data_normal,
        "Variance p-value": p_value_variance,
        "Equal Variances": equal_variances,
        "Test Used": test_used,
        "Statistic": t_stat,
        "p-value": p_value,
        "Conclusion": "Reject H0 (Significant differences)" if p_value < alpha else "Fail to reject H0 (No significant differences)"
    }

    # Print results more clearly
    print("\n **Hypothesis Test Results** ")
    print(f"✅ Normality Test: {'Yes' if data_normal else 'No'}")
    print(f"  - Normality per group: {normality}")
    print(f"✅ Variance Test: {'Equal' if equal_variances else 'Unequal'} (p = {p_value_variance:.4f})")
    print(f"✅ Applied Test: {test_used}")
    print(f" Statistic: {t_stat:.4f}, p-value: {p_value:.4f}")
    print(f" Conclusion: {result['Conclusion']}\n")

    return result