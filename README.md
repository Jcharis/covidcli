## Covidcli 
`covidcli` : A simple CLI for tracking and getting info about Coronavirus(covid19) Outbreak built with python.


![PyPI - Python Version](https://img.shields.io/pypi/pyversions/covidcli)

[![GitHub license](https://img.shields.io/github/license/Jcharis/covidcli)](https://github.com/Jcharis/covidcli/blob/master/LICENSE)


#### Dependencies
`covidcli` was designed with CLICK with the following dependencies
+ pandas
+ pyfiglet
+ tabulate


#### Installation
```bash
pip install covidcli
```

#### Screenshot
![](https://github.com/Jcharis/covidcli/blob/master/images/image01.png)


![](https://github.com/Jcharis/covidcli/blob/master/images/image02.png)

### Usage
#### Show Cases of Coronavirus
+ shows cases by the following cases ***confirmed|recovered|deaths|all***
```bash
covidcli show confirmed
```
```bash
Showing:: confirmed cases
===========================================
Number of Confirmed Cases:: 5532341.0
      Province/State         Country/Region      Lat      Long     Date  Confirmed
0                NaN               Thailand  15.0000  101.0000  1/22/20        2.0
1                NaN                  Japan  36.0000  138.0000  1/22/20        2.0
2                NaN              Singapore   1.2833  103.8333  1/22/20        0.0
3                NaN                  Nepal  28.1667   84.2500  1/22/20        0.0
4                NaN               Malaysia   2.5000  112.5000  1/22/20        0.0
...              ...                    ...      ...       ...      ...        ...
31057            NaN                 Jersey  49.1900   -2.1100  3/23/20        0.0
31058            NaN            Puerto Rico  18.2000  -66.5000  3/23/20        0.0
31059            NaN  Republic of the Congo  -1.4400   15.5560  3/23/20        0.0
31060            NaN            The Bahamas  24.2500  -76.0000  3/23/20        0.0
31061            NaN             The Gambia  13.4667  -16.6000  3/23/20        0.0

[31062 rows x 6 columns]

```


#### Get Latest Cases of Coronavirus
```bash
covidcli get latest
```
```bash
Showing Latest Cases
Accessed Time::2020-03-24 11:18:56.031077
=============================
{'Confirmed Cases': 5532341.0, 'Recovered Cases': 1980983.0, 'Death Cases': 196876.0}

```

#### Get Previous Cases of Coronavirus
```bash
covidcli get previous
```
```bash
Showing Previous Cases
Previous Time::2020-03-22 09:13:44.128850
=============================
{'Confirmed Cases': 4283692, 'Recovered Cases': 1606190, 'Death Cases': 143329}


```

#### Fetch and Download Current Dataset
+ Downloads a clean dataset of the covid19 outbreak in a csv format
```bash
covidcli get dataset
```


#### Get Status of Cases By Country
+ Get status of cases by countries either as all cases,confirmed,recovered or deaths.
```bash
covidcli get status "Italy"
```
```bash
Get Status of Cases
Country::Italy
Accessed Time::2020-03-24 11:08:49.648721
=============================
{'Confirmed Cases': 497959.0, 'Recovered Cases': 50954.0, 'Death Cases': 39435.0}
```

#### Search Info By Country
+ similar to the `get status` it searches for countries
```bash
covidcli search "Italy" --cases confirmed 
```
```bash
Searched::Italy
===================================
Accessed Time:: 2020-03-24 11:11:40.266145
Total Number of confirmed Cases for Italy::497959.0

```
or
```bash
covidcli search "China" 
```
```bash
Searched::China
===================================
Showing Latest Data
Accessed Time:: 2020-03-24 11:12:44.237260
       Province/State Country/Region      Lat      Long     Date  Confirmed  Recovered  Deaths
154             Hubei          China  30.9756  112.2707  1/22/20      444.0       28.0    17.0
158         Guangdong          China  23.3417  113.4244  1/22/20       26.0        0.0     0.0
159             Henan          China  33.8820  113.6140  1/22/20        5.0        0.0     0.0
160          Zhejiang          China  29.1832  120.0934  1/22/20       10.0        0.0     0.0
161             Hunan          China  27.6104  111.7088  1/22/20        4.0        0.0     0.0
...               ...            ...      ...       ...      ...        ...        ...     ...
30749  Inner Mongolia          China  44.0935  113.9448  3/23/20       75.0       74.0     1.0
30750         Ningxia          China  37.2692  106.1655  3/23/20       75.0       75.0     0.0
30754         Qinghai          China  35.7452   95.9956  3/23/20       18.0       18.0     0.0
30755           Macau          China  22.1667  113.5500  3/23/20       24.0       10.0     0.0
30763           Tibet          China  31.6927   88.0924  3/23/20        1.0        1.0     0.0

[2046 rows x 8 columns]

```

#### Get/Show Cases By Date
```bash
covidcli get date 2020-02-20
```
```bash
Showing 2020-02-20 Cases Worldwide 
Accessed Time::2020-03-25 13:41:46.182374
=============================
Analysing Data:  [####################################]  100%
Showing Case For 2020-02-20
             Confirmed  Recovered  Deaths
cases_dates                              
2020-02-20     76197.0    18177.0  2247.0

```

#### Compare Cases of Multiple Countries
```bash
covidcli compare China Italy Nigeria US
```
```bash
Comparison of ('China', 'US', 'Italy', 'Nigeria') Affected
Accessed Time::2020-03-25 13:45:34.795250
=============================
                Confirmed  Recovered    Deaths
Country/Region                                
China           3531169.0  1787212.0  119412.0
                Confirmed  Recovered  Deaths
Country/Region                              
US               159039.0      427.0  2276.0
                Confirmed  Recovered   Deaths
Country/Region                               
Italy            497959.0    50954.0  39435.0
                Confirmed  Recovered  Deaths
Country/Region                              
Nigeria             139.0        8.0     0.0

```

#### For US States
```bash
covidcli get usa Washington
```
```bash
State::Washington
Accessed Time::2020-04-10 00:50:08.332228
=============================
{'Confirmed Cases': 3688, 'Death Cases': 244}

```

#### Credits For Data
+ https://github.com/CSSEGISandData

#### Fixes and Update
** Added **
+ Comparison Between Countries
+ Get Cases By Date
+ Active Cases

** Fixes **
+ Data Discrepancy


#### By 
+ Jesse E.Agbe(JCharis)
+ Jesus Saves @JCharisTech



#### NB
+ Contributions Are Welcomed
+ Notice a bug, please let us know.
+ Thanks A lot