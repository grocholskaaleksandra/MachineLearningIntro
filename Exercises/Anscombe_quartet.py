#First review

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import numpy as np

def welcome() -> None:
    """
    Welcome message to Anscombe's quartet'

    Returns
    -------
    None
        
    """
    print("Hello user! This program is designed to perform Anscombe quartet calculations ")
    input("Please click any button to continue and to create the designated folder for the outputs: ")


def create_directory(folder_name: str) -> None:
    """
    Function designed to create new directory. 

    Parameters
    ----------
    folder_name : str
        Predefined folder name "output".

    Returns
    -------
    None

    """
    
    print('Creating new folder...')
    if not os.path.exists(folder_name):
        os.makedirs(folder_name) 
    print('Folder created!')

def download_dataset() -> pd.DataFrame:
    """
    Download of the Anscombe dataset from the seaborn library

    Returns
    -------
    anscombe_df : DataFrame

    """

    input("Click any button to download dataset: ")
    anscombe_df = sns.load_dataset("anscombe")
    print(anscombe_df)
    return anscombe_df

def add_first_plot_test(anscombe_df: pd.DataFrame) -> print:
    """
    Function designed to create the chart with the use of seaborn library. The output is saved to .jpg file.

    Parameters
    ----------
    anscombe_df : pd.DataFrame
        Data frame downloaded with the use of download_dataset() function.

    Returns
    -------
    print
        User guidance.

    """
    input("Click any button to generate the plot: ")
    sns.lmplot(x="x", y="y", col="dataset", hue="dataset", data=anscombe_df,
               col_wrap=2, palette="muted", height=5)
    plt.gcf().suptitle("Anscombe's Quartet", x=0.5, y=1)
    plt.savefig('output/image.jpg')
    plt.show()
    print ("Plot created! You can find them in the newly created folder.")
    
    
def basic_statistics(anscombe_df: pd.DataFrame) -> print:
    """
    Function designed to create the basic statistical calculations. The output is saved to .csv file.

    Parameters
    ----------
    anscombe_df : pd.DataFrame
        Data frame downloaded with the use of download_dataset() function.

    Returns
    -------
    print
        User guidance.

    """
    input("Click any button to generate the basic statistics: ")
    grouped = anscombe_df.groupby('dataset')
    summary_results = pd.DataFrame(columns=['mean_x', 'mean_y', 'std_x', 'std_y', 'correlation', 'var_x', 'var_y'])
    for key in grouped.groups.keys():
        summary_results.loc[key] = (
            grouped.mean().loc[key]['x'],
            np.round(grouped.mean().loc[key]['y'], 2),
            np.round(grouped.std().loc[key]['x'], 5),
            np.round(grouped.std().loc[key]['y'], 2),
            np.round(grouped.corr().loc[(key, 'x')]['y'], 3),
            np.round(grouped.var().loc[key]['x'], 5),
            np.round(grouped.var().loc[key]['y'], 2),

        )
    summary_results.to_csv('output/basic_statistics.csv')
    print(summary_results)
    print ("Basic statistics created! You can find them in the newly created folder.")
    input("Click any button to exit the program ")

    
def main():
    welcome()
    create_directory("output")
    anscombe_df = download_dataset()
    add_first_plot_test(anscombe_df)
    basic_statistics(anscombe_df)

if __name__ == "__main__":
    main()