# FFTI - text rearrange program 
  This program was created to get a tab separated file in format:
  
  ```
  0151	1425.76	28320	0
  2361	1158.49	4100	1200
  2663	737.1	2903	429
  2792	897.75	1950	627
  ```
  
  and rearrange it to be ready to upload to a framework used at work in the format of:
  
  ```
  E0151
  A1425.76|2019|Acumulado Ahorro
  A28320.00|2019|Prestamo Fondo 1
  A0.00|2019|Acumulado Empresa 1
  E2361
  A1158.49|2019|Acumulado Ahorro
  A4100.00|2019|Prestamo Fondo 1
  A1200.00|2019|Acumulado Empresa 1
  ```
  This file is meant for internal use and its uploaded to a 3rd poarty software
  it's posted here just as showcase for manipulating strings using pandas
  
  A sample file is included in the folder "files" if you wanna test it
  a warning about the way of manipulating data into pandas dataframes is showed because im reindexing data
  im aware of this but i neglected to fix it since im not calculating anything after the rearranging but writing
  a file instead.
  
  you are welcome to fix this part of the project if want to keep it clean
  
## Authors
  Jaime Arturo Lopez Barajas A.K.A. DarkPsydeLord, Tacoder

## Dependencies
  * pandas
  * Tkniter

## Licence
    Image processing on python
    Copyright (C) 2019  Jaime Arturo Lopez Barajas

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
    
## About the author
  >_"The mythical tacoder is an ethereal being that likes to impersonate a gigantic floating taco..."_ -DarkPsydeLord
  
  _**-*Cough cough*-**_
  
  Jaime Lopez is just an average guy trying to learn the ways of python by his own and _might not_ be able
  to help you if you have any deep question about life or coding in general, BUT, will gladly hear you and share
  some awesome taco recipes.
  
  Enjoy my work.
  
  ![Banner](https://user-images.githubusercontent.com/23390253/56400747-1c4da380-621b-11e9-88df-1e01cf050e81.jpg)
  
  **-Contact-**
    tacoder@outlook.com
