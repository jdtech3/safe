import numpy as np
import pandas as pd
import scipy.stats as stats

def trucated_normal(n, min, max, mu, sigma):
    distr = stats.truncnorm((min - mu) / sigma, (max - mu) / sigma, loc=mu, scale=sigma)

    return distr.rvs(n)

def gen_quiz_marks(n, mean=70):
    return trucated_normal(n, min=0, max=100, mu=mean, sigma=10)

def gen_time_taken(n):
    return trucated_normal(n, min=15, max=60, mu=40, sigma=10)

def example_number_of_incidents_vs_avg_mark_in_category():
    return pd.DataFrame({
        'year': [2023, 2024, 2025, 2026, 2027],
        'incidents': [17, 15, 6, 11, 3],
        'mark': [75, 75, 82, 79, 94],
    })

def example_courses():
    return [
        'CHE204',
        'CHE205',
        'CHE222',
    ]

def example_question_categories():
    return [
        'lab space',
        'policies',
        'responsibilities',
        'procedures',
        'ppe',
    ]
