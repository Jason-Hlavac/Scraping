from google_images_download import google_images_download
def downloadimages(query):
    arguments = {"keywords": query, 
                "format": "jpg", 
                "limit":4, 
                "print_urls":True, 
                "size": "medium", 
                "aspect_ratio": "panoramic"} 
    try: 
        response.download(arguments)
    except FileNotFoundError:
        arguments = {"keywords": query, 
                     "format": "jpg", 
                     "limit":4, 
                     "print_urls":True,  
                     "size": "medium"} 
        try:
            response.download(arguments)
        except:
            pass



def fill_query(list):
    list.append(input("What do you want in your search query: "))
    resp(list)
    
def resp(list):
    answer = input("Would you like to add something else y/n:  ")
    if (answer == "y"):
        fill_query(list)
    elif(answer == "n"):
        pass
    else:
        print("That is not a valid answer")
        resp(list)
        
response = google_images_download.googleimagesdownload()
search_query = []
fill_query(search_query)

for (query) in search_query:
    downloadimages(query)
    print()
        
response = google_images_download.googleimagesdownload()
