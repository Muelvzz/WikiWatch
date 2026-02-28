from services.wiki_calculate import analyzed_data

if __name__ == '__main__':
    user_input = analyzed_data("https://en.wikipedia.org/wiki/Magnus_Carlsen")

    print(user_input)

'''
1. main.py sends an input into the wiki_fetch
2. the wiki_fetch sends a request for an api
3. the wiki_fetch will return the api

4. the wiki_calculate will then start after the wiki_fetch
5. the wiki_calculate will then perform all the functions
6. the wiki_calculate will send it back to the main.py to display

'''