lines = [line.strip() for line in open('_torey.csv').readlines()]
lines.pop(0)

# keep these until I get to the top of the list
lines.pop(0)
lines.pop(0)

div_template = (
    "<div>"
    "<video controls>"
    "<source src='/assets/videos/torey/{}' type='video/mp4' />"
    "</video>"
    "<p><a href='{}'>{}<a></p>"
    "</div>")

result = ""
for line in lines:
    video, day, url, title, comment = line.split(";")
    print video
    result += div_template.format(video, url, title)

fh = open('_includes/torey.html', 'w')
fh.write(result)
