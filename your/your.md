<span style="float:right;">[[source]](https://github.com/thepetabyteproject/your/blob/master/your/your.py#L17)</span>

### Your


```python
your.Your(file)
```


Your class.

Args: 

    file: String or a list of files. It can either filterbank or psrfits files.

Examples: 

    your_object = your.Your("/path/to/filterbank.fil")
    your_object = your.Your(["puppi_58763_B1919+21_0292_0001.fits","puppi_58763_B1919+21_0292_0002.fits"]

Attributes: 

    your_header: instance of the Header class


----

<span style="float:right;">[[source]](https://github.com/thepetabyteproject/your/blob/master/your/your.py#L130)</span>

### bandpass


```python
Your.bandpass(nspectra=None)
```


Create the bandpass of the file

Args: 

    nspectra (int): Number of spectra to create bandpass from.

Returns: 

    numpy.ndarray: bandpass array


----

<span style="float:right;">[[source]](https://github.com/thepetabyteproject/your/blob/master/your/your.py#L158)</span>

### get_data


```python
Your.get_data(nstart, nsamp, time_decimation_factor=None, frequency_decimation_factor=None, pol=0)
```


Read data from files

Args: 

    nstart (int): start sample
    nsamp (int): number of samples to read
    time_decimation_factor (int): number of time samples to average
    frequency_decimation_factor (int): number of frequency channels to average
    pol (int): which polarization to chose

!!! note
    The decimation (both in time and frequency) is done on the data read i.e containing `nsamp` number of samples
    and `nchans` number of channels. Therefore, both decimation factors should exactly divide the
    nsamps or nchans respectively.

Returns: 

    numpy.ndarray: 2D numpy array of data


----

<span style="float:right;">[[source]](https://github.com/thepetabyteproject/your/blob/master/your/your.py#L267)</span>

### dispersion_delay


```python
Your.dispersion_delay(dms=5000)
```


Calculate the dispersion delay in seconds for the given configuration

Args: 

    dms: DM or a list of DM values

Returns: 

    Dispersion delay in seconds.


----

<span style="float:right;">[[source]](https://github.com/thepetabyteproject/your/blob/master/your/your.py#L285)</span>

### Header


```python
your.Header(your)
```


Your Header class, it contains all the relevant metadata.

Args: 

    your: Your object

Attributes: 

    filelist (list): List of files used to make the your object
    filename (str): Name of the first file used to make the object
    basename (str): Base name of file
    source_name (str): Source Name
    ra_deg (float): RA of the source in degrees
    dec_deg (float): Dec of the source in degrees
    bw (float): bandwidth of the data
    center_freq (float): Center frequency of the data.
    time_decimation_factor (int): Number of time samples to average
    frequency_decimation_factor (int): Number of frequency channels to average
    native_tsamp (float): Sampling time of the data pre-decimation (seconds)
    native_foff (float): Channel bandwidth of the data pre-decimation (MHz)
    native_nchans : Number of channels in the data pre-decimation
    native_nspectra: Number of spectra in the data pre-decimation
    dtype: dtype of the (read) data
    nbits (int): Number of bits in the data
    tstart (float): Start MJD of the data
    fch1 (float): Frequency of the first channel (MHz)
    npol (int): Number of polarisations in the data


----

