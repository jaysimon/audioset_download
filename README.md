# Audioset download python code
- This code is for downloading all audioset in **mono, 16kHz, 16bit wav format**.
- Main download code is from dcase. I have change the code more suitable for download the whole audioset.
- I use this code download the whole audioset in **3 months**. It's a long time, so be patient, record the download num every day.
# How to use
1. Download/Make a list, [audioset_list_link](https://research.google.com/audioset/download.html)
2. Using convert_dcase_format.py to convert to dcase format, **change paths in the main function**
```
def main():
    fileOri = "../list/balanced_train_segments.csv"  # The list download from google
    fileTo = "../list/balanced_train_segments_converted.csv"  # The list converted to dcase format
    convert(fileOri, fileTo)  # Run converting
```
3. Change download_data.py list and save path, **change paths in the main function**3
```
if __name__ == "__main__":
    sCsvPath = "../list/balanced_train_segments_converted.csv"  
    # Download list path
    sToPath = "../data/balanced_train_segments"  
    # Save directory path
    iJobs = 3   
    # Download jobs parallel
```
4. run.sh

