import time
import pandas as pd
import numpy as np
import os

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = pd.Series(data=[1,2,3,4,5,6], index=['january', 'february', 'march', 'april', 'may', 'june'])
days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']



def get_filters():
    os.system('clear') # clear the screen before the program runs
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    while city.lower() not in CITY_DATA:
        print('So you want data...')
        time.sleep(1)
        print('Bike data.\n')
        time.sleep(1)
        print('For which city would you like bike share data?\nType the city as listed below:\n')
        for key in CITY_DATA:
            print((key.title()))
        city = input('\n')
        if city.lower() in CITY_DATA:
            break
        print('Invalid Input\n')

    os.system('clear') # clear the screen between each question

    print('-'*40)

    # get user input for month (all, january, february, ... , june)
    month = ''
    
    
        # use the index of the months list to get the corresponding int
    while month.lower() not in months and month.lower() != 'all':
        print('\n\nYou would like data for which month?\nChose from the list.\n')
        for item in months.index:
            print(item.title())
        print('or type \"all\" for all months')
        month = input('\n\n\n').lower()
        if month.lower() in months or month.lower() == 'all':
            break
        print('Invalid Input\n')
    month = months[month]

    os.system('clear') # clear the screen between each question

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = ''
    
    print('-'*40)
    
        # filter by day of week to create the new dataframe
    while day.lower() not in days and day.lower() != 'all':
        print('You would like data for which day of the week?\nBe sure to type an option from the list above\nOr type \'All\' for all days\n\n')
        for item in days:
            print(item.title())
        day = input('').lower()
        if day.lower() in days or day.lower() == 'all':
            break
        print('Invalid Input\n')
            

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(CITY_DATA[city])
    print(df)
    df['Start Time'] =  pd.to_datetime(df['Start Time'])    
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    df['Start_End_Combo'] = df['Start Station'] + ' To ' + df['End Station']
    # change df according to user inputs
    if month < 7:
        df = df[df['month'] == month]

    if day in days:
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    os.system('clear') # clear the screen before the data is returned
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    top_month = df['month'].value_counts().index[0]
    print('Month with the MOST bike rentals: \n{}\n\n'.format(months.index[top_month-1]))

    # display the most common day of week
    top_day = df['day_of_week'].value_counts().index[0]
    print('Day with the MOST bike rentals: \n{}\n\n'.format(top_day))
    
    # display the most common start hour
    top_hour = df['hour'].value_counts().index[0]
    print('hour with the MOST bike rentals: \n{}\n\n'.format(top_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('')
    print('-'*40)
    input('Press enter to see the next screen')
    print('-'*40)
    print('-'*40)
    print('-'*40)
    print('\n\n\n\n\n')


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    top_st_st = df['Start Station'].value_counts().index[0]
    print('Bikes are rented the most from: \n{}\n\n'.format(top_st_st))

    # display most commonly used end station
    top_en_st = df['End Station'].value_counts().index[0]
    print('Bikes are returned the most to: \n{}\n\n'.format(top_en_st))

    # display most frequent combination of start station and end station trip
    top_st_en_combo = df['Start_End_Combo'].value_counts().index[0]
    print('The most common route is : \n{}\n\n'.format(top_st_en_combo))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('')
    print('-'*40)
    input('Press enter to see the next screen')
    print('-'*40)
    print('-'*40)
    print('-'*40)
    print('\n\n\n\n\n')


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('Total travel time for the selected location is:   {}\n'.format(time.strftime("%H:%M:%S", time.gmtime(df['Trip Duration'].sum()))))

    # display mean travel time
    print('Average travel time in the selected location is:   {}'.format(time.strftime("%H:%M:%S", time.gmtime(df['Trip Duration'].mean()))))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('')
    print('-'*40)
    input('Press enter to see the next screen')
    print('-'*40)
    print('-'*40)
    print('-'*40)
    print('\n\n\n\n\n')


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('Bike Renter classification is as follows with a count for each: \n{}\n'.format(df['User Type'].value_counts()))

    # Display counts of gender
    while True:
        try:
            print('Bike Renter gender is as follows with a count for each: \n{}\n'.format(df['Gender'].value_counts()))
            break
        except KeyError:
            break
    # Display earliest, most recent, and most common year of birth
    while True:
        try:
            print('The oldest subscriber was born in: {}'.format(int(df['Birth Year'].min())))
            print('The youngest subscriber was born in {}'.format(int(df['Birth Year'].max())))
            print('The most common year of birth is: {}'.format(int(df['Birth Year'].value_counts().index[0])))
            break
        except KeyError:
            break

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print('-'*40)
    print('-'*40)
    print('\n\n\n\n\n')
    
    
    
    
    #print(df.loc[0])
    answer = input('\n\n\n\n\n\n\n\n\n\n\n\n\n\nWould you like to view the first 5 entries of raw data from this dataset?\n\n')
    counter = 0
    counter1 = 0
    while answer.lower() == 'yes' or answer.lower() == 'y':
        
        try:
            print(df.loc[counter])
            print()
            print('-'*40)
            print()
            print('-'*40)
            print()
            counter1+=1
            if counter1 % 5 == 0:
                answer = input('Would you like to view the next 5 entries of raw data?')
                if answer.lower() == 'no' or answer.lower() == 'n':
                    break
            counter+=1
        except KeyError:
            counter+=1
            pass
        


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
