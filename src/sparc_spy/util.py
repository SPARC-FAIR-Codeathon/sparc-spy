import pandas as pd
from hurry.filesize import size
from sparc_me import Dataset_Api
from tabulate import tabulate


def get_scafold_based_datasets(save_csv=False, html_table=True):
    """Prints a list of scaffold-based datasets available on Pensieve.

    Args:
        save_csv (bool): Save dataset information to a csv file.
        html_table (bool): Returns html table rather than dataframe

    Return:
        df (Pandas Dataframe): Dataframe containing information regarding the scaffold-based datasets.

    """
    all_datasets = Dataset_Api().get_all_datasets_latest_version_pensieve()
    scafold_datasets = []

    for i in all_datasets:
        if i["name"].lower().__contains__("scaffold") or i["description"].lower().__contains__("scaffold") \
                or i["tags"].__contains__("scaffold"):
            scafold_datasets.append({'Id': i["id"],
                                     'Source Dataset Id': i["sourceDatasetId"],
                                     'Name': i["name"].strip(),
                                     'Description': i['description'].strip(),
                                     'Tags': i["tags"],
                                     'Version': str(i["version"]).strip(),
                                     "Dataset Size": size(i["size"]),
                                     "DOI": i["doi"].strip()})

    df = pd.DataFrame.from_dict(scafold_datasets)

    if save_csv:
        df.to_csv("Dataset_Information.csv")

    if html_table:
        return tabulate(df, headers='keys', tablefmt='html')
    else:
        print(tabulate(df, headers='keys', tablefmt='grid'))
        return df
