#Karina
#Create a function that takes a number as a parameter and displays all the streets that have traffic congestion above or equal to that number
#After you create the function, create a list of street names where the volume is greater than 3,000 cars per hour
#In addition, find and print the street that is the busiest in chicago.


traffic_streets=["State St", "Michigan Ave", "Wacker Dr", "Lake Shore Dr", "Western Ave",
    "Halsted St", "Milwaukee Ave", "Fullerton Ave", "Grand Ave", "Belmont Ave",
    "Irving Park Rd", "North Ave", "Lawrence Ave", "Foster Ave", "Bryn Mawr Ave",
    "Peterson Ave", "Touhy Ave", "Devon Ave", "Addison St", "Montrose Ave",
    "Damen Ave", "Elston Ave", "Lincoln Ave", "Archer Ave", "Pulaski Rd",
    "Cicero Ave", "Kedzie Ave", "California Ave", "Homan Ave", "Central Park Ave",
    "Narragansett Ave", "Austin Blvd", "Ashland Ave", "Central Ave", "Laramie Ave",
    "Kostner Ave", "Crawford Ave", "Columbus Dr", "LaSalle St", "Dearborn St",
    "Clark St", "Broadway", "Sheridan Rd", "Ridge Ave", "Clybourn Ave",
    "Ogden Ave", "Roosevelt Rd", "Cermak Rd", "Pershing Rd", "Garfield Blvd"
]

traffic_volume=[ 2800, 5200, 2900, 2500, 4100,
    2100, 2400, 4800, 1800, 2300,
    2200, 4300, 1900, 1500, 1400,
    2600, 2100, 1700, 2400, 1800,
    2000, 1900, 3900, 2500, 2800,
    2900, 2200, 1600, 1200, 1100,
    1300, 1700, 4500, 2100, 1800,
    1400, 1300, 2900, 2700, 2400,
    2200, 2500, 2600, 2100, 1900,
    2300, 2800, 2400, 2100, 1500
]

filtered_list=[]

def traffic_congestion(volume):
    #STEP 1 CREATE THE LOOP
    for i in range(len(traffic_volume)):
        #Step 2 (THE conditional statement)
        if traffic_volume[i]>=volume:
            #STEP 3 (APPEND THE CORRECT ITEM)
            filtered_list.append(traffic_streets[i])
        #STEP 4 ANALYZE RESULTS and CLEAR the FILTERED LIST
    print(filtered_list)
    filtered_list.clear()

traffic_congestion(3000)
traffic_congestion(5000)
