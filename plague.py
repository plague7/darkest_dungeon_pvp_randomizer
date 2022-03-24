#Imports

import numpy as np
import streamlit as st
import pandas as pd
import random

#Functions

def choose_n(n=4):
	
	vals = []

	while len(vals) < 4:
		num = np.random.randint(1,num_chars)

		if num not in vals:
			vals.append(num)

	return vals

def get_chars(vals):

	return [character_classes[i] for i in choose_n()]

def choice_randomizer():

	choices = ['Blind random team',
	'Random visible teams',
	'Build your own team']

	number = random.randint(0, 2)
	
	final_choice = choices[int(number)]
	
	st.write(str(final_choice))

#Character classes + num_chars

character_classes = ['Abomination',
'Antiquarian',
'Arbalest',
'Bounty Hunter',
'Crusader',
'Grave Robber',
'Hellion',
'Highwayman',
'Houndmaster',
'Jester',
'Leper',
'Man-at-Arms',
'Musketeer',
'Occultist',
'Plague Doctor',
'Vestal']

num_chars = len(character_classes)

#STREAMLIT FUNCTIONS#

#Header#
st.title('Darkest Dungeon PVP Randomizer')
st.header('Choose one specific use below !')

#Mode selector

choice = st.selectbox('Randomizer', ['One random team','My team and my opponent team', 'Choice randomizer'])

if choice == 'One random team':
		if st.button('Choose a random team for myself'):
			character_list = get_chars(choose_n())
			st.write(character_list)
elif choice == 'My team and my opponent team':
		if st.button('Choose a random team for me and my opponent'):
			st.write('Your team shall be')
			character_list = get_chars(choose_n())
			st.write(character_list)
			st.write('And your enemy team shall be')
			character_list_2 = get_chars(choose_n())
			st.write(character_list_2)
elif choice == 'Choice randomizer':
		if st.button('Our next fight will be...'):
			choice_randomizer()


