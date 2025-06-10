import record
import datetime
import os, numpy as np, pandas as pd

SAMPLE_LENGTH = 10 #s
SAMPLE_RATE = 4*256 #fs (x*256)

def storeSampleData(data:np.ndarray):
    #get current date
    date = datetime.datetime.now()
    s_date = f"{date.strftime('%Y')}{date.strftime('%m')}{date.strftime('%d')}"
    s_time = f"{date.strftime('%H')}{date.strftime('%M')}{date.strftime('%S')}"

    #get data path
    script_dir = os.path.dirname(__file__) #absolute dir of script
    data_path = os.path.join(script_dir, f"data/{s_date}/")
    sample_path = os.path.join(data_path, f'sample_{s_date}{s_time}.npy')
    metadata_path = os.path.join(data_path, f'meta_{s_date}.csv')

    #check whether the specified path exists
    if not os.path.exists(data_path):
        #create new directory
        os.makedirs(data_path)
        print(f"created new dir {data_path}")

    #store sample
    np.save(sample_path, data)

    #create new metadata
    new_df = pd.DataFrame({
        # convert to storable format, [pd.to_datetime()]
        "timestamp": [date.isoformat()], 
        "sample id": [f'sample_{s_date}{s_time}.npy'],
        "sample length": [SAMPLE_LENGTH],
        "sample rate": [SAMPLE_RATE]
    })
    
    try:
        #read metedata file
        df = pd.read_csv(metadata_path)
        #add new data
        df = pd.concat([df, new_df], ignore_index=True)
    except FileNotFoundError as error:
        print(error)
        df = new_df

    #store metadata
    df.to_csv(metadata_path, index=False)
    print("data stored succesfully")

if __name__ == '__main__':

    data_sample = record.recordSample(SAMPLE_LENGTH, SAMPLE_RATE)
    storeSampleData(data_sample)