"""
Oscar Dring
CS 021
Final
"""
#in this function the results of find_common are displayed after the lists are processd and compaired
def main():
    play_list_1 = ['Drake', 'Maroon 5', 'Dua Lipa', 'Ariana Grande',
               'Lady Gaga', 'Taylor Swift', 'Lizzo', 'Bruno Mars']
    play_list_2 = ['Taylor Swift', 'Ed Sheeran', 'Marshmello', 'Lady Gaga',
               'Travis Scott', 'Maroon 5', 'Justin Bieber', 'Blake Shelton']
    play_list_3 = ['Maroon 5', 'Lady Gaga', 'Camila Cabello', 'Taylor Swift',
               'Post Malone', 'The Weeknd', 'Selena Gomez']
    common_list = find_common(play_list_1,play_list_2,play_list_3)

    print('The artists common in all three playlists are:')
    for num, artist in enumerate(common_list):
        
        print(num+1,'-', artist)
   
    

#in this function the three playlists are compaired to one another to find the common artists between the three after doing this the one common playlist arstist list is returned
def find_common(play_list_1,play_list_2,play_list_3):
    list_1 = list(set(play_list_1).intersection(play_list_2))
    common_list = list(set(list_1).intersection(play_list_3))
    
    
    return common_list

if __name__ == '__main__':
    main()
