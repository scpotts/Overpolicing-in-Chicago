#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 14 15:53:45 2021

@author: stephaniepotts
"""

### Analysis Context

Chicago, IL has a reputation for investing heavily in policing technology, 
specifically in predictive policing technology (Rodrigo, 2021). In the 2000s 
and 2010s, Chicago invested its resources heavily in predictive policing, 
changing the way data was used by the Chicago Police Department (CPD) to 
understand, track, and reduce crime rates across the city.

While many have heralded the benefits of the data-driven policing strategies,
many people have also criticized relying so heavily on crime data to inform 
these strategies. It is widely known, especially in the case of Chicago, that
police are frequently assigned to patrol neighborhoods that contain higher
numbers of residents of color. This could be because these neighborhoods often
have higher numbers of low-income earners and less educated people, which can
go hand in hand with increased gang violence and higher rates of crime 
generally. This increased police presence in communities of color leads to 
seemingly more crime committed by people of color, because there are more police
present to witness and intervene in the activities. While this phenomenon has
numerous societal implications, the data-related implication is that it appears
on paper that people of color commit more crime, reinforcing the idea that more
police (and perhaps harsher policing tactics) should be deployed in these 
communities.

Much of predictive policing relies on this biased data, which will most likely 
lead to policing with biased outcomes if this technology is used to mitigate
these crimes before they occur (Dixon & Isaac, 2017). The goal of this analysis
is to produce maps of crimes that are likely to be evenly reported or evenly 
commited across Chicago, and comparing this to CPD tracked crime and arrest rates
to detect any potential biases or disparities. This analysis seeks to further 
the hypothesis that biased police data will likely lead to biased policing,
creating more tensions in already marginalized communities.

### Population Data

The first map discussed in **README.md**, **population.png**, displays the 
number of housing units per Census tract in Cook County, IL. The city of Chicago
takes up approximately the center half of the map. This map is helfpul to use 
as context for the population density of the areas highlighted in the race, 
crime, and arrest maps discussed throughout this analysis. Some helpful things 
to note are that the North East side of the city, along the border of Lake
Michigan is very heavily populated, while the city center is more sparsely 
populated. The South, South West, and West sides (the areas of particular note 
in this analysis) are moderately populated compared to other areas on the map.

The second map discussed, **race_pop.png**, shows the number of Black or African 
Americanhouseholders per Census tract in Chicago. This map is helpful to keep 
alongsidethe **population.png** map for context. This map shows how distinctly 
segregated Chicago is. There are higher concentrations of Black or African 
American householders on the South side, the West side, and the North side of 
the city. Something important to note is the North side of the city with high 
numbers of Black householders is a densely populated and relatively wealthy
area. For the purposes of this analysis, the South, South West, and West sides
are most important because that is where police have concentrated most of their
efforts.

### Crime & Arrest Data

The maps **arrest_map.png**, **battery_map.png**, and **narcotics_map.png** 
show the high concentrations of arrests and rates of battery and narcotics 
crimes in the South and West sides of the city, which is what previous evidence 
of bias policed data in Chicago predicted. This is especially interesting 
considering battery is equally likely to be reported by victims to the police, 
yet there are higher rates of it detected in CPD records. This is possibly 
because there are more officers on the ground in the highlighted neighborhoods
to find occurrences of battery as they take place, instead of victims having to
manually report them to CPD. 

Additionally, there is much evidence that narcotics are used at fairly equal 
rates across racial groups (Langan, 1995, p.3; US Department of Health and Human 
Services, 2013, p. 26), but the **narcotics_map.png** map would lead one to 
believe that most drug-related crimes occur in the South and West sides as well,
even though use is probably much more evenly spread across the city.

The data presented by the arrest, narcotics, and battery maps in this analysis 
show a high police presence in already marginalized communities. They also suggest
that crimes that occur or that are reported at fairly equal rates are much more
often detected by police in these areas. This presents a clear case of why any
policing strategy based on the data shown here would most likely lead to 
over-policing these already marginalized communities, possibly further raising 
tensions between the community and the police, leading to distorted rates of 
crime detections and arrest rates, and have other negative conseuqences not only
for the residents of these neighborhoods, but residents across the city.

### Sources

Dixon, A., & Isaac, W. (9 May 2017). "Why big data of police activity is
     inherently biased". The Conversation.com. Retrieved from,
     https://theconversation.com/why-big-data-analysis-of-police-activity-is-inherently-biased-72640

Langan, P. (1 October 1995). "The racial disparity in US drug arrests". US 
     Department of Justice. Retrieved from,
     https://www.bjs.gov/content/pub/pdf/rdusda.pdf

Rodrigo, C. (21 April 2021). "Police technology under scrutiny following 
     Chicago shooting." The Hill.com. Retrieved from, 
     https://thehill.com/homenews/state-watch/549612-police-technology-under-scrutiny-following-chicago-shooting

US Department of Health and Human Services. (2013). "Results from the 2013 
     national survey on drug use and health". US Department of Health and Human 
     Services. Retrieved from, 
     https://www.samhsa.gov/data/sites/default/files/NSDUHresultsPDFWHTML2013/Web/NSDUHresults2013.pdf
