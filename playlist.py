"""
Oscar Dring
CS 021
Final
"""

def main():
play_list_1 = ['Drake', 'Maroon 5', 'Dua Lipa', 'Ariana Grande',
               'Lady Gaga', 'Taylor Swift', 'Lizzo', 'Bruno Mars']
play_list_2 = ['Taylor Swift', 'Ed Sheeran', 'Marshmello', 'Lady Gaga',
               'Travis Scott', 'Maroon 5', 'Justin Bieber', 'Blake Shelton']
play_list_3 = ['Maroon 5', 'Lady Gaga', 'Camila Cabello', 'Taylor Swift',
               'Post Malone', 'The Weeknd', 'Selena Gomez']
find_common(play_list_1,play_list_2,play_list_3)


def find_common(play_list_1,play_list_2,play_list_3):
    list_1(set(play_list_1).intersection(play_list_2)
           print(list_1)
