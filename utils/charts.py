import math
import numpy as np
import pandas as pd
import seaborn as sns
from io import BytesIO

from utils import gen_data

sns.set_theme(style='darkgrid')

def demo_courses_vs_marks():
    data = {}
    for cat in gen_data.example_courses():
        data[cat] = gen_data.gen_quiz_marks(60, 70 + np.random.randint(-10, 10))
    df = pd.DataFrame(data=data)

    plot = sns.catplot(data=df)
    plot.ax.axhline(y=75, color='r', linestyle='dashed')
    plot.set(ylim=(0, 100), yticks=np.arange(0, 101, 10))

    f = BytesIO()
    plot.savefig(f, format='png')

    return f

def demo_question_categories_vs_marks():
    data = {}
    for cat in gen_data.example_question_categories():
        data[cat] = gen_data.gen_quiz_marks(60, 70 + np.random.randint(-20, 20))
    df = pd.DataFrame(data=data)

    plot = sns.catplot(data=df, aspect=1.6)
    plot.set(ylim=(0, 100))

    f = BytesIO()
    plot.savefig(f, format='png')

    return f

def demo_time_taken_vs_marks():
    times = gen_data.gen_time_taken(60)
    marks = gen_data.gen_quiz_marks(60, 70 + np.random.randint(-10, 10))

    # https://stats.stackexchange.com/questions/111865/tool-for-generating-correlated-data-sets
    correlated_marks = 0.6 * times + math.sqrt(1 - 0.6**2) * marks

    data = {
        'time': times,
        'mark': correlated_marks,
    }
    df = pd.DataFrame(data=data)

    plot = sns.lmplot(data=df, x='time', y='mark', scatter_kws={'color': 'purple'}, aspect=1.6)
    plot.set(ylim=(50, 100))
    plot.fig.subplots_adjust(top=0.9)
    plot.fig.suptitle('Quiz completion time vs. quiz score', fontsize=16)
    plot.set_axis_labels(x_var='Time taken to complete quiz (min)', y_var='Mark obtained (%)')

    f = BytesIO()
    plot.savefig(f, format='png')

    return f

def demo_incidents_vs_marks():
    data = gen_data.example_number_of_incidents_vs_avg_mark_in_category()
    df = pd.DataFrame(data=data)

    sizes = [n * 20 for n in range(2, 2 + len(data))]
    plot = sns.relplot(data=df, x='incidents', y='mark', size='year', sizes=sizes, hue='year', aspect=1.6)
    sns.regplot(data=df, x='incidents', y='mark', scatter=False, ax=plot.ax);
    plot.set(ylim=(50, 100))
    plot.fig.subplots_adjust(top=0.9)
    plot.fig.suptitle('Number of incidents vs. category score in "PPE" category', fontsize=16)
    plot.set_axis_labels(x_var='Number of incidents', y_var='Mark obtained (%)')

    f = BytesIO()
    plot.savefig(f, format='png')

    return f

