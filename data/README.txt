Example data
============

gb_cycling_accidents.csv
------------------------

This is a Dataset of Bicycle accidents in Great Britain from 1970 to 2018. 

Each row holds information about a specific accident, and each column holds a particular piece of information about the accidents. 

Data Dictionary:

  1. Accident_Index - Unique identifier for the accident. This may be thought of as the accident "case number".
  2. Number_of_Vehicles - Number of vehicles that were involved in the accident
  3. Number_of_Casualties - Number of casualties resulting from the accident
  4. Date - Date when the accident happened
  5. Time - Time when the accident happened
  6. Speed_limit - Speed limit on the part of the road where the accident took place
  7. Road_conditions - Road condition (e.g., "frost") at the time and place of the accident
  8. Weather_conditions - Whether condition (e.g., "rain") at time and place of the accident
  9. Day - Day of the week when the accident occurred
  10. Road_type	- Type of road (e.g., "Dual carriageway") where the accident happened
  11. Light_conditions - Light conditions (e.g., "Daylight") at time of accident
  12. Gender - Whether the accident victim was Male or Female
  13. Severity - How severe (e.g., "Serious") the accident was 
  14. Age_Grp - Age group of the accident victim

The Dataset contains data such as the following accident index, number of vehicles involved, number of casualties, date and time of accident, speed limit, road and weather conditions, day of accident and finally the road type in which the accident took place. It also includes the gender of person driving the bicycle, severity of the accident and the age group range of the victims.

https://data.world/gonzandrobles/bicycleaccidentsuk

titanic.csv
-----------

The sinking of the Titanic is one of the most infamous shipwrecks in history.

On April 15, 1912, during her maiden voyage, the widely considered “unsinkable” RMS Titanic sank after colliding with an iceberg. Unfortunately, there weren’t enough lifeboats for everyone onboard, resulting in the death of 1502 out of 2224 passengers and crew.

While there was some element of luck involved in surviving, it seems some groups of people were more likely to survive than others.

Data Dictionary

Variable	Definition	Key
survival 	Survival 	0 = No, 1 = Yes
pclass 	Ticket class 	1 = 1st, 2 = 2nd, 3 = 3rd
sex 	Sex 	
Age 	Age in years 	
sibsp 	# of siblings / spouses aboard the Titanic 	
parch 	# of parents / children aboard the Titanic 	
ticket 	Ticket number 	
fare 	Passenger fare 	
cabin 	Cabin number 	
embarked 	Port of Embarkation 	C = Cherbourg, Q = Queenstown, S = Southampton

Variable Notes

pclass: A proxy for socio-economic status (SES)
1st = Upper
2nd = Middle
3rd = Lower

age: Age is fractional if less than 1. If the age is estimated, is it in the form of xx.5

sibsp: The dataset defines family relations in this way...
Sibling = brother, sister, stepbrother, stepsister
Spouse = husband, wife (mistresses and fiancés were ignored)

parch: The dataset defines family relations in this way...
Parent = mother, father
Child = daughter, son, stepdaughter, stepson
Some children travelled only with a nanny, therefore parch=0 for them.

https://www.kaggle.com/competitions/titanic/data

world_population.csv
--------------------

About Dataset
Context

The current US Census Bureau world population estimate in June 2019 shows that the current global population is 7,577,130,400 people on earth, which far exceeds the world population of 7.2 billion in 2015. Our own estimate based on UN data shows the world's population surpassing 7.7 billion.

China is the most populous country in the world with a population exceeding 1.4 billion. It is one of just two countries with a population of more than 1 billion, with India being the second. As of 2018, India has a population of over 1.355 billion people, and its population growth is expected to continue through at least 2050. By the year 2030, the country of India is expected to become the most populous country in the world. This is because India’s population will grow, while China is projected to see a loss in population.

The following 11 countries that are the most populous in the world each have populations exceeding 100 million. These include the United States, Indonesia, Brazil, Pakistan, Nigeria, Bangladesh, Russia, Mexico, Japan, Ethiopia, and the Philippines. Of these nations, all are expected to continue to grow except Russia and Japan, which will see their populations drop by 2030 before falling again significantly by 2050.

Many other nations have populations of at least one million, while there are also countries that have just thousands. The smallest population in the world can be found in Vatican City, where only 801 people reside.

In 2018, the world’s population growth rate was 1.12%. Every five years since the 1970s, the population growth rate has continued to fall. The world’s population is expected to continue to grow larger but at a much slower pace. By 2030, the population will exceed 8 billion. In 2040, this number will grow to more than 9 billion. In 2055, the number will rise to over 10 billion, and another billion people won’t be added until near the end of the century. The current annual population growth estimates from the United Nations are in the millions - estimating that over 80 million new lives are added each year.

This population growth will be significantly impacted by nine specific countries which are situated to contribute to the population growing more quickly than other nations. These nations include the Democratic Republic of the Congo, Ethiopia, India, Indonesia, Nigeria, Pakistan, Uganda, the United Republic of Tanzania, and the United States of America. Particularly of interest, India is on track to overtake China's position as the most populous country by 2030. Additionally, multiple nations within Africa are expected to double their populations before fertility rates begin to slow entirely.
Content

In this Dataset, we have Historical Population data for every Country/Territory in the world by different parameters like Area Size of the Country/Territory, Name of the Continent, Name of the Capital, Density, Population Growth Rate, Ranking based on Population, World Population Percentage, etc.
Dataset Glossary (Column-Wise)

    Rank: Rank by Population.
    CCA3: 3 Digit Country/Territories Code.
    Country: Name of the Country/Territories.
    Capital: Name of the Capital.
    Continent: Name of the Continent.
    2022 Population: Population of the Country/Territories in the year 2022.
    2020 Population: Population of the Country/Territories in the year 2020.
    2015 Population: Population of the Country/Territories in the year 2015.
    2010 Population: Population of the Country/Territories in the year 2010.
    2000 Population: Population of the Country/Territories in the year 2000.
    1990 Population: Population of the Country/Territories in the year 1990.
    1980 Population: Population of the Country/Territories in the year 1980.
    1970 Population: Population of the Country/Territories in the year 1970.
    Area (km²): Area size of the Country/Territories in square kilometer.
    Density (per km²): Population Density per square kilometer.
    Growth Rate: Population Growth Rate by Country/Territories.
    World Population Percentage: The population percentage by each Country/Territories.

Structure of the Dataset

Acknowledgement

This Dataset is created from https://worldpopulationreview.com/. If you want to learn more, you can visit the Website.

Cover Photo by: People symbol vector created by rawpixel.com - www.freepik.com
