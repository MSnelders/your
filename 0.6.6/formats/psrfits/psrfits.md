<span style="float:right;">[[source]](https://github.com/thepetabyteproject/your/blob/master/your/formats/psrfits.py#L66)</span>

### PsrfitsFile


```python
your.formats.psrfits.PsrfitsFile(psrfitslist)
```


Simple functions for reading psrfits files from python. Not all possible features are implemented.

Original Source from Scott Ransom's
[psrfits](https://github.com/scottransom/presto/blob/master/python/presto/psrfits.py ).

Args: 

    psrfitslist (str): list of files

Attributes: 

    filename (str): Name of the first file
    filelist (list): List of files
    fileid (int): Index of the current file
    fits (obj): fits object of the current file read
    specinfo (obj): Object of class SpectraInfo for the given file list
    header (list): Header of the fits file
    source_name (str): Source Name
    machine_id (int): Machine ID
    barycentric (int): If 1 the data is barycentered
    pulsarcentric (int): Is the data in pulsar's frame of reference?
    src_raj (float): RA of the source (HHMMSS.SS)
    src_deg (float): Dec of the source (DDMMSS.SS)
    az_start (float): Telescope Azimuth (degrees)
    za_start (float): Telescope Zenith Angle (degrees)
    fch1 (float): Frequency of first channel (MHz))
    foff (float): Channel bandwidth (MHz)
    nchans (int): Number of channels
    nbeams (int): Number of beams in the rcvr.
    ibeam (int): Beam number
    nbits (int): Number of bits the data are recorded in.
    tstart (float): Start MJD of the data
    tsamp (float): Sampling interval (seconds)
    nifs (int): Number of IFs in the data.


----

<span style="float:right;">[[source]](https://github.com/thepetabyteproject/your/blob/master/your/formats/psrfits.py#L191)</span>

### read_subint


```python
PsrfitsFile.read_subint(isub, apply_weights=True, apply_scales=True, apply_offsets=True, pol=0, npoln=1)
```


Read a PSRFITS subint from a open pyfits file object.
Applys scales, weights, and offsets to the data.

Args: 

    isub (int): index of subint (first subint is 0)
    apply_weights (bool): If True, apply weights. (Default: apply weights)
    apply_scales (bool): If True, apply scales. (Default: apply scales)
    apply_offsets (bool): If True, apply offsets. (Default: apply offsets)
    pol (int): which polarization to chose
    npoln (int): number of polarizations to return

Returns: 

    np.ndarray: Subint data with scales, weights, and offsets applied in float32 dtype with shape (nsamps,nchan).


----

<span style="float:right;">[[source]](https://github.com/thepetabyteproject/your/blob/master/your/formats/psrfits.py#L343)</span>

### get_data


```python
PsrfitsFile.get_data(nstart, nsamp, pol=0, npoln=1)
```


Return 2D array of data from PSRFITS files.

Args: 

    nstart (int): Starting sample
    nsamp (int): number of samples to read
    pol (int): which polarization to return
    npoln (int): number of polarizations to return

Returns: 

    np.ndarray: Time-Frequency numpy array


----

<span style="float:right;">[[source]](https://github.com/thepetabyteproject/your/blob/master/your/formats/psrfits.py#L458)</span>

### SpectraInfo


```python
your.formats.psrfits.SpectraInfo(filenames)
```


Class to read the header of fits files

Args: 

    filenames (list): list of fits files


----

<span style="float:right;">[[source]](https://github.com/thepetabyteproject/your/blob/master/your/formats/psrfits.py#L32)</span>

### unpack_2bit


```python
your.formats.psrfits.unpack_2bit(data)
```


Unpack 2-bit data that has been read in as bytes.

Args: 

    data (np.ndarray): array of unsigned 2-bit ints packed into an array of bytes.

Returns: 

    np.ndarray: unpacked array. The size of this array will be four times the size of the input data.


----

<span style="float:right;">[[source]](https://github.com/thepetabyteproject/your/blob/master/your/formats/psrfits.py#L50)</span>

### unpack_4bit


```python
your.formats.psrfits.unpack_4bit(data)
```


Unpack 4-bit data that has been read in as bytes.

Args: 

    data (np.ndarray): array of unsigned 4-bit ints packed into an array of bytes.

Returns: 

    np.ndarray: unpacked array. The size of this array will be twice the size of the input data.


----

