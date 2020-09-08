# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import io
import json
import os
import re
import numpy as np
import pandas as pd

def remove_html_tags(text):
    #removing html from data
    unwanted_chars = ['/n','/t']
    for i in unwanted_chars:
        text.replace(i,'')
    return re.sub("<.*?>", "", text)

def replace_unessecary_characters(text):

    text = text.strip('\n')
    text = text.strip('\t')
    return text


if __name__ == '__main__':

    # Setting file location in string format and accessing os to obtain the directory of the file
    directory_in_str = "C:\\Users\Arzhang\\PycharmProjects\\jsonParser\\JSONFolder\\"
    directory = os.fsencode(directory_in_str)

    # Setting the headers for the CSV file and the name of the CSV file of interest
    header = "Thread, Title, PostID, Username, Date, Post Content \n"
    CSVFile = "hackThisUserData.csv"

    #Opening the CSV file of interest to write to
    with io.open(CSVFile, "w",encoding="utf-8") as f:
        f.write(header)

        #Obtaining the the .JSON files in directory and iterating through them to Parse
        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            filename = directory_in_str + filename

        #Opening the .JSON files for parsing the data and calling loads function to load
            with io.open(filename, "r", encoding="utf-8") as json_data:
                data = json.load(json_data)

                for i in data:

                    #Parsing .JSON file for elements of interest
                    thread = str(i.get('user_url_blog'))
                    title = str(i.get('post_title'))
                    post_ID = str(i.get('pid'))
                    username = str(i.get('username'))
                    date = str(i.get('post_date'))
                    postContent = str(i.get('post_content'))


                    if thread != "None"or title != "None":
                        date = remove_html_tags(postContent)
                        postContent = remove_html_tags(postContent)
                        f.write(thread.replace(',', '').replace('[', '').replace(']', '').replace("'", '') + "," +
                                title.replace(',','').replace('[', '').replace(']', '').replace("'", '') + "," +
                                post_ID.replace(',','').replace('[', '').replace(']', '').replace("'", '') + "," +
                                username.replace(',','').replace('[', '').replace(']', '').replace("'", '') + "," +
                                date.replace(',','').replace('[', '').replace(']', '').replace("'", '') + "," +
                                postContent.replace(',','').replace('[', '').replace(']', '').replace("'", '') + "\n" )


    df = pd.read_csv(CSVFile)













