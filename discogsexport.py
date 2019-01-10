import discogs_client
import time

outFile = "GONZOCIRCUS.html"

f = open(outFile, "w")

d = discogs_client.Client('mind-the-gap-exporter/0.1', user_token="")

# find the Gonzo label and it's releases
results = d.search('gonzo circus', type='label')
gonzolabel = results.page(1)[0]
gonzoreleases = gonzolabel.releases

# go over every release
for release in gonzoreleases:
    time.sleep(0.5)
    print(release.title.upper())
    print(release.year)
    f.write(release.title.upper())
    f.write(" (")
    f.write(str(release.year))
    f.write(")")
    f.write("<br>")
    print( )
    for track in release.tracklist:
        artistname = ""
        for artist in track.artists:
            if artistname != "": 
                artistname += ", "
            artistname += artist.name
        title = track.title
        if title != "Track 13":
            print(artistname, "-", title)
            f.write(artistname)
            f.write(" - ")
            f.write("<i>")
            f.write(title)
            f.write("</i>")
            f.write("<br>")
    f.write("<br>")
    print(release.notes)
    f.write("<b>")
    f.write("<i>")
    f.write(release.notes)
    f.write("</b>")
    f.write("</i>")
    f.write("<br>")
    print( )

