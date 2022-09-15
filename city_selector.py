import fire
import questionary







def run():
    print("Welcome to the City Selector")

    app_running = True

    while app_running:
        choice = questionary.select(
            "What metropolitan city would you like to review?",
            choices=["Atlanta", "Austin", "Boston", "Chicago", "Dallas", "Denver", "Detroit", "Houston", "Las Vegas", "Los Angeles", "Miami", "Minneapolis", "New York", "Orange County", "Philadelphia", "Phoenix", "Portland", "Raleigh", "Sacramento", "San Diego", "Seattle", "SF Bay Area", "Washinton DC", "Quit"]
        ).ask()

        if choice == "Atlanta":
            cli_prefix = "atlanta"
            print(f"... Running search on {cli_prefix}.craigslist.org ...")           
        elif choice == "Austin":
            cli_prefix = "austin"
            print(f"... Running search on {cli_prefix}.craigslist.org ...")
        elif choice == "Boston":
            cli_prefix = "boston"
            print(f"... Running search on {cli_prefix}.craigslist.org ...")            
        elif choice == "Chicago":
            cli_prefix = "chicago"
            print(f"... Running search on {cli_prefix}.craigslist.org ...")
        elif choice == "Dallas":
            cli_prefix = "dallas"
            print(f"... Running search on {cli_prefix}.craigslist.org ...")
        elif choice == "Denver":
            cli_prefix = "denver"
            print(f"... Running search on {cli_prefix}.craigslist.org ...")
        elif choice == "Detroit":
            cli_prefix = "detroit"
            print(f"... Running search on {cli_prefix}.craigslist.org ...")
        elif choice == "houston":
            cli_prefix = "houston"
            print(f"... Running search on {cli_prefix}.craigslist.org ...")
        elif choice == "Las Vegas":
            cli_prefix = "lasvegas"
            print(f"... Running search on {cli_prefix}.craigslist.org ...")
        elif choice == "Los Angeles":
            cli_prefix = "losangeles"
            print(f"... Running search on {cli_prefix}.craigslist.org ...")
        elif choice == "Miami":
            cli_prefix = "miami"
            print(f"... Running search on {cli_prefix}.craigslist.org ...")
        elif choice == "minneapolis":
            cli_prefix = "minneapolis"
            print(f"... Running search on {cli_prefix}.craigslist.org ...")
        elif choice == "New York":
            cli_prefix = "newyork"
            print(f"... Running search on {cli_prefix}.craigslist.org ...")
        elif choice == "Orange County":
            cli_prefix = "orangecounty"
            print(f"... Running search on {cli_prefix}.craigslist.org ...")
        elif choice == "Philadelphia":
            cli_prefix = "philadelphia"
            print(f"... Running search on {cli_prefix}.craigslist.org ...")
        elif choice == "Phoenix":
            cli_prefix = "phoenix"
            print(f"... Running search on {cli_prefix}.craigslist.org ...")
        elif choice == "Portland":
            cli_prefix = "portland"
            print(f"... Running search on {cli_prefix}.craigslist.org ...")
        elif choice == "Raleigh":
            cli_prefix = "raleigh"
            print(f"... Running search on {cli_prefix}.craigslist.org ...")
        elif choice == "Sacramento":
            cli_prefix = "sacramento"
            print(f"... Running search on {cli_prefix}.craigslist.org ...")
        elif choice == "San Diego":
            cli_prefix = "sandiego"
            print(f"... Running search on {cli_prefix}.craigslist.org ...")
        elif choice == "Seattle":
            cli_prefix = "seattle"
            print(f"... Running search on {cli_prefix}.craigslist.org ...")
        elif choice == "SF Bay Area":
            cli_prefix = "sfbay"
            print(f"... Running search on {cli_prefix}.craigslist.org ...")
        elif choice == "Washington DC":
            cli_prefix = "washdc"
            print(f"... Running search on {cli_prefix}.craigslist.org ...")


        elif choice == "Quit":
            app_running = False
            print("Thank you for using the Post Pandemic Housing Relocator Tool! Goodbye!")


if __name__ == "__main__":
    fire.Fire(run)