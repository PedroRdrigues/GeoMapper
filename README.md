# GeoMapping

Data processing and conversion in GeoJson or .xlsx

## Getting Started

Install the latest version of GeoMapping using pip.

```bash
    pip install GeoMapper
```
    
## Importing files into GeoMepping

```code
    from MapeAR import FormatSpreadSheet as fss

    area = fss('data/arborizacao_brasil.csv') # Also supports Excel files
```

## Use of treatments for afforestation

```code
    area.afforestation() 
```

## 💾 Saves to a specified file and names it 

```code
    area.save('Arborizacao_Brasil_tratado')
```

## Improvements

### Save as GeoJson

Currently it is not possible to save the new file in any format other than .xlsx. The first improvement will be to implement saving to GeoJson which is the real focus.


### Implement new treatment methods

As the initial focus was only on afforestation, it was implemented first, but in the future I intend to add other methods such as gases and pollutants, combustion, environmental risk zones, temperature, etc...