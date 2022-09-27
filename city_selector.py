import fire
import questionary
import pandas as pd
import hvplot.pandas
import matplotlib.pyplot as plt
#import plotext as plt2
from pathlib import Path
import holoviews as hv
from zillow_api import zillow_api_request


### Autorun code ###
def run():
    print("Welcome to the City Selector")

    app_running = True

    ### Asks for input from User in CLI environment:
    choice = questionary.select(
        "Which metropolitan city were you considering moving to?",
        choices=["Atlanta, GA", "Austin, TX", "Boston, MA", "Chicago, IL", "Dallas, TX", "Denver, CO", "Detroit, MI", "Houston, TX", "Las Vegas, NV", "Los Angeles, CA", "Miami, FL", "Minneapolis, MN", "New York City, NY", "Philadelphia, PA", "Phoenix, AZ", "Portland, OR", "Raleigh, NC", "Sacramento, CA", "San Diego, CA", "Seattle, WA", "San Francisco, CA", "Washington, DC"]
    ).ask()
    
    ### Import data from Apartment_List using city selected by User
    city_data =  pd.read_csv(Path("./Resources/Apartment_List_Rent_Estimates_City_2022_8.csv"))
    city = choice
    city_df = city_data.loc[(city_data["City_Name"] == city) & (city_data["Bedroom_Size"] == "_Overall")]
    city_df = city_df.drop(columns=["City_Name", "FIPS_Code", "Population", "Bedroom_Size"])
    city_df_transposed = city_df.T
    city_df_transposed = city_df_transposed.astype(float)
    city_df_transposed.columns = ["Rent"]
    
    aug_2022_avg = city_df_transposed.values[-1].min()
    
    # Does request on zillow's API to grab rental listings for city selected above
    zillow_api_request(city)
    
    ###
    # Add in calculation to show percentage change from 1 year prior

    
    ###Create hvplot and save to .html for user interactivity
    hvplot.save(city_df_transposed.hvplot(
        title=f"Average Overall Rent for {city} from 2017 through August 2022",
        xlabel="Date",
        ylabel="Average Overall Rent",
        rot=90,
        height=500,
        ylim=(city_df_transposed.min().values[0]* 0.95,city_df_transposed.max().values[0] *1.05 )
    ),"./Results/city_plot.html")

    ###save plot as .jpg
    city_df_transposed.plot(  
        title=f"Average Overall Rent for {city} from 2017 through August 2022",
        xlabel="Date",
        ylabel="Average Overall Rent",
        rot=45,
        legend=False,
        ylim=(city_df_transposed.min().values[0]* 0.95,city_df_transposed.max().values[0] *1.05 ));
    plt.savefig("./Results/city_plot.jpg")

    
    

    
    #import data from API
    city_listings_df = pd.read_csv(
        Path(f'./Resources/{city}.csv')
    )
    
    #city_listings_data = listings_df[listings_df['CITY STATE COLUMN'] == city]
    #display(city_listings_data.head())
    
    #GeoViews plot   
    hv.save(city_listings_df.hvplot.points(
        'longitude',
        'latitude',
        geo=True,
        tiles='OSM',
        hover_cols=["address", "units"],
        frame_width=500,
        frame_height=500,
    ), './Results/geoviews.html')
    

    ### FIX PLOTEXT CODE
    # plt2.image_plot("./Results/city_plot.jpg")
    # plt2.title("test")
    # plt2.show()
            
    print(f"\nthe average rent for {city} in August 2022 was ${aug_2022_avg}\n")
    print(f"Please see the following charts in ./Results/ for a view of the average rent history for {city}\n city_plot.jpg\n city_plot.html\n geoviews.html\n")
    print(f"Thanks for using our Post Pandemic Housing Relocator Tool! Goodbye!")


if __name__ == "__main__":
    fire.Fire(run)