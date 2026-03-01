import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def generate_ev_data(num_rows=2000):
    np.random.seed(42)
    random.seed(42)
    
    # 1. Define base parameters
    cities = ['Ahmedabad', 'Bengaluru', 'Chennai', 'Delhi', 'Hyderabad', 'Kolkata', 'Mumbai', 'Pune']
    stations = [f'ST{str(i).zfill(3)}' for i in range(1, 21)]
    vehicle_types = ['Bike', 'Scooter', 'Auto', 'Car']
    payment_methods = ['Credit Card', 'Debit Card', 'UPI', 'RFID Card', 'App Wallet']
    
    data = []
    
    # Base date to start generating from (e.g., Jan 1st of current year)
    start_date = datetime(2026, 1, 1)
    
    for i in range(1, num_rows + 1):
        # Generate varied dates over a 6-month period
        days_offset = random.randint(0, 180)
        current_date = start_date + timedelta(days=days_offset)
        
        station = random.choice(stations)
        city = random.choice(cities)
        vehicle = np.random.choice(vehicle_types, p=[0.3, 0.4, 0.1, 0.2]) # Weighted distribution
        payment = random.choice(payment_methods)
        
        # 2. Logic for Duration & Time
        # Different vehicles have different typical charge durations
        if vehicle in ['Bike', 'Scooter']:
            duration_mins = int(np.random.normal(loc=45, scale=15)) # Mean 45 mins
        elif vehicle == 'Auto':
            duration_mins = int(np.random.normal(loc=90, scale=30)) # Mean 90 mins
        else: # Car
            duration_mins = int(np.random.normal(loc=180, scale=60)) # Mean 3 hours
            
        # Bound duration safely between 10 mins and 12 hours
        duration_mins = max(10, min(720, duration_mins))
        
        # Start Time (Bias towards daytime/evening Commute)
        hour = int(np.random.normal(14, 5)) 
        hour = max(0, min(23, hour))
        minute = random.randint(0, 59)
        start_time = f"{hour:02d}:{minute:02d}"
        
        # Calculate End Time
        start_datetime = datetime.combine(current_date, datetime.strptime(start_time, "%H:%M").time())
        end_datetime = start_datetime + timedelta(minutes=duration_mins)
        end_time = end_datetime.strftime("%H:%M")
        
        # 3. CORE LOGIC: Energy Consumption strongly tied to Duration & Vehicle Type
        # Charge rates per minute depending on the onboard charger capacity
        charge_rates = {
            'Bike': 0.05,     # 3kW charger
            'Scooter': 0.04,  # 2.5kW charger
            'Auto': 0.12,     # 7kW charger
            'Car': 0.83       # 50kW DC Fast Charger
        }
        
        base_energy = duration_mins * charge_rates[vehicle]
        # Add a tiny bit of random noise (efficiency loss, battery curve)
        noise = np.random.normal(0, base_energy * 0.05) 
        energy_kwh = round(max(0.5, base_energy + noise), 2)
        
        # 4. CORE LOGIC: Cost strictly tied to Energy + specific fees
        # Assume base rate of ~₹15 per kWh + a connection fee (if any)
        base_rate = np.random.uniform(14.5, 18.5) # Slight variations in pricing across cities
        cost_inr = round(energy_kwh * base_rate, 2)
        
        data.append([
            f'SESSION{str(i).zfill(5)}',
            station,
            city,
            current_date.strftime('%Y-%m-%d'),
            start_time,
            end_time,
            duration_mins,
            vehicle,
            energy_kwh,
            cost_inr,
            payment
        ])

    df = pd.DataFrame(data, columns=[
        'Session_ID', 'Station_ID', 'City', 'Date', 
        'Charging_Start_Time', 'Charging_End_Time', 'Duration_mins',
        'Vehicle_Type', 'Energy_Consumed_kWh', 
        'Cost_INR', 'Payment_Method'
    ])
    
    return df

if __name__ == "__main__":
    print("Synthesizing 2000 rows of highly-correlated EV charging data...")
    df = generate_ev_data(2000)
    
    # Save over the old dataset
    filepath = "/Users/agnik/Desktop/genai/EV_Charging_Station_Usage.csv"
    df.to_csv(filepath, index=False)
    print(f"✅ Successfully saved logical synthetic data to {filepath}")
    
    # Calculate some quick stats to verify the math
    correlations = df[['Duration_mins', 'Energy_Consumed_kWh', 'Cost_INR']].corr() if 'Duration_mins' in df.columns else df[['Energy_Consumed_kWh', 'Cost_INR']].corr()
    print("\nVerifying Mathematical Corellations (Should be close to 1.0):")
    print(df[['Energy_Consumed_kWh', 'Cost_INR']].corr())