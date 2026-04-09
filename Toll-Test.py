def get_toll_rate(highway_name, is_texpress=False):
    """
    Acts as a traffic cop, routing the request to the local database 
    or the live web scraper depending on the road type.
    """
    
    if not is_texpress:
        # 1. THE STATIC ROUTE (NTTA)
        # We will eventually pull this from your SQL database. 
        # For now, here are some hardcoded 2-axle rates for the Forester.
        ntta_rates = {
            "DNT": 1.90,    # Example rate for a segment of the Dallas North Tollway
            "PGBT": 2.45,   # Example rate for a segment of the Pres. George Bush Turnpike
            "SRT": 3.10     # Example rate for the Sam Rayburn Tollway
        }
        
        price = ntta_rates.get(highway_name)
        if price:
            return f"${price:.2f} (Pulled from local data)"
        else:
            return "Error: Static route not found."
            
    else:
        # 2. THE DYNAMIC ROUTE (TEXpress)
        # This is where our web scraper will eventually live.
        print(f"\n[System] Initializing web scraper for {highway_name}...")
        
        # Placeholder for the future BeautifulSoup/Requests logic
        scraped_live_price = 4.50 
        
        return f"${scraped_live_price:.2f} (Scraped live from TEXpress website)"


# --- Let's test the Traffic Cop! ---

print("Driver is heading to the Dallas North Tollway (Static)...")
dnt_price = get_toll_rate("DNT", is_texpress=False)
print(f"Result: {dnt_price}")

print("\nDriver is merging onto the LBJ TEXpress lanes (Dynamic)...")
lbj_price = get_toll_rate("LBJ", is_texpress=True)
print(f"Result: {lbj_price}")