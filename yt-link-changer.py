youtubeLink = input('Type in a link: ') #user types in a youtube link

if(youtubeLink[28:32] == '?si='): #if the link has a self-identifier meant to track users
    newLink = youtubeLink[:youtubeLink.rfind('?')] #gets rid of everything after the ?
    print(newLink) #prints link without si...
    if (newLink[8:17] == 'youtu.be/'): #if the link has the URL shortener
        print(newLink.replace('youtu.be/', 'www.youtube.com/watch?v=')) #turns youtu.be to youtube.com, prints it
elif(youtubeLink[8:17] == 'youtu.be/'): #if the link has the URL shortener
    print(youtubeLink.replace('youtu.be/', 'www.youtube.com/watch?v=')) #turns youtu.be to youtube.com, prints it
elif(youtubeLink[28:32] == '?pp='): #if the link has a cluttered indexing thing
    newLink = youtubeLink[:youtubeLink.rfind('?')]
    print(newLink) #prints link without pp...
    if (newLink[8:17] == 'youtu.be/'): #if the link has the URL shortener
        print(newLink.replace('youtu.be/', 'www.youtube.com/watch?v=')) #turns youtu.be to youtube.com, prints it
else:
    print(youtubeLink) #prints link unchanged if it lacks those characteristics
