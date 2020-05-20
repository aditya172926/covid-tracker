import numpy
import pandas as pd
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup

def graph():
    url = 'https://www.mohfw.gov.in/'
    # make a GET request to fetch the raw HTML content
    web_content = requests.get(url).content
    # parse the html content
    soup = BeautifulSoup(web_content, "html.parser")
    # remove any newlines and extra spaces from left and right
    extract_contents = lambda row: [x.text.replace('\n', '') for x in row]
    # find all table rows and data cells within
    stats = [] 
    all_rows = soup.find_all('tr')
    for row in all_rows:
        stat = extract_contents(row.find_all('td')) 
    # notice that the data that we require is now a list of length 5
        if len(stat) == 5:
            stats.append(stat)
    #now convert the data into a pandas dataframe for further processing
    new_cols = ["Sr.No", "States/UT","Confirmed Cases","Recovered","Deceased"]
    state_data = pd.DataFrame(data = stats, columns = new_cols)
    state_data = state_data.iloc[:33,]
    
    state_data['Confirmed Cases'] = state_data['Confirmed Cases'].map(int)
    state_data['Recovered'] = state_data['Recovered'].map(int)
    state_data['Deceased'] = state_data['Deceased'].map(int)
    #pie chart------------------------------------------------------------------------------------
    group_size = [sum(state_data['Confirmed Cases']),
                sum(state_data['Recovered']),
                sum(state_data['Deceased'])]
    group_labels = ['Confirmed Cases\n' + str(sum(state_data['Confirmed Cases'])),
                    'Recovered\n' + str(sum(state_data['Recovered'])),
                    'Deceased\n' + str(sum(state_data['Deceased']))]
    custom_colors = ['blue','green','red']
    plt.figure(figsize = (5,5))
    a = plt.pie(group_size, labels = group_labels, colors = custom_colors)
    #central_circle = plt.Circle((0,0), 0.5, color = 'white')
    #fig = plt.gcf()
    #fig.gca().add_artist(central_circle)
    #plt.rc('font', size = 12)
    #plt.title('Nationwide total Confirmed Cases, Recovered and Deceased Cases', fontsize = 20)
    plt.savefig('/Users/harshshetye/Desktop/graphs/pie.jpg')
    #plt.show()    
    #bar chart------------------------------------------------------------------------------
    plt.figure(figsize = (15,10))
    plt.barh(state_data['States/UT'], state_data['Confirmed Cases'].map(int), 
            align = 'center', 
            color = 'lightblue', 
            edgecolor = 'blue')

    plt.xlabel('No. of Confirmed Cases cases', fontsize = 18)
    plt.ylabel('States/UT', fontsize = 18)
    plt.gca().invert_yaxis()
    plt.xticks(fontsize = 14)
    plt.yticks(fontsize = 14)
    plt.title('Total Confirmed Cases Cases Statewise', fontsize = 18 )
    for index, value in enumerate(state_data['Confirmed Cases']):
        plt.text(value, index, str(value), fontsize = 12)
    plt.savefig('/Users/harshshetye/Desktop/graphs/bar.jpg')
    #plt.show()