### Covidcli 
+ A simple CLI for tracking and getting info about Coronavirus Outbreak


#### Dependencies
+ click
+ pandas
+ pyfiglet
+ tabulate


#### Installation
```bash
pip install covidcli
```

### Usage
#### Show Cases of Coronavirus By confirmed|recovered|deaths|all
```bash
covidcli show confirmed
```


#### Get Latest Cases of Coronavirus
```bash
covidcli get latest
```


#### Get Previous Cases of Coronavirus
```bash
covidcli get previous
```

#### Fetch and Download Current Dataset
```bash
covidcli get dataset
```


#### Get Status of Cases By Country
```bash
covidcli get "Italy" --cases confirmed 
```

#### Search Info By Country
```bash
covidcli search "Italy" --cases confirmed 
```
or
```bash
covidcli search "China" 
```


#### Credits For Data
+ https://github.com/CSSEGISandData

#### By 
+ Jesse E.Agbe(JCharis)
+ Jesus Saves @JCharisTech



#### NB
+ Contributions Are Welcomed
+ Notice a bug, please let us know.
+ Thanks A lot